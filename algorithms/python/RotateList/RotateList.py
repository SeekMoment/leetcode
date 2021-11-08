# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        itr = head
        n = 1
        if head is None:
            return None

        while itr.next:
            itr = itr.next
            n += 1

        k = k % n
        if k == 0:
            return head

        pos = n - k
        curr = head
        prev = None

        while pos > 0:
            prev = curr
            curr = curr.next
            pos -= 1

        temp = curr
        prev.next = None
        itr.next = head

        return curr
