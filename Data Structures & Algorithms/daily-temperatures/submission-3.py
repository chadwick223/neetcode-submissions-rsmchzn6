class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res=[0]*len(temperatures)
        stack=[] #pair:[temp,index]
        for i, t in enumerate(temperatures): # enumrate ke kaam hi yahi hota hai ki vo hume counter anad uske saath jo value hai vo bhi dede
            while stack and t > stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]=(i-stackInd)
            stack.append([t,i])
        return res







          