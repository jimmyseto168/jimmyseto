#1290. Convert Binary Number in a Linked List to Integer
#linked list 的節點為每一個二進位的數字
#EX:head = [1,1,1]= 2^2+2^1+1 = 7

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        a = 0
        while head: 
            answer = 2*a + head.val 
            head = head.next 
        return a
