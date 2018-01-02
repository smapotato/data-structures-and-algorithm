"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = -1 #nums[0...zero] == 0
        two = len(nums) #nums[two...n-1] == 2
        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[i],nums[two] = nums[two],nums[i]
            else:
                zero += 1
                nums[i],nums[zero] = nums[zero],nums[i]
                i += 1
