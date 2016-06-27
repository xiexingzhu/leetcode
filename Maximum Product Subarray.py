# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:37:29 2016

@author: kid

Maximum Product Subarray
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        positive_max=0
        negative_min=0
        tmp=max(nums)
        
        for i in range(len(nums)):
            if nums[i]>0:
                posi=positive_max
                nega=negative_min
                positive_max=max(posi*nums[i],nums[i])
                negative_min=nega*nums[i]
            elif nums[i]<0:
                posi=positive_max
                nega=negative_min
                positive_max=nega*nums[i]
                negative_min=min(posi*nums[i],nums[i])
                    
            else:
                positive_max=0
                negative_min=0
        
            tmp=max(tmp,positive_max)
            
        return tmp