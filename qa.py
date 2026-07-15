from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

def ask_question(question, context):

    answer = qa_pipeline(
        question=question,
        context=context
    )

    return answer['answer']