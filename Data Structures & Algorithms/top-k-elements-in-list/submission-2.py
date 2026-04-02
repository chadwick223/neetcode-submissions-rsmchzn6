class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        #in index we will map count and in values we will store the list of values that occur that(count) many times

        freq=[[]for i in range(len(nums)+1)]
        # its for i in range(len(nums)+1)] because eg [1,2,3] we are making our index count
        # so if num+1 is not here count wil stop at 2, but we know we could be asked 3 most freq elements
        # so in that case 3 will not be there. so it will cause problem 

        for n in nums:
            count[n]=1+count.get(n,0)

        for n,c in count.items(): #n-> key,c->value
            freq[c].append(n)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

