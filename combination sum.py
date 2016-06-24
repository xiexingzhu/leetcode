# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:18:01 2016

@author: kid

leetcode  Algorithm combination sum
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        tmp=[]
        count=[]
        
        for i in range(len(candidates)):
            #print tmp
            if not len(tmp)==0:
                for j in range(len(tmp)):
                    if not tmp[j]==-1:
                        if sum(tmp[j])+candidates[i]>target:
                            tmp[j]=-1
                        elif sum(tmp[j])+candidates[i]<target:
                            Tmp=list(tmp[j])
                            while sum(Tmp)+candidates[i]<=target:
                                Tmp.append(candidates[i])
                                if sum(Tmp)==target:
                                    count.append(Tmp)
                                else:
                                    tmp.append(list(Tmp))
                            
                        else:
                            tmp[j].append(candidates[i])
                            count.append(tmp[j])
                        
                s=[]
                ss=[]
                while(sum(ss)<=target):
                    if sum(ss)==target:
                        count.append(list(ss))
                    else:
                        if not ss==[]:
                            s.append(list(ss))
                    ss.append(candidates[i])
                        
                tmp.extend(s)
            else:
                s=[]
                ss=[]
                while(sum(ss)<=target):
                    if sum(ss)==target:
                        count.append(list(ss))
                    else:
                        if not ss==[]:
                            s.append(list(ss))
                    ss.append(candidates[i])
                tmp.extend(s)
                
                
        return count

