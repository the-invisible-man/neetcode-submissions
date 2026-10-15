class MinStack:

    def __init__(self):
        self.stack = []
        self.tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.tracker:
            self.tracker.append(min(self.tracker[-1], val))
        else:
            self.tracker.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tracker[-1]
