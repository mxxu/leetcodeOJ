class MinStack:
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.elements.append(x)
        self.size = self.size + 1

        if len(self.elements) == 1 or self.getMin() > x:
            self.min_eles.append(self.size - 1)

    # @return nothing
    def pop(self):
        if self.min_eles and self.min_eles[-1] == self.size - 1:
            self.min_eles.pop()
        self.elements.pop()
        self.size = self.size - 1

    # @return an integer
    def top(self):
        return self.elements[-1]

    # @return an integer
    def getMin(self):
        return self.elements[self.min_eles[-1]]

    def __init__(self):
        self.elements = []
        self.min_eles = []
        self.size = 0
