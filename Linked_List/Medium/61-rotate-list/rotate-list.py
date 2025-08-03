# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k % len(head)
        if not head:
            return head
        length = 1
        curr = head
        
        while (curr.next):
            length +=1
            curr = curr.next
        start = k % length
        curr.next = head
        to_cut = length - start
        new_tail = head
        for _ in range(to_cut-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head