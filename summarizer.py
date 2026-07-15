from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):

    if len(text) > 2000:
        text = text[:2000]

    summary = summarizer(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return summary[0]['summary_text']