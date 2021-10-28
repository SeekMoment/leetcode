# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while l1:
            lst.append(l1.val)
            l1 = l1.next

        while l2:
            lst.append(l2.val)
            l2 = l2.next

        lst.sort(reverse=True)
        l1 = None
        while len(lst) > 0:
            node = ListNode(lst[0], l1)
            l1 = node
            lst.pop(0)
        return l1
