def maxProduct(nums):
    multp = -1
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if multp < nums[i] * nums[j]:
                multp = nums[i] * nums[j]
    print(multp)
    
maxProduct([10, -20, 0, 3])

    