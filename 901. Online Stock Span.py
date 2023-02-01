class StockSpanner:

    def __init__(self):
        self.stack = []
        self.lst = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            self.lst.append(1)
            return 1
        count = 1
        while self.stack and self.stack[-1] <= price:
            count += self.lst.pop()
            self.stack.pop()
        self.stack.append(price)
        self.lst.append(count)
        return count
