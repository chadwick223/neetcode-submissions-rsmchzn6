class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsum=nums[0]
        currsum=0

        for n in nums :
            currsum=max(currsum,0)
            currsum =currsum+n
            maxsum=max(maxsum,currsum)

        return maxsum

        
        