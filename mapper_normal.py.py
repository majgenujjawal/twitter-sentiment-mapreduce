import sys
import csv

POSITIVE_WORDS = {"good", "great", "awesome", "love", "happy", "best", "nice", "wonderful", "positive", "amazing", "thanks", "cool", "exciting"}
NEGATIVE_WORDS = {"bad", "awful", "terrible", "hate", "sad", "worst", "poor", "horrible", "negative", "angry", "disappoint", "useless", "fail", "wrong", "boring"}

for row in csv.reader(sys.stdin):
    try:
        label = row[0].strip()
        tweet = row[5].strip()

        if not tweet:
            continue

        if label == "0":
            actual = "Negative"
        elif label == "4":
            actual = "Positive"
        else:
            continue

        # Count positive and negative words in the tweet
        words = set(tweet.lower().split())
        pos_count = len(words.intersection(POSITIVE_WORDS))
        neg_count = len(words.intersection(NEGATIVE_WORDS))

        # Calculate simple compound score (-1.0 to 1.0)
        total = pos_count + neg_count
        if total == 0:
            score = 0.0
        else:
            score = (pos_count - neg_count) / total

        # Classify sentiment
        if score > 0:
            predicted = "Positive"
        elif score < 0:
            predicted = "Negative"
        else:
            predicted = "Neutral"
        
        print(f"SENTIMENT\t{predicted}|{actual}|{score}")

    except (IndexError, ValueError):
        continue