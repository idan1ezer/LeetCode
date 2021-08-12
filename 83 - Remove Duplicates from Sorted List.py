# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(self, head):
    while(head.next != None):
        if (head.val == head.next.val):
            head.next = head.next.next

    return head
