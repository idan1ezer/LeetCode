# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head):
    cache = {}

    while (head is not None):
        if (head not in cache):
            cache[head] = True
        else:
            return True
        head = head.next

    return False