class MinStack:

    def __init__(self):
        self.stack = []
        self.tracker = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.tracker) > 0:
            if self.tracker[-1] > val:
                self.tracker.append(val)
            else:
                self.tracker.append(self.tracker[-1])
        else:
            self.tracker.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.tracker.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.tracker[-1]
