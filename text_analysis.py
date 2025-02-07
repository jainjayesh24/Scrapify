from collections import Counter

# Load cleaned text
with open("cleaned_articles.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()
word_counts = Counter(words)

# Show most common words
print("Top 10 words:", word_counts.most_common(10))
