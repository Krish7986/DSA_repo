'''

Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]'''

class Solution():
    def threesum(self,nums):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    right-=1
        return result
 

obj = Solution()

# Test Case 1: Original example
nums = [-1,0,1,2,-1,-4]
print("Test 1:", obj.threesum(nums))  # Expected: [[-1,-1,2],[-1,0,1]]

# Test Case 2: No valid triplets
nums = [0,1,1,1,1]
print("Test 2:", obj.threesum(nums))  # Expected: []

# Test Case 3: Multiple same values
nums = [-2,0,0,2,2]
print("Test 3:", obj.threesum(nums))  # Expected: [[-2,0,2]]

# Test Case 4: Negative numbers only
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print("Test 4:", obj.threesum(nums))  # Expected: Multiple valid triplets

# Test Case 5: Simple case with duplicates
nums = [-1,-1,0,1,2,-1,-4]
print("Test 5:", obj.threesum(nums))  # Expected: [[-1,-1,2],[-1,0,1]]

# Test Case 6: Only zeros
nums = [0,0,0,0]
print("Test 6:", obj.threesum(nums))  # Expected: [[0,0,0]]