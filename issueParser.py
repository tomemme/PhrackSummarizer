import requests
from transformers import pipeline
from bs4 import BeautifulSoup

# Text extraction function
def fetch_and_parse_issue(url):
    response = requests.get(url)
    if response.status_code == 200:
        text = response.text
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text()
    else:
        print(f"Failed to fetch the issue: {response.status_code}")
        return None

# Filter out ASCII art and irrelevant sections (basic example)
def clean_text(text):
    lines = text.splitlines()
    filtered_lines = []
    for line in lines:
        # Skip lines that are likely ASCII art or headers
        if len(line.strip()) > 5 and not any(char in line for char in "+-_|\\/"):
            filtered_lines.append(line)
    return "\n".join(filtered_lines)

# Summarization logic
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(text):
    if len(text) > 2000:
        return chunk_and_summarize(text)
    else:
        return summarize_text(text)

def summarize_text(text):
    max_len = 150 if len(text) > 1000 else 60
    min_len = 30 if len(text) > 1000 else 20
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False, clean_up_tokenization_spaces=True)
    return summary[0]['summary_text']

def chunk_and_summarize(text, chunk_size=1000):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = [summarizer(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)

# Example usage
url = "http://www.phrack.org/archives/issues/71/10.txt"  # Replace with actual URL
raw_text = fetch_and_parse_issue(url)
if raw_text:
    cleaned_text = clean_text(raw_text)
    summary = summarize_article(cleaned_text)
    print(summary)
