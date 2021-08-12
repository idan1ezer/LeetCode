# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = temp = ListNode(0)
    while l1 != None and l2 != None:

        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    temp.next = l1 or l2
    return dummy.next

print(mergeTwoLists(l1 = [1,2,4], l2 = [1,3,4]))
print(mergeTwoLists(l1 = [], l2 = []))
print(mergeTwoLists(l1 = [], l2 = [0]))