''' Two pointers 
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Contraints
2 ≤ numbers.length ≤ 3 × 10⁴
👉 Array will have at least 2 elements and can go up to 30,000 → so solution must be efficient (no O(n²))
numbers is sorted in non-decreasing order
👉 Elements are already sorted → we can use two pointers instead of hashmap
There is exactly one solution
👉 No confusion → once we find the pair, we can directly return



'''
class Solution:
    def two_pointers(self,nums,target):
        left,right = 0,len(nums)-1
        while left < right:
            sum = nums[left]+nums[right]
            if sum == target:
                return ([left+1, right+1])
            elif sum < target:
                left+=1
            else:
                right-=1  
            
obj = Solution()
nums = [2,7,11,15]
target = 9
print(obj.two_pointers(nums,target))