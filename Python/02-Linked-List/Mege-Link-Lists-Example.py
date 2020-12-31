# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 16:48:50 2020

@author: SethHarden

Merge a list of lists
"""

class Solution:
    def mergeKLists(self, lists):
        if not self.lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
    
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    
    mergeKLists([[1,4,5],[1,3,4],[2,6]])