# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        result = [None] * k  # Initialize the result list with None values
        
        # Step 1: Calculate the total length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Determine the base size and the remainder
        size = length // k  # Base size of each part
        extra = length % k  # Number of parts that will have one extra element
        
        current = head
        for i in range(k):
            if not current:
                result[i] = None  # If the list is smaller than k, add None for empty parts
            else:
                result[i] = current  # Start a new part
                part_size = size + (1 if extra > 0 else 0)  # Determine the size of this part
                extra -= 1
                
                # Move to the end of this part
                for j in range(1, part_size):
                    if current:
                        current = current.next
                
                # Break the current part from the rest of the list
                if current:
                    next_part = current.next
                    current.next = None
                    current = next_part
        
        return result