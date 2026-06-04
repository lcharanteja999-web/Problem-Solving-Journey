#---------------Brute force method--------

def two_sum(nums, target):                                          #Time complexity  = O(n²)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


nums = [2, 12, 11, 7, 15]
target = 9

print(two_sum(nums, target))


#-------------optimal solution----------------

def two_sum(nums, target):                       #time complexity = O(n)
    d = {}
 
    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in d:
            return [d[needed], i]

        d[nums[i]] = i


nums = [2, 12, 11, 7, 15]
target = 9

print(two_sum(nums, target))
