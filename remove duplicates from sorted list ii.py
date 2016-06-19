# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:03:57 2016

@author: kid

leetcode Remove Duplicates from Sorted List ||
"""

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        H=head
        t=False
        Head=head
        if head==None:
            return head
        if head.next==None:
            return head
        
        while(head and head.next):
            if head.val == head.next.val:
                t=True
            while(head and head.next and head.val==head.next.val):
                head.next=head.next.next
            
            if t:
                if head==H:
                    H=head.next
                else:
                    Head.next=head.next
                    
                t=False
            
            else:
                Head=head    
            head=head.next
            
        return H
