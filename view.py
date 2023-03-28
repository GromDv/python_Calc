class view:

    def __init__(self, menu):
        self.menu = menu

    def Prompt(self):
        inpt = int(input(f"{self.menu.ToString()}"))
        return inpt

    def show(self, mystr):
        print(mystr)

    @staticmethod
    def showStr(mystr):
        print(mystr)

    def getUserExpression(self):
        return input("Введите выражение: ")
