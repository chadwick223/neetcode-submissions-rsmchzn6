class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closedtoopen={")":"(","}":"{","]":"["}
        for c in s:
            if c in closedtoopen:
                if stack and stack[-1]==closedtoopen[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        if len(stack)==0:
            return True
        else:
            return False
        