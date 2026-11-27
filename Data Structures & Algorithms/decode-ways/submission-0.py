class Solution:
    def numDecodings(self, s: str) -> int:
        # ord('A') = 65
        # 123: 1, 1 2, 12, 1 2 3, 1 23, 12 3
        memo = {}
        def dfs(ind):
            if ind == len(s):
                return 1
            if s[ind]=='0':
                return 0
            if ind in memo:
                return memo[ind]
            res = dfs(ind+1)
            if ind + 1 < len(s) and 10 <= int(s[ind:ind+2]) <= 26:
                res += dfs(ind+2)
            memo[ind] = res
            return res
        return dfs(0)