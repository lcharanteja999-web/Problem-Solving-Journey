#--------------Brute Force solution---------------------

def anagram(l1, l2):                    #Time complexity = O(n²)

    if len(l1) != len(l2):
        print("Not Anagram")
        return

    l2 = list(l2)

    for i in range(len(l1)):
        is_anagram = False

        for j in range(len(l2)):

            if l1[i] == l2[j]:
                is_anagram = True
                l2[j] = "*"      # mark as used
                break

        if not is_anagram:
            print("Not Anagram")
            return

    print("Anagram")


l1 = input("Enter first word: ")
l2 = input("Enter second word: ")

anagram(l1, l2)

#---------------------optimal solution----------------------
def anagram(l1, l2):                                            #Time complexity = O(n)

    if len(l1) != len(l2):
        return False

    d = {}

    # Count characters in first string
    for ch in l1:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1

    # Decrease count using second string
    for ch in l2:
        if ch not in d:
            return False
        d[ch] -= 1

    # Check if all counts are 0
    for value in d.values():
        if value != 0:
            return False

    return True


l1 = input("Enter first word: ")
l2 = input("Enter second word: ")

if anagram(l1, l2):
    print("Anagram")
else:
    print("Not Anagram")
