class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(cur, numToAdd):
            if len(cur)==k:
                res.append(list(cur))
                return
            if numToAdd > n:
                return
            cur.append(numToAdd)
            backtrack(cur, numToAdd+1)
            cur.pop()
            backtrack(cur, numToAdd+1)
        backtrack([], 1)
        return res