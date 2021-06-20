# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if head == None or head.next == None: return
        
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        n1, n2 = head, prev
        while n2.next != None:
            tmp = n1.next
            n1.next = n2
            n1 = tmp
            
            tmp = n2.next
            n2.next = n1
            n2 = tmp
        