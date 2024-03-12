# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d=ListNode(0)
        d.next=head
        presum=0
        dic={0:d}
        cur=head
        while cur:
            presum+=cur.val
            if presum in dic:
                dlt=dic[presum].next
                tmp=presum+dlt.val
                while dlt != cur:
                    del dic[tmp]
                    dlt=dlt.next
                    tmp+=dlt.val
                dic[presum].next=cur.next
            else:
                dic[presum]=cur
            cur=cur.next
        return d.next

        