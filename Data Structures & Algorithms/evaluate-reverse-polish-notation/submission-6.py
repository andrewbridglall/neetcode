class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # init vars
        stack = []
        operators = {'+', '-', '*', '/'}
        # add operands to stack (convert to ints)
        # at operators, conduct operation and push res to stack
        for token in tokens:
            # check for operators first
            if token in operators:
                op1, op2 = stack.pop(), stack.pop()    
                if token == '+':
                    stack.append(op2 + op1)
                elif token == '-':
                    stack.append(op2 - op1)
                elif token == '*':
                    stack.append(op2 * op1)
                elif token == '/':
                    stack.append(int(op2 / op1))
            # if not operator, must be operand
            else:
                stack.append(int(token))
            print(stack)
        # at end of tokens return stack top
        return stack.pop()