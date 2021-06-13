# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        head1=ListNode()
        p=head1
        head2=ListNode()
        q=head2
        i=0
        while head is not None:
            if i%2==0:
                p.next=head
                head=head.next
                p=p.next
            else:
                q.next=head
                head=head.next
                q=q.next
            i+=1
        if(i%2!=0):
            q.next=None
        p.next=head2.next
        head1=head1.next
        return head1

        