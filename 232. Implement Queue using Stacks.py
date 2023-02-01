class MyQueue:

    def __init__(self):
        self.top = []
        self.bottom = []

    def push(self, x: int) -> None:
        self.bottom.append(x)

    def pop(self) -> int:
        if not self.top:
            while self.bottom:
                self.top.append(self.bottom.pop())
        return self.top.pop()

    def peek(self) -> int:
        if not self.top:
            while self.bottom:
                self.top.append(self.bottom.pop())
        return self.top[-1]

    def empty(self) -> bool:
        return (not self.bottom) and (not self.top)


obj = MyQueue()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
