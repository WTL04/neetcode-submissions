class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate both lists
        # compute the sum of both values
        # create a new linked list 
        # append that value to the new linked list
        # return the new linked list
        # r: O(N), s: O(1)

        curr1 = l1
        curr2 = l2

        head = ListNode()
        curr3 = head
        carry = 0

        while curr1 or curr2 or carry:
            # compute value
            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0
            total = v1 + v2 + carry
            carry = total // 10

            # create new node
            curr3.next = ListNode(total % 10)

            # iterate new list
            curr3 = curr3.next

            # iterate lists
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

        return head.next