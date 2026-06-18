#--------------------------------------------------Brute Force Solution------------------

# Time Complexity: O(n²)
# Space Complexity: O(1)

def two_sum(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return (i + 1, j + 1)


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print(two_sum(nums, target))

# -------------------------------------------------Optimal Solution (Two Pointers)------------------------------------
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: Works only for a sorted array.

def two_sum(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        if nums[left] + nums[right] == target:
            return (left + 1, right + 1)

        elif nums[left] + nums[right] < target:
            left += 1

        else:
            right -= 1


nums = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))

print(two_sum(nums, target))
