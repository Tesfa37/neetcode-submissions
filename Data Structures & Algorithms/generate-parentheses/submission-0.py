class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # close can only be added if we have more open
        # limit is n for both open and close
        res = []
        stack = []
        def backtrack(Open, closed):
            if Open == n and closed == n:
                res.append("".join(stack))
                # res.append(subset.copy())
                return
            if Open < n:
                stack.append("(")
                backtrack(Open + 1, closed)
                stack.pop()
            if closed < Open:
                stack.append(")")
                backtrack(Open, closed + 1)
                stack.pop()
        backtrack(0,0)
        return res