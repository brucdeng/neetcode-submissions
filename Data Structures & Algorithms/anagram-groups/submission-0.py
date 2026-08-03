class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newStrs = []
        for x in strs:
            newX = list(x)
            newX.sort()
            newStrs.append("".join(newX))
        map = {}
        for i, x in enumerate(newStrs):
            if x in map:
                map[x].append(strs[i])
            else:
                map[x] = [strs[i]]
        return [map[k] for k in map]