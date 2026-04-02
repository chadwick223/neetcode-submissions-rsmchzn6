class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack=[]
        operators=['+','-','*','/']
        for i in tokens:
            if i not in operators:
                self.stack.append(int(i))
            else:
                b=self.stack.pop()
                a=self.stack.pop()
                if i == "+":
                    self.stack.append(a+b)
                elif i=="-":
                    self.stack.append(a-b)
                elif i=="*":
                    self.stack.append(a*b)
                elif i =="/":
                    self.stack.append(int(a/b))
        return self.stack[0]

        



        