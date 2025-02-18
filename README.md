# 📰 News Summarizer

A simple **News Summarizer** application built with **Python** and **Tkinter**. It extracts and summarizes news articles from a given URL and provides sentiment analysis.

## 📌 Features

- Extracts and displays:
  - Article Title
  - Author(s)
  - Publishing Date
  - Summary of the Article
  - Sentiment Analysis (Positive, Negative, or Neutral)
- User-friendly interface built with **Tkinter**.
- Handles missing fields gracefully (displays "Not Available").
- Provides error messages for invalid URLs.

## 🛠️ Installation

Ensure you have **Python 3.10+** installed.

1. **Clone the Repository:**

```bash
    git clone https://github.com/your-username/news-summarizer.git
    cd news-summarizer
```

2. **Create a Virtual Environment (Optional but Recommended):**

```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**

```bash
    pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install the libraries:

```bash
    pip install newspaper3k textblob nltk
```

4. **Download NLTK Data (if required):**

```python
    import nltk
    nltk.download('punkt')
```

## ▶️ Usage

Run the application using the following command:

```bash
    python app.py
```

### How to Use:

1. Enter the URL of a news article.
2. Click the **"Summarize"** button.
3. View the extracted information and sentiment analysis.


## 📂 Project Structure

```
news-summarizer/
├── app.py              # Main application code
└── README.md           # Project documentation
```

## ✅ Requirements

- Python 3.10+
- newspaper3k
- textblob
- nltk

## 🐞 Troubleshooting

1. **Missing article content?**
   Ensure the article is publicly accessible and properly formatted.

2. **ImportError: newspaper module not found**
   Ensure you installed the `newspaper3k` package:
   ```bash
   pip install newspaper3k
   ```

## 📜 License

This project is licensed under the **MIT License**.

## 🤝 Contributing

Feel free to fork the repository and submit a pull request if you want to improve the project!

## 🌟 Acknowledgements

- [newspaper3k](https://github.com/codelucas/newspaper) for article extraction.
- [TextBlob](https://textblob.readthedocs.io/) for sentiment analysis.

---

💡 **Happy Summarizing!**

