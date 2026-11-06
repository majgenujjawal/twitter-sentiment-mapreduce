import sys

sentiment_count = {
    "Positive": 0,
    "Negative": 0,
    "Neutral": 0
}

sentiment_sum = {
    "Positive": 0.0,
    "Negative": 0.0,
    "Neutral": 0.0
}

confusion = {
    "Positive": {"Positive": 0, "Negative": 0, "Neutral": 0},
    "Negative": {"Positive": 0, "Negative": 0, "Neutral": 0}
}

total = 0

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t', 1)

        if key != "SENTIMENT":
            continue

        predicted, actual, score = value.split('|')
        score = float(score)

        sentiment_count[predicted] += 1
        sentiment_sum[predicted] += score

        confusion[actual][predicted] += 1
        total += 1

    except (ValueError, KeyError):
        continue

print("\n========= SENTIMENT DISTRIBUTION =========")

for sentiment in ["Positive", "Negative", "Neutral"]:
    count = sentiment_count[sentiment]
    average = sentiment_sum[sentiment] / count if count else 0
    percentage = (count / total * 100) if total else 0
    print(f"{sentiment}: {count}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Average Compound Score: {average:.4f}")
    print("----------------------------------------")

print("\n========= MODEL EVALUATION =========")

correct = (
    confusion["Positive"]["Positive"]
    + confusion["Negative"]["Negative"]
)

accuracy = correct / total if total else 0

print(f"Total Tweets: {total}")
print(f"Correct Predictions: {correct}")
print(f"Accuracy: {accuracy * 100:.2f}%")

for sentiment in ["Positive", "Negative"]:
    tp = confusion[sentiment][sentiment]
    
    fp = sum(
        confusion[actual][sentiment]
        for actual in ["Positive", "Negative"]
        if actual != sentiment
    )

    fn = sum(
        confusion[sentiment][predicted]
        for predicted in ["Positive", "Negative", "Neutral"]
        if predicted != sentiment
    )

    precision = tp / (tp + fp) if (tp + fp) else 0
    recall = tp / (tp + fn) if (tp + fn) else 0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall) else 0
    )

    print(f"\n{sentiment} Metrics")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")

print("\n========= CONFUSION MATRIX =========")
print("Actual / Predicted")
print("                 Positive Negative Neutral")

for actual in ["Positive", "Negative"]:
    print(
        f"{actual:12}"
        f"{confusion[actual]['Positive']:8}"
        f"{confusion[actual]['Negative']:8}"
        f"{confusion[actual]['Neutral']:8}"
    )