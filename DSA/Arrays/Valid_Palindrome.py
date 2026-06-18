# ---------------------------Brute Force Solution---------------
# Time Complexity: O(n)
# Space Complexity: O(n)

def palindrome(word):

    reverse = ""

    for i in range(len(word) - 1, -1, -1):
        reverse += word[i]

    if reverse == word:
      return True
    else:
      return False


word = input("Enter word: ")
print(palindrome(word))

#----------------------- Optimal Solution (Two Pointers)-----------------------

# Time Complexity: O(n)
# Space Complexity: O(1)

def palindrome(word):

    left = 0
    right = len(word) - 1

    while left < right:

        if word[left] != word[right]:
            return False

        left += 1
        right -= 1

    return True


word = input("Enter word: ")
print(palindrome(word))
