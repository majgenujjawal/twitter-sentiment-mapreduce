# Twitter Sentiment Analysis using Hadoop MapReduce

## Project Overview

This project implements a Sentiment Analysis Pipeline using **Apache Hadoop MapReduce** to analyze 1.6 million tweets from the Sentiment140 dataset.

The project uses Python and Hadoop Streaming to classify tweets into three sentiment categories:
- Positive
- Negative
- Neutral

It uses a lexicon-based sentiment analysis approach to identify positive and negative words in tweets and calculate sentiment scores.

## Technologies Used

- Python 3
- Apache Hadoop
- Hadoop MapReduce
- Hadoop Streaming
- HDFS (Hadoop Distributed File System)
- Sentiment140 Dataset
- Linux / Ubuntu

## Dataset

The project uses the publicly available Sentiment140 dataset.

Dataset details:
- Total tweets: 1,600,000
- Negative label: 0
- Positive label: 4
- CSV format with 6 columns
- Tweet text is extracted from column 6.

The dataset is not included in this repository because of its large file size.

## Project Structure

```text
twitter-sentiment-mapreduce/
│
├── twitter_mapper.py
├── vader_mapper.py
├── twitter_reducer.py
├── ujjawal_preprocessed.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── screenshot_01.png
    ├── screenshot_02.png
    └── ...
```

## Project Components

### 1. Data Preprocessing

The preprocessing script:
- Converts tweets to lowercase.
- Removes URLs and user mentions.
- Removes hashtag symbols while retaining words.
- Removes punctuation and special characters.
- Removes empty tweets.
- Preserves sentiment labels.

### 2. Sentiment Analysis Mapper

The lexicon-based mapper:
- Identifies positive and negative words.
- Counts matching words.
- Calculates a sentiment score.

Formula:

```text
Score = (Positive Words - Negative Words)
        / (Positive Words + Negative Words)
```

Classification:
- Score greater than 0: Positive
- Score less than 0: Negative
- Score equal to 0: Neutral

### 3. VADER Mapper

The project also includes a VADER-based mapper using the VADER Sentiment Analysis library.

It classifies tweets using compound sentiment scores.

