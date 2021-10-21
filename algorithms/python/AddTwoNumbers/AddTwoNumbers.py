# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list_l1 = []
        list_l2 = []
        list_l1_int = ''
        list_l2_int = ''
        while l1:
            list_l1.append(l1.val)
            l1 = l1.next
        while l2:
            list_l2.append(l2.val)
            l2 = l2.next

        for i in list_l1[::-1]:
            list_l1_int += str(i)
        for i in list_l2[::-1]:
            list_l2_int += str(i)

        list_sum = int(list_l1_int) + int(list_l2_int)
        s = t = ListNode()

        for x in str(list_sum)[::-1]:
            s.next = ListNode(x)
            s = s.next

        return t.next