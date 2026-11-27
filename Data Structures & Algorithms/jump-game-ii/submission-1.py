class Solution:
    def jump(self, nums: List[int]) -> int:
        ind = 0
        count = 0
        while ind < len(nums)-1:
            if ind + nums[ind] >= len(nums)-1:
                count+=1
                break
            nextInd = ind+1
            maxSeen = nextInd + nums[nextInd]
            for i in range (nextInd, nextInd + nums[ind]):
                if i+nums[i] >=maxSeen:
                    nextInd = i
                    maxSeen = i+nums[i]
            ind = nextInd
            count+=1
        return count