class MyQueue:
    def __init__(self):
        self.myStack = []

    def push(self, x: int) -> None:
        self.myStack.append(x)

    def pop(self) -> int:
        return self.myStack.pop(0)

    def peek(self) -> int:
        return self.myStack[0]

    def empty(self) -> bool:
        if len(self.myStack) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()