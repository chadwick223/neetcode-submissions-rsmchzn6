class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}

        freq=[[]for n in range (len(nums)+1)]
        #it creates someting like this [[],[],[],[]]

        for n in nums:
            count[n]=1+count.get(n,0)

        for n,c in count.items():
            #n-key,c-value/count ki frequency of a number 

            freq[c].append(n)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if (len(res))==k:
                    return res


