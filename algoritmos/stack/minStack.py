class MinStack:

    def __init__(self):
        self.valueStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.valueStack.append(val)
        if not self.minStack or self.minStack[-1] >=  val :
            self.minStack.append(val)

    def pop(self) -> None:
        if self.valueStack: 
            value = self.valueStack.pop()
            if value == self.minStack[-1]:
                self.minStack.pop()

    def top(self) -> int:
        if self.valueStack: 
            return self.valueStack[-1]
        return None


    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
