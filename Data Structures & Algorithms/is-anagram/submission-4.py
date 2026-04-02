class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            new_2={}
            new={}
            for i in range(len(s)):
                new[s[i]] = 1+new.get(s[i],0)
                new_2[t[i]]=1+new_2.get(t[i],0)

            for c in new:
                if new[c]!=new_2.get(c,0):

                    return False

            return True

        