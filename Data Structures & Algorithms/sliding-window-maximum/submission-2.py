class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=collections.deque()
        l=0
        r=0
        while r < len(nums):

            while q and q[-1][0]<nums[r]:
                q.pop()

            #before appending we need to check if nums[r]>topmost/rightmost
            #value in our qeue
            q.append((nums[r],r))
            #q[o][0] -> value
            #q[0][1] > index

            # also if left is out of bound then we need to remove it

            if l > q[0][1]:
                q.popleft()
            if (r+1)>=k:
                output.append(q[0][0])
                l+=1
            r+=1
        return output
            



        