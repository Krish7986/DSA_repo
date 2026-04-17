
# Brute Force Approach
def trapping_(nums):
    total = 0
    for i in range(len(nums)):
        left ,right = 0,0
        for j in range(i+1):
            left = max(left,nums[j])
        for j in range(i,len(nums)):
            right = max(right,nums[j])
        total += min(left,right) - nums[i]
    return total

nums = [2, 1, 5, 3, 1, 0, 4]
print(trapping_(nums))

# Optimized
def trapping(nums):
    water = 0
    left,right = 0,len(nums)-1
    max_left,max_right = nums[left],nums[right]
    while (left < right):
        if max_left < max_right:
            left+=1
            max_left = max(max_left,nums[left])
            water+=max_left - nums[left]
        else:
            right-=1
            max_right = max(max_right,nums[right])
            water+=max_right-nums[right]
    return water


nums = [2, 1, 5, 3, 1, 0, 4]
print(trapping(nums))