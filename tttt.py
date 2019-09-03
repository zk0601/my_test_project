
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

    def myAtoi(self, str):
        str = str + 'p'
        _range = [-2 ** 31,  2 ** 31 - 1]
        symbol = ['-', '+']
        result = []
        for i in range(len(str)):
            if i == len(str) - 1:
                break
            if str[i] != ' ' and not str[i].isdigit() and len(result) == 0 and (str[i] not in symbol or not str[i+1].isdigit()):
                print(i)
                break
            if str[i].isdigit() or (str[i] in symbol and str[i+1].isdigit() and len(result) == 0):
                result.append(str[i])
                if not str[i+1].isdigit():
                    break
        if result:
            result = int(''.join(result))
            if result > _range[1]:
                return _range[1]
            elif result < _range[0]:
                return _range[0]
            else:
                return result
        else:
            return 0

    def generateMatrix(self, n):
        l = [0 for _ in range(n)]
        self.map = [l.copy() for _ in range(n)]
        self.value = 1
        self.func(0, n-1)
        return self.map

    def func(self, start, end):
        if start > end:
            return
        if start == end:
            self.map[start][end] = self.value
            return
        for i in range(start, end):
            self.map[start][i] = self.value
            self.value += 1
        for i in range(start, end):
            self.map[i][end] = self.value
            self.value += 1
        for i in range(end, start, -1):
            self.map[end][i] = self.value
            self.value += 1
        for i in range(end, start, -1):
            self.map[i][start] = self.value
            self.value += 1
        self.func(start+1, end-1)

    def longestcommonsubsequence(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[-1][-1]

    def solveNQueens(self, n):
        pass

if __name__ == '__main__':
    a = 'fsda'
    b = 'aacesdfsd'
    aa = Solution()
    print(aa.longestcommonsubsequence(a, b))

