# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1, num2 = 0, 0
        
        while l1:
            num1 = num1*10 + l1.val
            l1 = l1.next
        
        while l2:
            num2 = num2*10 + l2.val
            l2 = l2.next
        
        sum_ = num1 + num2
        curr = head = ListNode(0)
        
        if sum_ == 0:
            return head
    
        while sum_ > 0:
            head.next = ListNode(sum_ % 10, head.next)
            sum_ //=10
            
        return curr.next    