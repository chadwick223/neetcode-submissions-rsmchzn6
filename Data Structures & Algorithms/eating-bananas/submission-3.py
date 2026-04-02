class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 #minimum eating speed
        r=max(piles) #maximum eating speed
        res=r #in worst case senario , res= r (maximum eating speed)
        
        while l<=r:
            k=(l+r)//2
            hours=0

            for p in piles:
                hours+=math.ceil(p/k) #for making 3.1 ->4

            if hours <=h:

                res=min(res,k)
                r=k-1
            else:
                l=k+1

        return res


