import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

analyzer = SentimentIntensityAnalyzer()

query = "$PEPE OR $DOGE OR memecoin"
limit = 10
results = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= limit:
        break
    sentiment = analyzer.polarity_scores(tweet.content)
    label = "positive" if sentiment['compound'] > 0.05 else "negative" if sentiment['compound'] < -0.05 else "neutral"
    results.append({
        "text": tweet.content,
        "timestamp": tweet.date.isoformat(),
        "user": tweet.user.username,
        "sentiment": {
            "compound": sentiment['compound'],
            "label": label
        }
    })

# Print resultaten
for r in results:
    print(r)

# Optioneel opslaan
with open("output.json", "w") as f:
    json.dump(results, f, indent=2)
