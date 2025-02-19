import streamlit as st
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url = st.text_input("Enter the URL of the news article")

    if st.button("Summarize"):
        if not url:
            st.error("Please enter a valid URL")
            return

        with st.spinner("Summarizing the article..."):
            try:
                article = Article(url)

                article.download()
                article.parse()
                article.nlp()

                if not article.text:
                    st.error("Invalid URL or unable to extract content. Please check the URL and try again.")
                    return

                st.subheader("Title")
                st.write(article.title if article.title else "Not Available")

                st.subheader("Author(s)")
                st.write(', '.join(article.authors) if article.authors else "Not Available")

                st.subheader("Publishing Date")
                st.write(article.publish_date if article.publish_date else "Not Available")

                st.subheader("Summary")
                st.write(article.summary if article.summary else "Summary not available")

                analysis = TextBlob(article.text)
                sentiment_text = f"Polarity: {analysis.polarity:.2f}, Sentiment: {'Positive' if analysis.polarity > 0 else 'Negative' if analysis.polarity < 0 else 'Neutral'}"

                st.subheader("Sentiment Analysis")
                st.write(sentiment_text)

            except Exception as e:
                st.error(f"Invalid URL")

    st.markdown("<p style='text-align: center; font-size: 16px;'>👨‍💻 Made by <b>Yashwanth</b></p>", unsafe_allow_html=True)

if __name__ == "__main__":
    st.title("📰 News Summarizer")
    summarize()
    
