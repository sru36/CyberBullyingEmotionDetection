# Cyberbullying Emotion Detection using NLP

## 📌 Project Overview

This project analyzes social media text to detect **cyberbullying-related emotions** using Natural Language Processing (NLP). Starting from a real-world dataset of tweets, the system cleans the text, applies a pre-trained transformer-based emotion classification model, and generates a new **Emotion** column for each tweet.

The project demonstrates practical usage of:

* Text preprocessing
* Feature engineering
* Transformer-based emotion detection
* Data handling with Python

This is designed as a **B.Tech / undergraduate-level NLP project** with real-world relevance.

---

## 🎯 Objectives

* Load and preprocess a cyberbullying tweet dataset
* Clean noisy social media text
* Automatically classify emotions such as **anger, joy, sadness, fear, disgust, neutral**
* Add detected emotions as a new column in the dataset
* Save the enriched dataset for further analysis

---

## 📂 Dataset

**Source:** Kaggle / GitHub (Cyberbullying Tweets Dataset)

**Columns used:**

* `tweet_text` – Raw tweet content
* `cyberbullying_type` – Cyberbullying label

A new column is generated:

* `Emotion` – Detected emotion using NLP model

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Pandas** – Data handling
* **NumPy** – Numerical operations
* **NLTK** – Stopword removal
* **Transformers (Hugging Face)** – Emotion detection model
* **Torch** – Model backend
* **OpenPyXL** – Excel file handling

---

## ⚙️ Project Structure

```
project-folder/
│
├── CBTweets.csv
├── cyberbullying_emotion_detection.py
├── cyberbullying_with_emotion.xlsx
├── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install pandas numpy nltk transformers torch openpyxl
```

### 2️⃣ Run the Script

```bash
python cyberbullying_emotion_detection.py
```

### 3️⃣ Output

* A new Excel file named `cyberbullying_with_emotion.xlsx` is generated
* The file contains a new **Emotion** column

---

## 🧠 Methodology

1. Load the dataset using Pandas
2. Clean tweet text (lowercasing, removing URLs, mentions, special characters)
3. Remove stopwords for better semantic understanding
4. Apply a pre-trained transformer-based emotion classifier
5. Store the predicted emotion for each tweet
6. Save the updated dataset for analysis

---

## 📊 Emotions Detected

* Anger
* Joy
* Sadness
* Fear
* Disgust
* Neutral

---

## ✅ Key Highlights

* Uses **real-world noisy data**
* No manual emotion labeling
* Transformer-based NLP model
* Scalable and extendable

---

## 🔮 Future Enhancements

* Train a cyberbullying prediction model
* Correlate emotions with bullying categories
* Build a web interface for real-time detection
* Optimize inference using batch processing

---

## 👩‍💻 Author

**Srushti**
B.Tech – Artificial Intelligence & Data Science

---

## 📜 License

This project is for **academic and educational purposes only**.
