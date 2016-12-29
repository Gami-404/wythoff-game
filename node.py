class Node:
    counter1 = 0
    counter2 = 0

    # @return min of counters
    def min(self):
        if self.counter2 > self.counter1:
            return self.counter1
        else:
            return self.counter2

    # @return useful text for node
    def toString(self):
        return "counter1 (" + str(self.counter1) + ") counter2 (" + str(self.counter2) + ")"

    # @return max of value
    def max(self):
        if self.counter2 < self.counter1:
            return self.counter1
        else:
            return self.counter2

    # @return the predect depth
    def predectDepth(self):
        return (self.min() * 2) + self.max()
