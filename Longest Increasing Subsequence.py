# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 22:58:33 2016

@author: xy

leetcode Longest Increasing Subsequence
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp=[]
        if nums==[]:
            return 0
        
        for i in range(len(nums)):
            if len(tmp)==0:
                tmp.append([nums[i]])
                
            elif nums[i]>tmp[-1][-1]:
                s=list(tmp[-1])
                s.append(nums[i])
                tmp.append(s)
                
            elif nums[i]<=tmp[0][0]:
                tmp[0][0]=nums[i]
            elif nums[i]==tmp[-1][-1]:
                continue
            else:
                j=len(tmp)-1
                while(tmp[j][-1]>nums[i]):
                    j-=1
                    
                if tmp[j][-1]==nums[i]:
                    continue
                s=list(tmp[j])
                s.append(nums[i])
                tmp[j+1]=s
        
        return len(tmp[-1])