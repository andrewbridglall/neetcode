class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack soln
        # init vars
        n = len(s)
        left = []
        star = []
        # iter thru string s
        for i in range(n):
        # add left par to left stack
            if s[i] == '(':
                left.append(i)
        # add * to star stack
            elif s[i] == '*':
                star.append(i)
        # if right par pop from left, then try star
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
        # if left empty and star empty ret false
                else:
                    # not left and not star
                    return False
        # pop from left and star if left top < star top
        # if left top > star top ret False - stuck with open left bracket and no closing bracket
        while left and star:
            l, s = left[-1], star[-1]
            if l < s:
                left.pop()
                star.pop()
            else:
                return False
        # return true if left empty
        return not left

        