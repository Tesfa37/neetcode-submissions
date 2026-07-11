class Solution:
    def isValid(self, s: str) -> bool:
        """ Given input: s = [(){}[]]
            return true or false
            Since we are asked to keep track of the order
            Will use stack to solve it.
            Last in Last out.
        """
        stack = []
        closing = {")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in closing:
                if stack and stack[-1] == closing[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
