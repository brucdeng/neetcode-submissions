class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, state):
            if index==len(nums):
                res.append(list(state))
                return
            state.append(nums[index])
            backtrack(index+1, state)
            state.pop()
            backtrack(index+1, state)

        backtrack(0, [])
        return res