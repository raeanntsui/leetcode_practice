def twoSum(nums, target):
    for i in range(len(nums) - 1):
        print("number of current index", i)

    left = 0
    right = 1
    while right < len(nums):
        if nums[left] + nums[right] == target:
            return [left, right]
        right += 1
        if right == len(nums) and left < len(nums) - 2:
            left += 1
            right = left + 1

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)
print("Indices of numbers adding up to target:", result)  

# goal: return index of 2 numbers that add up to the target

# two pointer system:
# left pointer beginning at index 0
# right pointer beginning at index 1
# create a for loop: move right pointer if the target is not reached