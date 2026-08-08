class MinStack:

    def __init__(self):
        self.min_stack = []
        self.stack_array = []
        self.length = 0

    def push(self, val: int) -> None:
        self.stack_array.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        self.length += 1

    def pop(self) -> None:
        val = self.stack_array.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        self.length -= 1
        if self.length == 0: 
            return []
        return self.stack_array[self.length - 1]

    def top(self) -> int:
        return self.stack_array[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]