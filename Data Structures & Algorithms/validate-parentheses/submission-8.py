class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oTc = {'[': ']', '(': ')', '{': '}'}

        for c in s:
            # if c is open bracket -append
            if c in oTc:
                stack.append(c)
            # else (c is close bracket) - check if matches top
            else:
                # check if c matches stack top
                if len(stack) and oTc[stack[len(stack)-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
