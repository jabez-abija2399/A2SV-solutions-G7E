# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        tail = head
        leng = 1
        while tail.next:
            tail = tail.next
            leng += 1
        
        tail.next = head
        k = k % leng 
        stepTail = leng - k - 1
        newTail = head
        for _ in range(stepTail):
            newTail = newTail.next
        newHead = newTail.next
        newTail.next = None

        return newHead
