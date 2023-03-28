class SingleExpression:

    def __init__(self):
        self.start = -1
        self.end = 0
        self.result = ""

    def getSinglExpr(self, ex):
        start = -1
        end = 0

        for i in range(0, len(ex)):
            if ex[i] == '(':
                start = i
        if start >= 0:
            start += 1
            self.start = start
            for i in range(start, len(ex)):
                if ex[i] == ')':
                    end = i
                    break
            self.end = end
            self.result = str(ex)[self.start:self.end]
        else:
            self.start = 1
            self.end = len(ex) - 1
            self.result = ex
