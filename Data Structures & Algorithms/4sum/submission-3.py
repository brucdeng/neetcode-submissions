class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <=3:
            return []
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a==nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j]==nums[j-1]:
                    continue
                k = j+1
                l = len(nums)-1
                val = target - nums[i]- nums[j]
                while (k < l):
                    c = nums[k] + nums[l]
                    if c==val:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k+=1
                        l-=1
                        while (nums[k]==nums[k-1] and k < l):
                            k+=1
                    elif c > val:
                        l -= 1
                    else:
                        k+=1
        return res