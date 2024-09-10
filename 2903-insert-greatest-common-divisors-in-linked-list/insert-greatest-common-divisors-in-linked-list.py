# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return abs(a)
        res=head
        while head and head.next:
            tmp=ListNode(gcd(head.val,head.next.val),head.next)
            head.next=tmp
            head=tmp.next
        return res