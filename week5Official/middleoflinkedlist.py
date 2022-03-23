# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L = 0
        count = 0
        iterDummy = head
        while(iterDummy!=None):
            L+=1
            iterDummy = iterDummy.next
        print (L)
        if(L <1):
            return head 
        while( head !=None and count < L//2):
            count+=1
            head = head.next
        return head
        