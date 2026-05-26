# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxSum = 0
        slow, fast = head, head

        # loop until middle of list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow

        # reverse second half of the list
        current = mid
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next 

        tail = prev 

        # iterate both first and second halved lists 
        first, second = head, tail
        while first and second:
            total = first.val + second.val
            first = first.next
            second = second.next

            maxSum = max(total, maxSum)

        return maxSum






