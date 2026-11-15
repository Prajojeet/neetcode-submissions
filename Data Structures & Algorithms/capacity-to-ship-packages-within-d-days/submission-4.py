class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = sum(weights)
        min_cap = max(weights)
        def day_calc(mid_cap):
            d, curr_cap = 0, 0
            for weight in weights:
                curr_cap += weight
                if curr_cap >= mid_cap:
                    if curr_cap > mid_cap:
                        curr_cap = weight
                    else:
                        curr_cap = 0
                    d += 1

            if curr_cap != 0:
                d += 1
            return d
        res = 0
        while(min_cap <= max_cap):
            mid_cap = (max_cap + min_cap)//2
            d = day_calc(mid_cap)
            if d > days:
                min_cap = mid_cap + 1
            else:
                res = mid_cap
                max_cap = mid_cap - 1
        return res