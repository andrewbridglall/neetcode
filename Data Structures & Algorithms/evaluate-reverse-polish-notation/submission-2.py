class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack soln
        # init vars
        n = len(tokens)
        stack = []
        # iterate thru tokens
        for token in tokens:
        # if token is operator - compute and add to stack
            if token in {"+", "-", "*", "/"}:
                operand2 = stack.pop()
                operand1 = stack.pop()
                res = 0
                if token == '+':
                    res = operand1 + operand2
                elif token == '-':
                    res = operand1 - operand2
                elif token == '*':
                    res = operand1 * operand2
                else:
                    res = abs(operand1) // abs(operand2)
                    if operand1*operand2 < 0:
                        res *= -1
                stack.append(res)
        # if token is num add to stack
            else:
                stack.append(int(token))
            # print(stack)
        # return pop from stack
        return stack.pop()
