# AI News Summarizer

A Python-based tool that retrieves news articles from external sources and produces short, meaningful summaries using NLP techniques.

---

## Features

* Fetches news from RSS feeds or APIs
* Extracts and cleans article text
* Generates concise, high-quality summaries using NLP

---

## Requirements

* Python **3.10+**
* A virtual environment is **highly recommended**

---

## Setup

### 1. Clone the Repository

```bash
git clone <repo-url>
cd ai-news-summarizer
```

---

## From Scratch (Recommended)

### 1. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

```bash
source venv/bin/activate
```

### 3. Verify the Environment

You can confirm the virtual environment is active by checking:

* The `venv/` folder exists
* VS Code interpreter selection (`Cmd + Shift + P`)
* Environment variables:

  ```bash
  echo $VIRTUAL_ENV
  which python
  ```
* Config file:
  `venv/pyvenv.cfg`

---

## Install Dependencies

### Install from `requirements.txt`

```bash
python -m pip install -r requirements.txt
```

### View Installed Packages

```bash
pip list
```

### Update or Create `requirements.txt`

```bash
# Overwrite
python -m pip freeze > requirements.txt

# Append
python -m pip freeze >> requirements.txt
```

---

## Run the Project

```bash
python -m src.main
```

