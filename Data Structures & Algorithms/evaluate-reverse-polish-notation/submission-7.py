class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {"+","-","*","/"}
        for i in tokens:        
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second/ first))
            else:
                stack.append(int(i))
        return stack[0]