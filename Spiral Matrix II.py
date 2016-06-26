# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:35:28 2016

@author: xy

leetcode Spiral Matrix II
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        k=1
        tmp=[[0]*n for i in range(n)]
        
        up=0
        left=0
        right=n-1
        down=n-1
        direction=0
        
        while(True):
            if direction==0:
                for i in range(left,right):
                    tmp[up][i]=k
                    k+=1
                up+=1
            if direction==1:
                for i in range(up,down):
                    tmp[right][i]=k
                    k+=1
                right-=1
            if direction==2:
                for i in range(right,left-1,-1):
                    tmp[down][i]=k
                    k+=1
                down-=1
            if direction==3:
                for i in range(down,up-1,-1):
                    tmp[left][i]=k
                    k+=1
                left+=1
                
            if up>down or left>right:
                return tmp
                
            direction=(direction+1)%4