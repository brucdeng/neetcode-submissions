class TimeMap:

    def __init__(self):
        self.tm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.tm.keys():
            self.tm[key].append((value, timestamp))
        else:
            self.tm[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tm.keys():
            return ""
        ans = ""
        l, r = 0, len(self.tm[key])-1
        while (l <= r):
            mid = l + (r-l)//2
            if self.tm[key][mid][1] <= timestamp:
                t = self.tm[key][mid][1]
                ans = self.tm[key][mid][0]
            if timestamp > self.tm[key][mid][1]:
                l = mid+1
            elif timestamp < self.tm[key][mid][1]:
                r = mid-1
            else:
                break
        return ans
