# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:41:07 2016

@author: kid

leetcode  Partition List
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h=head
        h1=ListNode(-1)
        h2=head
        Head=h1
        h1.next=h
        
        while(h2):
            if h2.val>=x:
                Head=h2
                h2=h2.next
            else:
                if h1.next==h2:
                    Head=h2
                    h1=h1.next
                    h2=h2.next
                else:
                    Head.next=h2.next
                    tmp=h2
                    h2=h2.next
                    if h1.next==h:
                        h=tmp
                    tmp.next=h1.next
                    h1.next=tmp
                    h1=h1.next
                    
        return h
