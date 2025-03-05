def move_zeroes(nums):
    pointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pointer], nums[i] = nums[i], nums[pointer]
            pointer += 1
    return nums

result = move_zeroes([0,1,0,3,12])
print(result)