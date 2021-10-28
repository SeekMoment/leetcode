# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for i in lists:
            while i:
                lst.append(i.val)
                i = i.next
        lst.sort(reverse=True)
        lists = None
        while len(lst) > 0:
            node = ListNode(lst[0], lists)
            lists = node
            lst.pop(0)
        return lists
