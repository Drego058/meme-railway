from fastapi import FastAPI
import os
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()

@app.get("/scrape")
def scrape_twitter():
    BEARER_TOKEN = os.environ["TWITTER_BEARER_TOKEN"]
    client = tweepy.Client(bearer_token=BEARER_TOKEN)
    analyzer = SentimentIntensityAnalyzer()

    query = "$PEPE OR $DOGE OR memecoin lang:en -is:retweet"
    tweets = client.search_recent_tweets(query=query, max_results=10, tweet_fields=["created_at", "text"])

    results = []
    for tweet in tweets.data:
        text = tweet.text
        sentiment = analyzer.polarity_scores(text)
        label = "positive" if sentiment['compound'] > 0.05 else "negative" if sentiment['compound'] < -0.05 else "neutral"
        results.append({
            "text": text,
            "timestamp": tweet.created_at.isoformat(),
            "sentiment": {
                "compound": sentiment['compound'],
                "label": label
            }
        })

    return results
