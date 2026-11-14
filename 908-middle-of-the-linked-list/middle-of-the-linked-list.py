# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        temp=head
        count=0
        while temp:
            temp=temp.next
            count+=1
        mid=count//2
        temp=head
        for i in range(mid):
            temp=temp.next
        return temp

        