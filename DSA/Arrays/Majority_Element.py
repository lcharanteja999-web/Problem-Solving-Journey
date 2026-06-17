#---------------------Brute Force solution----------------------------
def majority_element(arr):

    max_count = 0                                  #Time Complexity: O(n²)
    res = -1

    for i in range(len(arr)):
        count = 0

        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > max_count:
            max_count = count
            res = arr[i]

    if max_count > len(arr) // 2:
        return res
    else:
        return "No Majority Element"


l = list(map(int, input("Enter elements: ").split()))

print(majority_element(l))

#---------------------optimal solution--------------------------------

def majority(arr):                                      #Time Complexity: O(n)
    d = {}

    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    for i in d:
        if d[i] > len(arr) // 2:
            return i
    
    return "no majority element"

l = list(map(int,input("enter elements: ").split()))
print(majority(l))
