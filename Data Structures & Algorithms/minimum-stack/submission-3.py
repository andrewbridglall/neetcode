import sys

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if not self.stack:
            self.min = sys.maxsize #reset
        elif self.stack and val == self.min:
            #recalc min
            self.min = self.stack[0]
            for num in self.stack:
                if num < self.min:
                    self.min = num

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min