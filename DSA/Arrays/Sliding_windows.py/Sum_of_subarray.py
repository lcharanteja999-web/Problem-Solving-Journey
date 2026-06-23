# ---------------- Brute Force Solution ----------------
# Time Complexity: O(n*k)
# Space Complexity: O(k)
#Since brute force uses slicing, arr[i:i+k] creates a temporary list of size k, so the space complexity is O(k)

arr = [2,1,5,1,3,2]
k = 3

max_sum = 0

for i in range(len(arr) - k + 1):
    current_sum = sum(arr[i:i+k])
    max_sum = max(current_sum, max_sum)

print(max_sum)


# ---------------- Sliding Window Solution ----------------
# Time Complexity: O(n)
# Space Complexity: O(1)


arr = [2,1,5,1,3,2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    max_sum = max(max_sum, window_sum)

print(max_sum)
