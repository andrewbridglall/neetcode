class MinStack:

    def __init__(self):
        self.stack = []
        self.sorted_arr = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.sorted_arr.append(val)
        self.sorted_arr.sort()

    def pop(self) -> None:
        val = self.stack.pop()
        self.sorted_arr.remove(val)
        self.sorted_arr.sort()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted_arr[0]
