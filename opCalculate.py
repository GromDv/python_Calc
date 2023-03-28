import Calc.operation as op
import Calc.view as vw
import Calc.singleExpresn as se
import Calc.ParsedExpression as pe


class opCalculate(op.Operation):

    def __init__(self):
        num = 0

    def execute(self, view):
        ex = view.getUserExpression()
        numSubs = self.getNumExp(ex)
        vw.view.showStr("Subs:" + str(numSubs))

        tm = se.SingleExpression()

        for i in range(0, numSubs):
            tm.getSinglExpr(ex)
            ptm = pe.ParcedExpression()
            ptm.ParseSingleExpression(tm.result)
            tres = self.CalcSimpleExpession(ptm)
            if i == numSubs - 1:
                ex = ex.replace(tm.result, tres)
            else:
                ex = ex.replace('(' + tm.result + ')', tres)

        return "Результат = " + str(ex)

    def getNumExp(self, ex):
        numOpenBrackets = 1
        numCloseBrackets = 1
        for i in range(0, len(str(ex))):
            if ex[i] == '(':
                numOpenBrackets += 1
            if ex[i] == ')':
                numCloseBrackets += 1
        if not (numOpenBrackets == numCloseBrackets):
            vw.view.showStr("В выражении есть несоответствие скобок")
        return numOpenBrackets

    def CalcSimpleExpession(self, listedExprx):
        lex = pe.ParcedExpression()
        lex = listedExprx
        i = 0
        while '*' in lex.opers or '/' in lex.opers:
            if lex.opers[i] == '*':
                res = self.doMathOperation('*', lex.nums[i], lex.nums[i + 1])
                lex.opers.pop(i)
                lex.nums[i + 1] = res
                lex.nums.pop(i)
            elif lex.opers[i] == '/':
                res = self.doMathOperation('/', lex.nums[i], lex.nums[i + 1])
                lex.opers.pop(i)
                lex.nums[i + 1] = res
                lex.nums.pop(i)
            i += 1

        i = 0
        while '+' in lex.opers or '-' in lex.opers:
            if lex.opers[i] == '+':
                res = self.doMathOperation('+', lex.nums[i], lex.nums[i + 1])
                lex.opers.pop(i)
                lex.nums[i + 1] = res
                lex.nums.pop(i)
            elif lex.opers[i] == '-':
                res = self.doMathOperation('-', lex.nums[i], lex.nums[i + 1])
                lex.opers.pop(i)
                lex.nums[i + 1] = res
                lex.nums.pop(i)
            i += 1
        return lex.nums[0]

    def doMathOperation(self, op, astr, bstr):
        a = float(str(astr))
        b = float(bstr)

        if op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        elif op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        else:
            result = 0
        return str(result)
