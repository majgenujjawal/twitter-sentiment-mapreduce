import csv
import re

input_file = "/home/hduser/Downloads/twitter_ujjawal.csv"
output_file = "/home/hduser/Downloads/twitter_ujjawal_processed.csv"

def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r"http\S+|www\S+", "", tweet)
    tweet = re.sub(r"@\w+", "", tweet)
    tweet = tweet.replace("#", "")
    tweet = re.sub(r"[^a-zA-Z\s]", "", tweet)
    tweet = " ".join(tweet.split())
    
    return tweet

total = 0
processed = 0
missing = 0
invalid = 0
malformed = 0

with open(input_file, "r", encoding="utf-8-sig",
            errors="replace", newline="") as infile:

    reader = csv.reader(infile)

    with open(output_file, "w", encoding="utf-8",
              newline="") as outfile:

        writer = csv.writer(outfile)

        for row in reader:
            total += 1
            if len(row) <= 5:
                malformed += 1
                continue

            label = row[0].strip()
            tweet = row[5].strip()

            if label not in ["0", "4"]:
                invalid += 1
                continue

            if not tweet or tweet.lower() in ["nan", "null", "none"]:
                missing += 1
                continue

            tweet = clean_tweet(tweet)

            if not tweet:
                missing += 1
                continue

            row[5] = tweet
            writer.writerow(row)

            processed += 1

print("\nPreprocessing Completed")
print("Total Rows:", total)
print("Processed Rows:", processed)
print("Missing Tweets:", missing)
print("Invalid Labels:", invalid)
print("Malformed Rows:", malformed)
print("Output File:", output_file)