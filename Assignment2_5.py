def maxZeros(nums):
    cnt = 0
    cnt_list = []
    for i in range(len(nums) - 1):
        if nums[i] == 0:
            cnt += 1           
        else:
            cnt_list.append(cnt)
            cnt = 0
    if nums[len(nums) - 1] == 0:
        cnt += 1
        cnt_list.append(cnt)       
    
    print(max(cnt_list))  

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])