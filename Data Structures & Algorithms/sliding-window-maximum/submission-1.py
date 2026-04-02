class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        l,r=0,0
        q=collections.deque()
        while r <len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) #we're appending the index
             #we are keeping the biggest  number at the front of qeue
            if l > q[0]:
                # is the index of l is greater than q[0]. since q[0] would be the greatest and at the leftest side of qeue you'll have to remove it since window is now silded
                q.popleft()

            if (r+1) >=k:
                output.append(nums[q[0]])
                l+=1
            r +=1
        return output

            

        