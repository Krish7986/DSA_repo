'''75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]'''



class Solution:
    def sortcolors(self,nums):
        low,mid,high = 0,0,len(nums)-1
        while mid < high:
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                # if (nums[mid] == 2 ): not necessary
                    nums[mid],nums[high] = nums[high],nums[mid]
                    high-=1
        return nums
                
obj = Solution()
nums = [2,0,2,1,1,0]
print(obj.sortcolors(nums))
nums = [1,0,3,0,1,3,1,3,0]
print(obj.sortcolors(nums))