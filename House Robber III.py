# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 14:52:18 2016

@author: kid

leetcode House Robber III
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs_rob(root)[0]
 
    def dfs_rob(self, root):
        if not root: return 0,0
        rob_L, no_rob_L = self.dfs_rob(root.left)
        rob_R, no_rob_R = self.dfs_rob(root.right)
        return max(no_rob_L + no_rob_R + root.val , rob_L + rob_R), rob_L + rob_R