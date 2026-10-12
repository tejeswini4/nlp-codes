import re
from collections import Counter

# Step 1: Read a text corpus
text = input("Enter a text corpus: ")

# Step 2: Sentence tokenization
sentences = re.split(r'(?<=[.!?])\s+', text.strip())
sentences = [s for s in sentences if s]

print("\nSentence Tokenization:")
for sentence in sentences:
    print(sentence)

# Step 3: Word tokenization
words = re.findall(r"\b\w+(?:'\w+)?\b", text.lower())

print("\nWord Tokenization:")
print(words)

# Step 4: Byte Pair Encoding (BPE)
def learn_bpe(corpus, num_merges=10):
    vocab = Counter()

    for word in corpus:
        chars = tuple(list(word) + ["</w>"])
        vocab[chars] += 1

    for _ in range(num_merges):
        pairs = Counter()

        for word, freq in vocab.items():
            for i in range(len(word) - 1):
                pairs[(word[i], word[i + 1])] += freq

        if not pairs:
            break

        best_pair = max(pairs, key=pairs.get)
        new_vocab = Counter()

        for word, freq in vocab.items():
            new_word = []
            i = 0

            while i < len(word):
                if (
                    i < len(word) - 1
                    and (word[i], word[i + 1]) == best_pair
                ):
                    new_word.append(word[i] + word[i + 1])
                    i += 2
                else:
                    new_word.append(word[i])
                    i += 1

            new_vocab[tuple(new_word)] += freq

        vocab = new_vocab

    return vocab

# Step 5: Generate subword vocabulary
bpe_vocab = learn_bpe(words, num_merges=10)

print("\nBPE Subword Vocabulary:")
for subword, frequency in bpe_vocab.items():
    print(" ".join(subword), ":", frequency)

# Step 6: Display unique subword tokens
subwords = set()

for word in bpe_vocab:
    subwords.update(word)

print("\nGenerated Subword Tokens:")
print(sorted(subwords))