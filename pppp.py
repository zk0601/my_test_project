class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        queue = []
        for chane in lists:
            curr = chane
            while curr:
                queue.append(curr.val)
                curr = curr.next
        queue.sort()

        if not queue:
            return None
        ret = ListNode(queue[0])
        curr = ret
        for i in queue[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return ret




