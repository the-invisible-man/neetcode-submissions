# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slowPointer = head
        fastPointer = head.next

        while fastPointer:
            if fastPointer == slowPointer:
                return True

            slowPointer = slowPointer.next

            if fastPointer.next:
                fastPointer = fastPointer.next.next
            else:
                fastPointer = fastPointer.next

        return False