from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # push to q2
        self.q2.append(x)
        # if any elts in q1 popleft and append to q2
        for _ in range(len(self.q1)):
            self.q2.append(self.q1.popleft())
        # swap q1,q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # popleft q1
        return self.q1.popleft()

    def top(self) -> int:
        # q1 at 0
        return self.q1[0]

    def empty(self) -> bool:
        # len of q1
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()