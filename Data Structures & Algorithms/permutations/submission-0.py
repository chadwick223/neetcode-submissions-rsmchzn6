class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        permutation=[]

        def dfs():
            if len(permutation)==len(nums):
                res.append(permutation.copy())
                return

            #for decisions 
            for i in range (len(nums)):
                if nums[i]  not in permutation:
                    permutation.append(nums[i])
                    dfs()

                    permutation.pop()

        dfs()
        return res

                
        
        