class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        val = len(nums)//3
        count = 0
        ans = set()
        for i in range(len(nums)):
            if i==0:
                count+=1
            else:
                if nums[i]==nums[i-1]:
                    count+=1
                else:
                    count = 1
            if count > val:
                ans.add(nums[i])
        return list(ans)

