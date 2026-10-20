class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal=len(nums) -1

        for i in range(len(nums)-1,-1,-1):
            if i+nums[i]>=goal: # i+ nums[i] is actualaly the furtest index i can reach
                goal =i 
        return True if goal == 0 else False