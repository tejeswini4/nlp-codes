import re
import math
import random
from collections import Counter

# Step 1: Read the text corpus
text = input("Enter a text corpus: ")

# Step 2: Preprocess the corpus
words = re.findall(r"\b\w+\b", text.lower())

if len(words) < 3:
    print("Please enter a longer text corpus.")
    raise SystemExit

print("\nPreprocessed Corpus:")
print(words)

# Step 3: Split into training and test sets
random.seed(42)
random.shuffle(words)

split_index = int(0.8 * len(words))

train_data = words[:split_index]
test_data = words[split_index:]

if not train_data or not test_data:
    print("Not enough words to create train and test sets.")
    raise SystemExit

print("\nTraining Data:")
print(train_data)

print("\nTesting Data:")
print(test_data)

# Step 4: Train a bigram language model
unigrams = Counter(train_data)
bigrams = Counter(zip(train_data, train_data[1:]))

vocabulary = set(train_data)
vocabulary_size = len(vocabulary)

# Step 5: Compute perplexity with Laplace smoothing
def calculate_perplexity(test_words, unigrams, bigrams,
                         vocabulary_size):
    if not test_words:
        return float("inf")

    log_probability = 0.0
    total_predictions = 0

    for i in range(1, len(test_words)):
        previous_word = test_words[i - 1]
        current_word = test_words[i]

        bigram_count = bigrams[(previous_word, current_word)]
        previous_count = unigrams[previous_word]

        # Laplace smoothing
        probability = (
            (bigram_count + 1) /
            (previous_count + vocabulary_size)
        )

        log_probability += math.log(probability)
        total_predictions += 1

    if total_predictions == 0:
        return float("inf")

    return math.exp(-log_probability / total_predictions)

# Step 6: Display perplexity
perplexity = calculate_perplexity(
    test_data,
    unigrams,
    bigrams,
    vocabulary_size
)

print("\nN-gram Language Model: Bigram")
print("Training Size:", len(train_data))
print("Testing Size:", len(test_data))
print("Vocabulary Size:", vocabulary_size)
print("Test Perplexity:", round(perplexity, 4))