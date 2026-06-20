
# ------------------ Brute Force ------------------
# Time Complexity : O(n × k)
# Space Complexity: O(k)

n = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

max_avg = float("-inf")

for i in range(len(n) - k + 1):
    subarray = n[i:i+k]
    avg = sum(subarray) / k

    if avg > max_avg:
        max_avg = avg

print(max_avg)


# ---------------- Sliding Window -----------------
# Time Complexity : O(n)
# Space Complexity: O(1)

n = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

window_sum = 0

# First window
for i in range(k):
    window_sum += n[i]

max_avg = window_sum / k

# Slide the window
for i in range(k, len(n)):

    window_sum = window_sum - n[i-k] + n[i]

    avg = window_sum / k

    if avg > max_avg:
        max_avg = avg

print(max_avg)
