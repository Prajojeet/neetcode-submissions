class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Concept of relative speed for each car 
        # time taken to reach target of second car >=
        # time taken to cover the difference, then fleet otherwise not
        # make a dictionary of position and the speed as value; sort the dictionary
        hashmap={}
        for index in range(len(position)):
            hashmap[position[index]]=speed[index]
        sorted_hashmap = dict(sorted(hashmap.items(), reverse=True))
        print(sorted_hashmap)

        time=0
        fleet=0
        for key in sorted_hashmap:
            if time<(target-key)/hashmap[key]:
                fleet+=1
                time=(target-key)/hashmap[key]
        return fleet