from collections import deque


class RecentCounter:

    def __init__(self):
        self.deque = deque()

    def ping(self, t: int) -> int:
        while self.deque and (t - 3000) > self.deque[0]:
            self.deque.popleft()

        self.deque.append(t)
        return len(self.deque)
