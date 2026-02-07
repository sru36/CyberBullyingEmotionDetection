# cyberbullying_emotion_detection.py

# ===============================
# 1. IMPORT LIBRARIES
# ===============================
import pandas as pd
import numpy as np
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import pipeline

# ===============================
# 2. DOWNLOAD NLTK RESOURCES
# ===============================
nltk.download('punkt')
nltk.download('stopwords')

# ===============================
# 3. LOAD DATASET
# ===============================
# Make sure CBTweets.csv is in the same folder
df = pd.read_csv("CBTweets.csv")

print("Dataset loaded successfully")
print(df.head())

# ===============================
# 4. TEXT CLEANING FUNCTION
# ===============================
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)      # remove URLs
    text = re.sub(r"@\w+", "", text)          # remove mentions
    text = re.sub(r"#\w+", "", text)          # remove hashtags
    text = re.sub(r"[^a-z\s]", "", text)      # remove special characters
    
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(tokens)

# Apply cleaning
df["clean_text"] = df["tweet_text"].apply(clean_text)

print("Text cleaning completed")

# ===============================
# 5. LOAD EMOTION CLASSIFIER
# ===============================
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=False
)

print("Emotion model loaded")

# ===============================
# 6. EMOTION DETECTION FUNCTION
# ===============================
def detect_emotion(text):
    try:
        result = emotion_classifier(text[:512])
        return result[0]['label']
    except Exception as e:
        return "unknown"

# ===============================
# 7. CREATE EMOTION COLUMN
# ===============================
print("Emotion detection started (this may take time)...")

df["Emotion"] = df["clean_text"].apply(detect_emotion)

print("Emotion column added")

# ===============================
# 8. SAVE FINAL DATASET
# ===============================
output_file = "cyberbullying_with_emotion.xlsx"
df.to_excel(output_file, index=False)

print(f"Final dataset saved as {output_file}")

# ===============================
# 9. BASIC SUMMARY
# ===============================
print("\nEmotion Distribution:")
print(df["Emotion"].value_counts())
