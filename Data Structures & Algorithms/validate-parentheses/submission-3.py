class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        
        #create match func
        def match(front: str, back: str) -> bool:
            if front == '[' and back == ']':
                return True
            elif front == '{' and back == '}':
                return True
            elif front == '(' and back == ')':
                return True
            else:
                return False
        
        stack = []
        for char in s:
            # if char in set of opening braces - append to stack
            if char in ('(', '{', '['):
                stack.append(char)
            # else, char must be closing brace - check if match top of stack
            else:
                #check if match
                if len(stack) >0 and match(stack[-1], char):
                    stack = stack[:-1] # pop char from stack
                else:
                    return False
        
        return True if len(stack) == 0 else False


        


        