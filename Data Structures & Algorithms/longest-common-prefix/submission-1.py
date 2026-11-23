class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = ""
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[len(strs)-1][i]:
                ans+=strs[0][i]
            else:
                break
        return ans