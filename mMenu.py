class mMenu:

    def __init__(self):
        self.menu = list()

    def ToString(self):
        res = "=======================================\n"
        res += "Чтобы выполнить операцию введите номер:\n"
        for mp in self.menu:
            res += str(mp.num) + " - " + mp.title + "\n"
        res += ": "
        return res

    def addMenuPoint(self, mp):
        self.menu.append(mp)

    def getMenuPointByNum(self, num):
        for mp in self.menu:
            if mp.num == num:
                return mp
