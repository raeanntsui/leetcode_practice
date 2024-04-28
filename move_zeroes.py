def move_zeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    pointer = 0
    for i in nums:
        if i != 0:
            temp = i
            i = nums[pointer]
            nums[pointer] = temp
            pointer+=1
    return nums

result = move_zeroes([0,1,0,3,12])
print(result)