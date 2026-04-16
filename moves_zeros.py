'''283. Move Zeroes
 

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

class Solution(object):
    def moveZeroes(self, nums):
        left,right = 0,0
        for i in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1
        return nums
obj = Solution()
nums = [0,1,0,3,12]
print(obj.moveZeroes(nums))
