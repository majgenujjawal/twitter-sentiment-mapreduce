import sys
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

for row in csv.reader(sys.stdin):
    try:
        # Extract CSV columns
        original_label = row[0].strip()
        tweet = row[5].strip()

        if not tweet:
            continue

        # Convert original dataset labels
        if original_label == "0":
            actual_sentiment = "Negative"
        elif original_label == "4":
            actual_sentiment = "Positive"
        else:
            continue

        # VADER sentiment analysis
        scores = analyzer.polarity_scores(tweet)
        compound = scores['compound']

        # Classify sentiment
        if compound >= 0.05:
            predicted_sentiment = "Positive"
        elif compound <= -0.05:
            predicted_sentiment = "Negative"
        else:
            predicted_sentiment = "Neutral"

        # Emit key-value pair
        print(
            f"SENTIMENT\t"
            f"{predicted_sentiment}|"
            f"{actual_sentiment}|"
            f"{compound}"
        )

    except (IndexError, ValueError):
        continue