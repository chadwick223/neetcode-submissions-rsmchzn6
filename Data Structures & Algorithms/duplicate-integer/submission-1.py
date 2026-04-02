class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (len(nums)-1):
            for j in range(len(nums)-1-i):
                if (nums[j]>nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                return True
        return False
            
        