from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_file,
    session
)

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import os

from utils.pdf_reader import extract_text
from utils.gemini_ai import generate_summary, ask_question
from utils.report_generator import generate_report


# --------------------------------------------------
# Flask App
# --------------------------------------------------

app = Flask(__name__)

app.config["SECRET_KEY"] = "gokul123"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


db = SQLAlchemy(app)



# --------------------------------------------------
# Global Variables
# --------------------------------------------------

document_text = ""

last_summary = ""



# --------------------------------------------------
# Database Models
# --------------------------------------------------


class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )


    name = db.Column(
        db.String(100),
        nullable=False
    )


    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )


    password = db.Column(
        db.String(200),
        nullable=False
    )
    
    is_admin = db.Column(
    db.Boolean,
    default=False
)

    documents = db.relationship(
        "Document",
        backref="owner",
        lazy=True
    )



class Document(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )


    filename = db.Column(
        db.String(200)
    )


    summary = db.Column(
        db.Text
    )


    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )



# --------------------------------------------------
# Home
# --------------------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip()
        password = request.form["password"]

        print("=" * 50)
        print("Email Entered :", email)

        user = User.query.filter_by(email=email).first()

        if user:
            print("User Found :", user.email)
            print("Password Match :", check_password_hash(user.password, password))

            if check_password_hash(user.password, password):

                session["user_id"] = user.id
                session["username"] = user.name

                flash("Login Successful", "success")

                return redirect(url_for("dashboard"))

            else:
                flash("Incorrect Password", "danger")

        else:
            print("User Not Found")
            flash("Email does not exist", "danger")

    return render_template("login.html")

# --------------------------------------------------
# Dashboard
# --------------------------------------------------

@app.route("/dashboard")
def dashboard():


    total_users = User.query.count()


    total_documents = Document.query.count()


    total_summaries = Document.query.count()


    total_clause_detection = Document.query.count()



    recent_documents = Document.query.filter_by(

        user_id=session["user_id"]

    ).order_by(

        Document.id.desc()

    ).limit(5).all()



    return render_template(

        "dashboard.html",

        total_users=total_users,

        total_documents=total_documents,

        total_summaries=total_summaries,

        total_clause_detection=total_clause_detection,

        recent_documents=recent_documents,

        username=session.get("username")

    )
# --------------------------------------------------
# Admin Panel
# --------------------------------------------------

@app.route("/admin")
def admin():

    if "user_id" not in session:
        return redirect(url_for("login"))

    total_users = User.query.count()

    total_documents = Document.query.count()

    total_reports = Document.query.count()

    users = User.query.all()

    documents = Document.query.all()

    return render_template(
        "admin.html",
        total_users=total_users,
        total_documents=total_documents,
        total_reports=total_reports,
        users=users,
        documents=documents
    )
# --------------------------------------------------
# Delete User
# --------------------------------------------------

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get_or_404(user_id)

    # Logged-in admin-a delete panna koodadhu
    if user.id == session["user_id"]:
        flash("You cannot delete your own account.")
        return redirect(url_for("admin"))

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully.")

    return redirect(url_for("admin"))
# --------------------------------------------------
# Upload PDF
# --------------------------------------------------

@app.route(
    "/upload",
    methods=["GET","POST"]
)

def upload():


    global document_text

    global last_summary



    if request.method=="POST":



        if "pdf" not in request.files:

            flash(
                "No file selected"
            )

            return redirect(
                url_for("upload")
            )



        pdf=request.files["pdf"]



        if pdf.filename=="":

            flash(
                "Choose PDF"
            )

            return redirect(
                url_for("upload")
            )



        filepath=os.path.join(

            app.config["UPLOAD_FOLDER"],

            pdf.filename

        )


        pdf.save(filepath)



        text=extract_text(
            filepath
        )


        document_text=text



        summary=generate_summary(
            text[:10000]
        )



        last_summary=summary



        document=Document(

            filename=pdf.filename,

            summary=summary,

            user_id=session["user_id"]

        )



        db.session.add(
            document
        )


        db.session.commit()



        return render_template(

            "result.html",

            summary=summary,

            answer=None

        )



    return render_template(
        "upload.html"
    )
# --------------------------------------------------
# Result Page
# --------------------------------------------------

@app.route("/result")
def result():

    return render_template(
        "result.html",
        summary=last_summary,
        answer=None
    )



# --------------------------------------------------
# Ask AI
# --------------------------------------------------

@app.route("/ask", methods=["POST"])
def ask():

    global document_text
    global last_summary


    question = request.form["question"]


    if document_text == "":

        flash(
            "Please upload a document first"
        )

        return redirect(
            url_for("upload")
        )



    answer = ask_question(
        document_text,
        question
    )



    return render_template(

        "result.html",

        summary=last_summary,

        answer=answer

    )



# --------------------------------------------------
# Document History (User Wise + Search)
# --------------------------------------------------

@app.route("/history")
def history():


    search = request.args.get("search")


    user_id = session["user_id"]



    if search:


        documents = Document.query.filter(

            Document.user_id == user_id,

            Document.filename.contains(search)

        ).all()



    else:


        documents = Document.query.filter_by(

            user_id=user_id

        ).all()



    return render_template(

        "history.html",

        documents=documents

    )
@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    upload_count = Document.query.filter_by(
        user_id=user.id
    ).count()

    return render_template(
        "profile.html",
        user=user,
        upload_count=upload_count
    )
@app.route("/admin")
def admin():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    if not user.is_admin:
        flash("Access Denied!")
        return redirect(url_for("dashboard"))

    total_users = User.query.count()
    total_documents = Document.query.count()

    users = User.query.all()
    documents = Document.query.order_by(
        Document.id.desc()
    ).all()

    return render_template(
        "admin.html",
        users=users,
        documents=documents,
        total_users=total_users,
        total_documents=total_documents
    )
@app.route("/check_admin")
def check_admin():

    user = User.query.first()

    if user is None:
        return "No user found"

    return f"""
    Name: {user.name}<br>
    Email: {user.email}<br>
    Admin: {user.is_admin}
    """
# --------------------------------------------------
# View Full Summary
# --------------------------------------------------

@app.route("/history/<int:id>")
def view_summary(id):


    document = Document.query.filter_by(

        id=id,

        user_id=session["user_id"]

    ).first_or_404()



    return render_template(

        "view_summary.html",

        document=document

    )



# --------------------------------------------------
# Download AI Report
# --------------------------------------------------

@app.route("/download_report")
def download_report():


    global last_summary



    if last_summary == "":


        return "No summary available"



    report_path = generate_report(
        last_summary
    )



    return send_file(

        report_path,

        as_attachment=True,

        download_name="AI_Legal_Report.pdf"

    )



# --------------------------------------------------
# Delete Document
# --------------------------------------------------

@app.route("/delete/<int:id>")
def delete_document(id):


    document = Document.query.filter_by(

        id=id,

        user_id=session["user_id"]

    ).first_or_404()



    file_path = os.path.join(

        app.config["UPLOAD_FOLDER"],

        document.filename

    )



    if os.path.exists(file_path):

        os.remove(file_path)



    db.session.delete(
        document
    )


    db.session.commit()



    flash(
        "Document deleted successfully"
    )



    return redirect(
        url_for("history")
    )



# --------------------------------------------------
# Logout
# --------------------------------------------------

@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.")

    return redirect(url_for("home"))

# --------------------------------------------------
# Admin Panel
# --------------------------------------------------

@app.route("/admin")
def admin():

    if "user_id" not in session:
        return redirect(url_for("login"))

    total_users = User.query.count()
    total_documents = Document.query.count()
    total_reports = Document.query.count()

    users = User.query.all()
    documents = Document.query.all()

    return render_template(
        "admin.html",
        total_users=total_users,
        total_documents=total_documents,
        total_reports=total_reports,
        users=users,
        documents=documents
    )
# --------------------------------------------------
# Create Database
# --------------------------------------------------

with app.app_context():

    db.create_all()



# --------------------------------------------------
# Run App
# --------------------------------------------------

if __name__ == "__main__":


    print(
        "="*50
    )

    print(
        "AI Legal Document Analyzer Started"
    )

    print(
        "Open: http://127.0.0.1:5000"
    )

    print(
        "="*50
    )


    app.run(

        debug=True,

        host="127.0.0.1",

        port=5000

    )