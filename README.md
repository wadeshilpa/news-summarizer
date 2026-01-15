# AI News Summarizer

A Python project that fetches news articles and generates short summaries using NLP.

---

## Features
- Fetches news from RSS feeds or APIs
- Extracts article text
- Generates concise summaries using NLP

---

## Requirements
- Python 3.10+
- Virtual environment (recommended)

---

## Setup

### 1. Clone the repository
```bash
git clone <repo-url>
cd ai-news-summarizer

## From scratch
Create virtual environment:
python3 -m venv venv

Activate virtual environment:
source venv/bin/activate

Verify if virtual environment is created:
- Look for a venv folder in your project
- Cmd+Shift+P
- echo $VIRTUAL_ENV 
- which python
- Check pyvenv.cfg 

Install all the libraries from requirements.txt:
python -m pip install -r requirements.txt

List the libraries:
pip list

create or update requirements.txt
python -m pip freeze > requirements.txt -------overwrites
python -m pip freeze >> requirements.txt --------appends


Run code :
python -m src.main


