class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two={}

        for i,n in  enumerate(nums):
            diff=target-n
            if diff in two :
                return [two[diff],i]
            two[n]=i

        return
        