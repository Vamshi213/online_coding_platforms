# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = ListNode();
        head = a;
        carry=0;
        while l1 or l2 or carry:
            sumd = carry;
            if l1: sumd+=l1.val;
            if l2: sumd+= l2.val;
            carry= int(sumd/10);
            temp=sumd%10;
            head.next= ListNode(temp);
            if l1: l1=l1.next;
            if l2: l2=l2.next;
            head=head.next;
        return a.next;
