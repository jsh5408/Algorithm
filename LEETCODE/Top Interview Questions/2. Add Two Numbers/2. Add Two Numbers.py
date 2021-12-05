# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        two = 0
        a = 1
        while l1 and l2:
            if l1.val + l2.val + carry > 9:
                two += ((l1.val + l2.val + carry) % 10) * a
                carry = 1
            else:
                two += (l1.val + l2.val + carry) * a
                carry = 0
            a *= 10
            l1 = l1.next
            l2 = l2.next
        
        l = l1 if l1 else l2
        while l:
            if l.val + carry > 9:
                two += ((l.val + carry) % 10) * a
                carry = 1
            else:
                two += (l.val + carry) * a
                carry = 0
            a *= 10
            l = l.next
        if carry:
            two += 1 * a
        
        two = reversed(list(str(two)))
        two = ''.join(two)
        
        ans = ListNode(0)
        h = ans
        i = 0
        while i < len(two):
            ans.next = ListNode(int(two[i]) % 10)
            i += 1
            ans = ans.next
            
        return h.next