class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count={}
        s2count={}

        for c in s1:
            s1count[c]=1+s1count.get(c,0)
        for i in range(len(s2)):
            need=len(s1count)
            cur=0
            s2count={}
            for j in range (i,len(s2)):
                s2count[s2[j]] = 1+s2count.get(s2[j],0)
                if s1count.get(s2[j],0) < s2count[s2[j]]:
                    break
                if s1count.get(s2[j],0)==s2count[s2[j]]:
                    cur+=1
                if cur == need:
                    return True
        return False
                
            

                




        






        






