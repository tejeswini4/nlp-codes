import re

# Step 1: Read a text corpus
text = input("Enter a text corpus: ")

# Step 2: Extract email IDs
emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    text
)

print("\nEmail IDs:")
print(emails)

# Step 3: Extract URLs
urls = re.findall(
    r'https?://[^\s<>"\']+|www\.[^\s<>"\']+',
    text
)

print("\nURLs:")
print(urls)

# Step 4: Extract dates (DD/MM/YYYY or DD-MM-YYYY)
dates = re.findall(
    r'\b\d{2}[/-]\d{2}[/-]\d{4}\b',
    text
)

print("\nDates:")
print(dates)


# Step 5: Minimum Edit Distance
def edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,       # Delete
                dp[i][j - 1] + 1,       # Insert
                dp[i - 1][j - 1] + cost # Substitute
            )

    return dp[m][n], dp


# Step 6: Display edit operations
def display_operations(word1, word2):
    m, n = len(word1), len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    operations = []
    i, j = m, n

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            cost = 0 if word1[i - 1] == word2[j - 1] else 1

            if dp[i][j] == dp[i - 1][j - 1] + cost:
                if cost == 1:
                    operations.append(
                        f"Substitute '{word1[i-1]}' "
                        f"with '{word2[j-1]}'"
                    )
                i -= 1
                j -= 1
                continue

        if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Delete '{word1[i-1]}'")
            i -= 1
        elif j > 0:
            operations.append(f"Insert '{word2[j-1]}'")
            j -= 1

    operations.reverse()

    print("\nEdit Operations:")
    if not operations:
        print("No operations needed. Words are identical.")
    else:
        for operation in operations:
            print(operation)


# Step 7: Get two words from the user
word1 = input("\nEnter the first word: ")
word2 = input("Enter the second word: ")

distance, _ = edit_distance(word1, word2)

print("\nMinimum Edit Distance:", distance)

display_operations(word1, word2)