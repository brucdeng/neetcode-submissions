class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(total, ind, cur):
            if total == target:
                res.append(list(cur))
                return
            if total > target or ind >= len(candidates):
                return
            cur.append(candidates[ind])
            backtrack(total + candidates[ind], ind+1, cur)
            cur.pop()
            tmp = ind+1
            while tmp < len(candidates) and candidates[tmp]==candidates[ind]:
                tmp+=1
            backtrack(total, tmp, cur)
            return
        backtrack(0, 0, [])
        return res