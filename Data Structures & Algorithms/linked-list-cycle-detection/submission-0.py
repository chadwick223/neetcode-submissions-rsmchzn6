# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head, head
        while fast and fast.next: #why fast.next is cause we are checking for the case in which we have only one element
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                return True

        return False
        