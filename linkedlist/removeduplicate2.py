# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        p1 = answer
        p2 = head
        answer.next = head
        while(p1.next):
            count = 0
            while(p2 != None and p1.next.val == p2.val):
                p2 = p2.next
                count +=1
            if(count > 1): p1.next = p2
            elif(count == 1): p1 = p1.next
        return answer.next
            