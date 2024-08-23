# HTMLTextSummarizer

## Overview
HTMLTextSummarizer is a Python-based tool designed to summarize text content extracted from HTML files. While it's currently a general-purpose tool, it can be adapted to specific use cases such as summarizing technical articles, research papers, or Phrack magazine issues.

## Features
- Extracts and cleans text from HTML files.
- Filters out irrelevant content like ASCII art or headers.
- Summarizes text using transformer-based models.

Python 3.6 or higher
## Installation
```bash
git clone https://github.com/tomemme/HTMLTextSummarizer.git
cd HTMLTextSummarizer
##create a virtual environment for imports
python3 -m venv summarizer_env
source summarizer_env/bin/activate  # On Windows: summarizer_env\Scripts\activate
pip install -r requirements.txt
or do individually
pip install requests beautifulsoup4 transformers
##close venv
deactivate


