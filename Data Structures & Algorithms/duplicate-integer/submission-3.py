class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:

        dup={}

        for i in range(len(nums)):

            if nums[i] not in dup:
                dup[nums[i]]=1+dup.get(0,nums[i])
            else:
                return True

        return False


