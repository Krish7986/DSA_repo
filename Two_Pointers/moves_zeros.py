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

# Test Case 1: Original example
nums = [0,1,0,3,12]
print("Test 1:", obj.moveZeroes(nums))  # Expected: [1,3,12,0,0]

# Test Case 2: No zeros
nums = [1,2,3,4,5]
print("Test 2:", obj.moveZeroes(nums))  # Expected: [1,2,3,4,5]

# Test Case 3: All zeros
nums = [0,0,0,0]
print("Test 3:", obj.moveZeroes(nums))  # Expected: [0,0,0,0]

# Test Case 4: Single zero
nums = [0]
print("Test 4:", obj.moveZeroes(nums))  # Expected: [0]

# Test Case 5: Zero at the beginning
nums = [0,1,2,3]
print("Test 5:", obj.moveZeroes(nums))  # Expected: [1,2,3,0]

# Test Case 6: Multiple zeros scattered
nums = [0,0,1,0,2,0,3,4]
print("Test 6:", obj.moveZeroes(nums))  # Expected: [1,2,3,4,0,0,0,0]
