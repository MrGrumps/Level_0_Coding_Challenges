#Task 0.6
def maximum(*nums):
    check = nums[0]
    for num in nums:
        if check < num:
            check = num
    return(check)
    
maximum(1,10,5,15,1,4)