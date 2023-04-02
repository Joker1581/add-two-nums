from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        pointer = result
        while l1 or l2 or carry:
            print(l1)
            firstNum = l1.val if l1 else 0
            secondNum = l2.val if l2 else 0
            print(firstNum)
            sum = firstNum + secondNum + carry
            num = sum % 10
            carry = sum // 10
            print(pointer)
            pointer.next = ListNode(num)
            pointer = pointer.next
            print(pointer)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next

# if __name__ == "__main__":
#     a1 = ListNode(2, ListNode(4, ListNode(3)))
#     a2 = ListNode(5, ListNode(6, ListNode(4)))
#     print(Solution.addTwoNumbers(Solution, a1, a2))            