class TimeMap:
    # store tuples in a dictionary that gets updated with timestamp! compare and give the answer accordingly

    def __init__(self):
        self.hashmap={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key]=[(value,timestamp)]
        else:
            self.hashmap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""

        # Do binary search here to find the upper bound (so that I can say if upper bound is zero, then return "")
        l=0
        r=len(self.hashmap[key])-1
        while(l<r):
            mid=(l+r)//2

            if self.hashmap[key][mid][1]<timestamp:
                l=mid+1
            else:
                r=mid
        
        if r==0 and self.hashmap[key][r][1]>timestamp:
            return ""
        elif self.hashmap[key][r][1]<=timestamp:
            return self.hashmap[key][r][0]
        else:
            return self.hashmap[key][r-1][0]