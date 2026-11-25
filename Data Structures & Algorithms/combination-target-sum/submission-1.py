class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(total, ind, cur):
            if total == target:
                res.append(list(cur))
                return
            if total > target or ind >= len(nums):
                return
            cur.append(nums[ind])
            backtrack(total + nums[ind], ind, cur)
            cur.pop()
            backtrack(total, ind+1, cur)
            return
        backtrack(0, 0, [])
        return res