import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
from collections import Counter
import os


try:
    nltk.download("stopwords")
    nltk.download("vader_lexicon")
    nltk.download("punkt") 
    nltk.download('punkt_tab')
except Exception as e:
    print(f"Error downloading NLTK data: {e}")

stop_words = set(stopwords.words("english"))
punctuation = set(string.punctuation)

class Comment:
    def __init__(self, text, pos_prob, neu_prob, neg_prob, compound):
        self.text = text
        self.pos_prob = pos_prob
        self.neu_prob = neu_prob
        self.neg_prob = neg_prob
        self.compound = compound

def top_comments(comments, x):
    rtn_comments = []
    try:
        for i in range(x):
            rtn_comments.append(str(comments[i].text))
    except IndexError:
        print(f"Not enough comments to extract {x} number of comments")
    return rtn_comments

def load_comments(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            comments = [x.strip() for x in file if x.strip() != ""]
        return comments
    except Exception as e:
        print(f"Error loading comments: {e}")
        return []

def analyze_sentiments(comments):
    sia = SentimentIntensityAnalyzer()
    pos_comments = []
    neu_comments = []
    neg_comments = []

    for comment in comments:
        score = sia.polarity_scores(comment)
        comment_obj = Comment(comment, score["pos"], score["neu"], score["neg"], score["compound"])
        if score["compound"] > 0.05:  # Positive
            pos_comments.append(comment_obj)
        elif score["compound"] < -0.05:  # Negative
            neg_comments.append(comment_obj)
        else:  # Neutral
            neu_comments.append(comment_obj)

    pos_comments = sorted(pos_comments, key=lambda comment: comment.compound, reverse=True)
    neg_comments = sorted(neg_comments, key=lambda comment: comment.compound)

    return pos_comments, neu_comments, neg_comments

def count_word_frequencies(comments):
    word_dict = Counter()
    for comment in comments:
        comment = re.sub(r"[^\w\s]", "", comment)  # Fix regex for text cleaning
        words = word_tokenize(comment)
        filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word not in punctuation]
        word_dict.update(filtered_words)

    top_20_words = dict(word_dict.most_common(20))
    return top_20_words

def main():
    file_path = "Comments.txt"
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    comments = load_comments(file_path)
    if not comments:
        print("No comments found in the file.")
        return

    pos_comments, neu_comments, neg_comments = analyze_sentiments(comments)
    top_3_comments = top_comments(pos_comments, 3)
    bottom_3_comments = top_comments(neg_comments, 3)
    word_dict = count_word_frequencies(comments)

    print("-------RESULT------------")
    print(f"Positive comments: {len(pos_comments)} percent: {float(len(pos_comments) / len(comments)) * 100:.1f}")
    print(f"Negative comments: {len(neg_comments)} percent: {float(len(neg_comments) / len(comments)) * 100:.1f}")
    print(f"Neutral comments: {len(neu_comments)} percent: {float(len(neu_comments) / len(comments)) * 100:.1f}")

    print(f"Top 20 words: {list(word_dict.keys())}")

    print("\nTop 3 positive comments:\n")
    for i in top_3_comments:
        print(i + "\n")

    print("\nTop 3 negative comments:\n")
    for i in bottom_3_comments:
        print(i + "\n")

if __name__ == "__main__":
    main()