import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url = utext.get('1.0', "end").strip()
    if not url:
        return

    try:
        article = Article(url)

        article.download()
        article.parse()
        article.nlp()

        for widget in [title, author, publication, summary, sentiment]:
            widget.config(state='normal')

        def safe_insert(widget, data):
            widget.delete('1.0', 'end')
            widget.insert('1.0', data if data else "Not Available")

        safe_insert(title, article.title)
        safe_insert(author, ', '.join(article.authors) if article.authors else "Not Available")
        safe_insert(publication, article.publish_date if article.publish_date else "Not Available")
        safe_insert(summary, article.summary if article.summary else "Summary not available")

        analysis = TextBlob(article.text)
        sentiment_text = f'Polarity: {analysis.polarity:.2f}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}'
        safe_insert(sentiment, sentiment_text)

        for widget in [title, author, publication, summary, sentiment]:
            widget.config(state='disabled')

    except Exception as e:
        print(f"Error: {e}")
        safe_insert(summary, "Error occurred during summarization. Please check the URL.")

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# Link the summarize function to the button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
