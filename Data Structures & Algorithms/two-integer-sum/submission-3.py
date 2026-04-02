class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #for loop {toh kha se kha tak?}
        #how will you define range? kyoki we want num[0] fix rahe,and vo num[i] se add ho
        # till range,

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

        return []

        