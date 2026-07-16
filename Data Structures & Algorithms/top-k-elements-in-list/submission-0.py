class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Dictionary of frequenties: algorithm of complexity n
        dictionary = {}
        for elements in nums:
            if dictionary.get(elements)==None:
                dictionary[elements]=1
            else: 
                dictionary[elements]+=1
        
        # Finding the k top frequencies using the bucket method
        bucket=[[] for i in range(len(nums)+1)]
        for num, freq in dictionary.items():
            bucket[freq].append(num)

        topk=[]
        for lists in range(len(bucket)-1,0,-1):
            for num in bucket[lists]:
                topk.append(num)
                if len(topk)==k:
                    return topk




        