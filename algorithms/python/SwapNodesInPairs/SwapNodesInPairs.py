# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        if len(lst) > 1:
            for i in range(0, len(lst) - 1, 2):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

        lst = lst[::-1]
        head = None
        while len(lst) > 0:
            node = ListNode(lst[0], head)
            head = node
            lst.pop(0)

        return head
