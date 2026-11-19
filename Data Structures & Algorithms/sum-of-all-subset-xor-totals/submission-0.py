class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def backtrack(cur, arr, ind):
            nonlocal total
            if (ind >= len(nums)):
                return
            arr.append(nums[ind])
            total += cur ^ nums[ind]
            backtrack(cur ^ nums[ind], arr, ind+1)
            arr.pop()
            backtrack(cur, arr, ind+1)
        backtrack(0, [], 0)
        return total