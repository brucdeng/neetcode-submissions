class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        dic = {}
        dic[2] = "abc"
        dic[3] = "def"
        dic[4] = "ghi"
        dic[5] = "jkl"
        dic[6] = "mno"
        dic[7] = "pqrs"
        dic[8] = "tuv"
        dic[9] = "wxyz"
        result = []
        def backtrack(ind, combo):
            nonlocal result
            nonlocal dic
            if ind >= len(digits):
                result.append(combo)
                return
            letters = dic[int(digits[ind])]
            for letter in letters:
                backtrack(ind+1, combo+letter)
        backtrack(0, "")
        return result