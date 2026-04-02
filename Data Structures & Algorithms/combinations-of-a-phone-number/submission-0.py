class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        #also digits seems liked are mapped with hashmaps
        #how should we access those charecters?
        #we need to hard code our hashmap since hume hashmap diya nhi gya hai
        digitToChar={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }


        def backtracking(i,word):
            if len (word)==len(digits):
                res.append(word)
                return

            for c in digitToChar[digits[i]]:
                backtracking(i+1,word+c)
                #lets say i got access to set of charecters

        if digits:
            backtracking(0,"")

        return res

         

        