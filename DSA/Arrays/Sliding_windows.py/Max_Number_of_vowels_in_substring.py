# ------------------ Brute Force ------------------
# Time Complexity : O(n × k)
# Space Complexity: O(k)

s = input("Enter string: ")
k = int(input("Enter k: "))

max_count = 0

for i in range(len(s) - k + 1):

    substring = s[i:i+k]

    count = 0

    for ch in substring:
        if ch in "aeiou":
            count += 1

    if count > max_count:
        max_count = count

print(max_count)


# ---------------- Sliding Window -----------------
# Time Complexity : O(n)
# Space Complexity: O(1)

s = input("Enter string: ")
k = int(input("Enter k: "))

count = 0

# First window
for i in range(k):
    if s[i] in "aeiou":
        count += 1

max_count = count

# Slide the window
for i in range(k, len(s)):

    # Remove leaving character
    if s[i-k] in "aeiou":
        count -= 1

    # Add entering character
    if s[i] in "aeiou":
        count += 1

    if count > max_count:
        max_count = count

print(max_count)
