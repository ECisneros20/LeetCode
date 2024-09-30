from typing import List, Optional

a = [2, 7, 11, 15]
b = 9


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getNumber(self, ln: ListNode) -> int:
        dec = 1
        num = 0
        while ln.next is not None:
            num += ln.val * dec
            dec *= 10
            ln = ln.next
        num += ln.val * dec
        return num

    def getList(self, num: int) -> List[int]:
        lst = []
        while num != 0:
            num, b = divmod(num, 10)
            lst.append(b)
        lst.reverse()
        return lst

    def getListNode(self, lst: List[int]) -> ListNode:
        l1 = ListNode()
        l2 = ListNode()
        if len(lst) == 1:
            l1 = ListNode(lst[0])
            return l1
        else:
            for pos, i in enumerate(lst):
                if pos == 0:
                    l1 = ListNode(i)
                else:
                    l2 = ListNode(i, l1)
                    l1 = l2
            return l2

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = self.getNumber(l1)
        num2 = self.getNumber(l2)
        lst = self.getList(num1 + num2)
        return self.getListNode(lst)


if __name__ == "__main__":
    obj = Solution()
    print(obj.addTwoNumbers(a, b))
