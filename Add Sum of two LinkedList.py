# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        previous = result = ListNode(None)
        remainder = 0

        while l1 or l2 or remainder:
            if l1:
                remainder += l1.val
                l1 = l1.next
            if l2:
                remainder += l2.val
                l2 = l2.next
            previous.next = ListNode(remainder % 10)
            previous = previous.next
            remainder //= 10

        return result.next
