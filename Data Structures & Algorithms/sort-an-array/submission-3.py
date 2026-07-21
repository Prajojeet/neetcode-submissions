class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # We will use merge sort that is a recursive algorithm in this go!
        l=0
        r=len(nums)-1
        # There are two operations dividing the array and a unique way of 
        # merging things so that individual lists are sorted
        def mergesort(l, r):
            if l>=r:
                return

            mid=(l+r)//2
            mergesort(l, mid)
            mergesort(mid+1, r)

            merge(l,mid,r)

        def merge(l, mid, r):
            a=[]
            b=[]

            for i in range(l,mid+1):
                a.append(nums[i])

            for i in range(mid+1,r+1):
                b.append(nums[i])
                
            i,j=0,0

            for k in range(l,r+1):
                if i==len(a):
                    nums[k]=b[j]
                    j+=1
                    k+=1
                elif j==len(b):
                    nums[k]=a[i]
                    i+=1
                    k+=1
                elif a[i]>=b[j]:
                    nums[k]=b[j]
                    j+=1
                    k+=1
                else:
                    nums[k]=a[i]
                    i+=1
                    k+=1
        mergesort(l,r)
        return nums