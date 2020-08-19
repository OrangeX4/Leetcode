from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Init
        value = l1.val + l2.val
        if value > 9:
            l3 = ListNode(value % 10)
            l1 = l1.next
            l2 = l2.next
            CF = True
        else:
            l3 = ListNode(value)
            l1 = l1.next
            l2 = l2.next
            CF = False
        Ans = l3
        
        # Main process
        while l1 != None and l2 != None:
            if CF:
                value = l1.val + l2.val + 1
            else:
                value = l1.val + l2.val
            if value > 9:
                l3.next = ListNode(value % 10)
                l1 = l1.next
                l2 = l2.next
                l3 = l3.next
                CF = True
            else:
                l3.next = ListNode(value)
                l1 = l1.next
                l2 = l2.next
                l3 = l3.next
                CF = False
        
        # For None value
        if l1 == None and l2 != None:
            while l2 != None:
                l3.next = l2
                l2 = l2.next
                l3 = l3.next
                if CF:
                    if l3.val + 1 > 9:
                        l3.val = 0
                        CF = True
                    else:
                        l3.val = l3.val + 1
                        CF = False
        if l2 == None and l1 != None:
            while l1 != None:
                l3.next = l1
                l1 = l1.next
                l3 = l3.next
                if CF:
                    if l3.val + 1 > 9:
                        l3.val = 0
                        CF = True
                    else:
                        l3.val = l3.val + 1
                        CF = False
        if l1 == None and l2 == None:
            if CF:
                l3.next = ListNode(1)
                return Ans
            else:
                return Ans

    def ToNumber(self, nums: List) -> ListNode:
        value = ListNode(0)
        ret = value
        for num in nums:
            value.val = num
            value.next = ListNode(0)
            savedValue = value
            value = value.next
        # Make the highest bit None
        savedValue.next = None
        return ret

    # def FromNumber(self, number: ListNode) -> int:
    #     weight = 1
    #     ret = 0
    #     while number != None:
    #         ret = ret + weight * number.val
    #         weight = 10 * weight
    #         number = number.next
    #     return ret

    def FromNumber(self, number: ListNode) -> int:
        ret = []
        while number != None:
            ret.append(number.val)
            number = number.next
        return ret


Ans = Solution()
a = Ans.ToNumber([5])
b = Ans.ToNumber([5,9,1])
print(Ans.FromNumber(Ans.addTwoNumbers(a, b)))