#----- contains duplicates------
#-----brute force method-------
def contains_duplicate(nums):                                 #time complexity =O(n²)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))


#-------optimal solution------
def contains_duplicate(nums):                                #time complexity = O(n)
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))
