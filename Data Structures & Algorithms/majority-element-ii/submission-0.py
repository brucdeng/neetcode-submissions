class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        ans = []
        for item in freq:
            if freq[item] > len(nums)/3:
                ans.append(item)
        return ans