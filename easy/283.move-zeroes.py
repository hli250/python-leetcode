#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    
        for i in range (len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
            

        
# @lc code=end

