# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        base = n // k
        extra = n % k
        res = [None] * k
        cur = head
        for i in range(k):
            res[i] = cur
            size = base + (1 if i < extra else 0)
            for j in range(size-1):
                if cur:
                    cur = cur.next
            if cur:
                nxt = cur.next
                cur.next = None
                cur = nxt
        return res
        