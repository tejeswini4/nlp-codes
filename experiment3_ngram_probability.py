import re
from collections import Counter

# Step 1: Read a text corpus
text = input("Enter a text corpus: ")

# Step 2: Preprocess the text
text = text.lower()
words = re.findall(r"\b\w+\b", text)

print("\nPreprocessed Text:")
print(words)

# Step 3: Generate unigram counts
unigrams = Counter(words)

print("\nUnigram Counts:")
for word, count in unigrams.items():
    print(word, ":", count)

# Step 4: Generate bigram counts
bigrams = Counter(zip(words, words[1:]))

print("\nBigram Counts:")
for bigram, count in bigrams.items():
    print(bigram, ":", count)

# Step 5: Compute next-word probability using bigram model
first_word = input("\nEnter the current word: ").lower()

next_word = input("Enter the next word: ").lower()

bigram_count = bigrams[(first_word, next_word)]
unigram_count = unigrams[first_word]

if unigram_count > 0:
    probability = bigram_count / unigram_count
    print(
        f"\nP({next_word} | {first_word}) = "
        f"{bigram_count}/{unigram_count} = {probability:.4f}"
    )
else:
    print("The current word is not present in the corpus.")