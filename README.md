# 📊 YouTube Comment Sentiment Analysis
🚀 Analyze YouTube comments with sentiment analysis to gain insights into audience opinions!

## 🔍 Overview
This Python-based project extracts comments from a YouTube video using the YouTube Data API v3, processes them for sentiment analysis using NLTK's SentimentIntensityAnalyzer, and provides key insights such as:

- Positive, Negative, and Neutral Sentiment Distribution
- Top 3 Most Positive & Negative Comments
- Most Frequently Used Words in Comments

## 🛠 Features
✅ Extract YouTube comments in bulk  
✅ Perform sentiment analysis (Positive, Neutral, Negative)  
✅ Identify trending words in the comments  
✅ Rank top & bottom comments based on sentiment score  
✅ Handles large datasets efficiently  

## 📦 Installation
### 1️⃣ Clone the repository:
```sh
git clone https://github.com/AdityaPrmr/Youtube-Comment-Sentiment-Analysis.git
cd Youtube-Comment-Sentiment-Analysis
```
### 2️⃣ Install dependencies:
```sh
pip install google-api-python-client nltk
```
### 3️⃣ Download NLTK datasets (if not already installed):
```python
import nltk
nltk.download("stopwords")
nltk.download("vader_lexicon")
nltk.download("punkt")
```
### 4️⃣ Set up your YouTube API Key:
- Open `fetch_comments.py`.
- Replace `api_key = ""` with your actual API Key.

## 🚀 Usage
### 1️⃣ Extract YouTube Comments:
Run the script to fetch comments:
```sh
python fetch_comments.py
```
The comments will be saved in `Comments.txt`.

### 2️⃣ Perform Sentiment Analysis:
Run the analysis script:
```sh
python analyze_comments.py
```
This script will:
- Analyze sentiment distribution in the comments.
- Display the most positive and negative comments.
- Show the top 20 most frequently used words.

## 📜 Project Structure
```
📂 Youtube-Comment-Sentiment-Analysis
│── fetch_comments.py   # Fetches YouTube comments & saves them in Comments.txt
│── analyze_comments.py # Analyzes comments using sentiment analysis
│── Comments.txt        # Stores extracted YouTube comments
│── README.md           # Project documentation
```

## 📌 Notes
- The YouTube API has a daily quota limit; make sure not to exceed it.
- Increase the `MAX_API_CALLS` limit carefully based on your quota.
- Modify the analysis logic in `analyze_comments.py` to suit your specific needs.

## 👨‍💻 Author
🔹 **Aditya Parmar**  
🔹 GitHub: [@AdityaPrmr](https://github.com/AdityaPrmr)  
🔹 LinkedIn: [Aditya Parmar](https://www.linkedin.com/in/adityaparmar-)  

## ⭐ Like this project?
Feel free to star ⭐ the repository and contribute to improving it! 🚀
