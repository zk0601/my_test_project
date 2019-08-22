
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if not head:
            return None
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        val_list = sorted(val_list)
        head = ListNode(val_list[0])
        curr = head
        for i in val_list[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return head

    def sortList2(self, head):
        if not head or not head.next: return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList2(head), self.sortList2(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

    def maxArea(self, height):
        start, end = 0, len(height) - 1
        res = 0
        while start < end:
            res = max(min(height[start], height[end]) * (end-start), res)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res

    def isPalindrome(self, x):
        return True if str(x) == ''.join(list(reversed(str(x)))) else False


if __name__ == '__main__':
    a = [1,8,6,2,5,4,8,3,7]
    aa = Solution()
    print(aa.isPalindrome(121))
