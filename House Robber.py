# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:05:50 2016

@author: kid

leetcode House Robber
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums)<3:
            return max(nums) if nums else 0
        tmp=[0]*len(nums)
        
        tmp[0]=nums[0]
        tmp[1]=max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            tmp[i]=max(tmp[i-2]+nums[i],tmp[i-1])
            
        return tmp[-1]
