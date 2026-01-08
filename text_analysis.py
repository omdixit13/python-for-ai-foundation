from collections import Counter

text = input("Enter text: ")

words = text.lower().split()
sentences = text.split(".")

word_count = len(words)
sentence_count = len([s for s in sentences if s.strip()])

common_word = Counter(words).most_common(1)[0][0]

print("Word Count:", word_count)
print("Sentence Count:", sentence_count)
print("Most Common Word:", common_word)
