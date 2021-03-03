def twoSum(nums, target):
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            total = nums[i] + nums[j]
            if target == total:
                print([i, j])

twoSum([5, 11, 40, 15], 55)
