import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

# Load articles
with open("articles.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()
filtered_words = [word for word in words if word.lower() not in stopwords.words("english")]

# Save cleaned text
with open("cleaned_articles.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(filtered_words))

print("Stopwords removed and saved to cleaned_articles.txt!")
