#--------------First negative number--------------
# Time Complexity: O(n * k)
# Space Complexity: O(n - k + 1)

arr = [12,-1,-7,8,-15,30,16,28]
k = 3

l = []

for i in range(len(arr) - k + 1):
    is_found = False
    window = arr[i : k + i]

    for j in range(len(window)):
        if window[j] < 0:
            l.append(window[j])
            is_found = True
            break

    if not is_found:
        l.append(0)

print(l)

#-----------------liding window-------------------
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

q = deque()
ans = []

for i in range(len(arr)):

    # Add negative index
    if arr[i] < 0:
        q.append(i)

    # Remove indexes outside current window
    if q and q[0] <= i - k:
        q.popleft()

    # First complete window formed
    if i >= k - 1:
        if q:
            ans.append(arr[q[0]])
        else:
            ans.append(0)

print(ans)



