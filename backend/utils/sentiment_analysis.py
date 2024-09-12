from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline('sentiment-analysis')

def analyze_sentiment(content):
    result = sentiment_analyzer(content)[0]
    return result
