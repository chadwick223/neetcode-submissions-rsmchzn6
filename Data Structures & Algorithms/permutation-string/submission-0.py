class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1count,s2count=[0]*26,[0]*26

        for i in range (len(s1)):
            s1count[ord(s1[i])-ord('a')] +=1
            s2count[ord(s2[i])-ord('a')] +=1

        
        matches=0

        for i in range (26):

            matches +=(1 if s1count[i]==s2count[i] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True
            #right part of the window
            index=(ord(s2[r]) - ord('a')) # tells me which letter  i'm dealing with (a-z)

            s2count[index] +=1
            if s1count[index]==s2count[index]:
                matches+=1
            elif s1count[index] +1 ==s2count[index]:
                matches -=1
            #left part of the window
            index= ord(s2[l]) - ord('a') # index jaha pe l tha (example 1)
            s2count[index] -=1 #array mese uske count ko 1 se ghata diey
            if s1count[index]==s2count[index]:
                matches +=1
            elif s1count[index]-1==s2count[index]: # That means before removing, counts were equal, but now we removed one, so they don't match anymore, so we lose a match.
                matches -=1


            l +=1
        return matches ==26







        






