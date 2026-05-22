class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:


            # compute arithmetic 
            if char == "+":
                temp = int(stack.pop()) + int(stack.pop())
                stack.append(temp)
            elif char == "-":
                # swap ordering of values
                a, b = stack.pop(), stack.pop()
                temp = int(b) - int(a)
                stack.append(temp)
            elif char == "*":
                temp = int(stack.pop()) * int(stack.pop())
                stack.append(temp)
            elif char == "/":
                # swap ordering of values
                a, b = stack.pop(), stack.pop()
                temp = int(b) / int(a)
                stack.append(temp)
            else:
                # push numbers
                stack.append(char)
            

        return int(stack[0])