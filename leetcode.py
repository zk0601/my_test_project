class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret = dict()
        for word in strs:
            in_ret = False
            if ''.join(sorted(list(word))) in ret:
                ret[''.join(sorted(list(word)))].append(word)
                in_ret = True
            if not in_ret:
                ret.setdefault(''.join(sorted(list(word))), [word])
        return ret


if __name__ == '__main__':
    a = Solution()
    a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
