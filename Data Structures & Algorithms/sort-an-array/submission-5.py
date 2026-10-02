class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # # Bubble Sort - check sorted or not, keep swapping the elements again and again once all are sortec!
        # condition = True
        # while(condition):
        #     condition = False
        #     for i in range(len(nums) - 1):
        #         if nums[i] > nums[i + 1]:
        #             condition = True
        #             temp = nums[i]
        #             nums[i] = nums[i + 1]
        #             nums[i + 1] = temp

        # return nums

        # # Insertion Sort - take the element and keep it in its position, ie sort sublists

        # for i in range(1, len(nums)):
        #     key = nums[i]
        #     j = i - 1
        #     while(j >= 0 and nums[j] > key):
        #         nums[j + 1] = nums[j]
        #         j -= 1
        #     nums[j + 1] = key


        # return nums

        # # Selection sort - find the minimum and replace it with the current pointer
        # i = 0
        # for i in range(len(nums)):
        #     minimum = nums[i]
        #     index = i
        #     # Find minimum element
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < minimum:
        #             index = j
        #             minimum = nums[j]
        #     # Updation
        #     nums[index] = nums[i]
        #     nums[i] = minimum
        # return nums

        # Merge Sort

        def Merge(l , mid, r):
            a = []
            b = []

            for i in range(l, mid + 1):
                a.append(nums[i])

            for i in range(mid + 1, r + 1):
                b.append(nums[i])

            i, j = 0, 0
            while(l <= r):
                if i == len(a):
                    nums[l] = b[j]
                    j += 1
                elif j == len(b):
                    nums[l] = a[i]
                    i += 1

                elif a[i] < b[j]:
                    nums[l] = a[i]
                    i += 1
                else:
                    nums[l] = b[j]
                    j += 1
                
                l += 1

        def MergeSort(l, r):
            # Base Case
            if l >= r:
                return 

            mid = (l + r)//2

            MergeSort(l, mid)
            MergeSort(mid + 1, r)

            Merge(l, mid, r)

        MergeSort(0, len(nums) - 1)
        return nums

