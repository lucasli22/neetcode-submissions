class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack.append(int(tokens[0]))

        for i in range(1, len(tokens)):
            print(stack, tokens[i])
            if tokens[i] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif tokens[i] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif tokens[i] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif tokens[i] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(tokens[i]))

        return stack[-1]

