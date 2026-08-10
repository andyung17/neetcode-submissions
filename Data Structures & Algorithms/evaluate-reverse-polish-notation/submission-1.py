class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operand_first = 0
        operand_second = 0

        for token in tokens:
            if token in '+-/*':
                operand_first = int(stack.pop())
                operand_second = int(stack.pop())
                if token == "+":
                    stack.append(operand_second + operand_first)
                elif token == "-":
                    stack.append(operand_second - operand_first)
                elif token == "/":
                    stack.append(int(operand_second / operand_first))
                elif token == "*":
                    stack.append(operand_second * operand_first)
            else:
                stack.append(int(token))

        return stack[-1]
