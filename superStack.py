class superStack:

    def __init__(self):
        self.stack = []
        self.cursum = 0
        self.incr = []

    def push(self, v):
        self.stack.append(v)
        self.incr.append(0)
        self.cursum += v
        s = len(self.stack)

        print(self.stack[s - 1] )

    def pop(self):
        v = self.stack.pop()
        i = self.incr.pop()
        self.cursum -= (v+i)

        if len(self.stack) > 0:
            self.incr[- 1] += i
            print(self.stack[- 1] + self.incr[- 1])
        elif len(self.stack) == 0:
            print("EMPTY")

    def inc(self, i, v):
        self.cursum += i*v
        self.incr[- 1] += v

        print(self.stack[- 1] + self.incr[- 1])



    def sum(self):
        print( self.cursum )


if __name__ == '__main__':
    # a = superStack()
    # a.push(4)
    # a.push(5)
    # a.inc(2, 1)
    # a.sum()
    # a.pop()
    # a.pop()
    # a.sum()
    a = []
    print(a[-1])




