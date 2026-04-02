class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new={}
        for i in range (len(nums)):
            new[nums[i]]=1+new.get(nums[i],0)
            if new[nums[i]]>=2:
                return True
        return False
