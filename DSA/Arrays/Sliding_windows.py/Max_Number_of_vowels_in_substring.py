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

window_count = sum(1 for ch in s[:k] if ch in "aeiou")
max_count = window_count

for i in range(k,len(s)):
    if s[i-k] in "aeiou":
        window_count -= 1
    
    if s[i] in "aeiou":
        window_count += 1

    max_count = max(max_count,window_count)
print(max_count)
