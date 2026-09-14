class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # NLogN time complexity: logN Binary Search + N - days calculation
        # Minimum Capacity: weight of bulkiest package
        # Maximum Capacity: Sum of all weights (Given all need to be transported in one day)

        min_cap = max(weights)
        max_cap = sum(weights)

        while(max_cap>=min_cap):

            mid_cap = (max_cap+min_cap)//2  

            # Calculation of time for each kind of vessel
            counter=0
            time=0
            for weight in weights:
                counter+=weight
                if counter==mid_cap:
                    time+=1
                    counter=0
                elif counter>mid_cap:
                    time+=1
                    counter=weight
                
            if counter!=0:
                time+=1

            # Comparison and updation
            if time<=days:
                max_cap = mid_cap-1
            else:
                min_cap = mid_cap+1
        return min_cap