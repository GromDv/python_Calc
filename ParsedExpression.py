import Calc.view as vw


class ParcedExpression:

    def __init__(self):
        self.nums = []
        self.opers = []

    def ParseSingleExpression(self, ex):
        dig = ""
        ex = str(ex).replace('+-', '-')
        for i in range(0, len(ex)):
            if str(ex[i]).isdigit() or ex[i] == '.':
                dig += ex[i]
            elif ex[i] == '+' or ex[i] == '-' or ex[i] == '*' or ex[i] == '/':
                self.opers.append(ex[i])
                if len(dig) > 0:
                    self.nums.append(dig)
                    dig = ""
            elif ex[i] == " ":
                pass
            else:
                vw.view.showStr("В выражении есть непонятные символы!")
            if i == len(ex) - 1:
                self.nums.append(dig)
