# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:38:30 2016

@author: kid

leetcode House Robber II
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robbery(nums):
            if len(nums)<3:
                return max(nums) if nums else 0
            else:
                tmp=[0]*len(nums)
                tmp[0]=nums[0]
                tmp[1]=max(nums[0],nums[1])
                
                for i in range(2,len(nums)):
                    tmp[i]=max(tmp[i-1],tmp[i-2]+nums[i])
                    
                return tmp[-1]
                
        if len(nums)<3:
            return max(nums) if nums else 0

        
        return max(robbery(nums[1:]),robbery(nums[:-1]))