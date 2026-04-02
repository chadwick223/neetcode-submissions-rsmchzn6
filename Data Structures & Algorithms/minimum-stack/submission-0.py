class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def isempty(self) -> bool:
        return len(self.minstack) == 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        if not self.isempty():
            self.stack.pop()
            self.minstack.pop()

    def top(self) -> int:
        if not self.isempty():
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.isempty():
            return self.minstack[-1]
