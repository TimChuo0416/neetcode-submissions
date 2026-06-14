class MinStack:

    def __init__(self):
        self.stack = []
        self.minlist = []
        self.pre = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minlist[-1] if self.minlist else val)
        self.minlist.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minlist.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minlist[-1]
