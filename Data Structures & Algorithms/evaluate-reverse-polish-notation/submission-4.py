class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expression = {
            "+",
            "-",
            "*",
            "/",
        }


        for char in tokens:

            # push numbers
            if char not in expression:
                stack.append(char)

            # compute arithmetic 
            if char in expression and len(stack) > 1:

                if char == "+":
                    temp = int(stack.pop()) + int(stack.pop())
                elif char == "-":
                    # swap ordering of values
                    digit1 = stack.pop()
                    digit2 = stack.pop()
                    temp = int(digit2) - int(digit1)
                elif char == "*":
                    temp = int(stack.pop()) * int(stack.pop())
                elif char == "/":
                    # swap ordering of values
                    digit1 = stack.pop()
                    digit2 = stack.pop()
                    temp = int(digit2) / int(digit1)
                
                stack.append(temp)

        return int(stack[0])