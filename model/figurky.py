class Figurka:
    def __init__(self, isbila, minmult=-7, maxmult=7):
        self._isbila = isbila
        self._minmult = minmult
        self._maxmult = maxmult
        self._vektory = None


    def getSmery(self):
        return self._vektory

    def isBila(self):
        return self._isbila

    def getminmult(self):
        return self._minmult

    def getmaxmult(self):
        return self._maxmult


class Kral(Figurka):
    def __init__(self, isbila, moved=False):
        super().__init__(isbila, minmult=-1, maxmult=1)
        self._vektory = [(0, 1), (1, 1), (1, 0), (1, -1)]
        self._moved = moved

    def moved(self):
        self.moved = True

class Kvida(Figurka):
    def __init__(self, isbila):
        super().__init__(isbila)
        self._vektory = [(0, 1), (1, 1), (1, 0), (1, -1)]

class Strelec(Figurka):
    def __init__(self, isbila):
        super().__init__(isbila)
        self._vektory = [(1, 1), (-1, 1)]

class Vez(Figurka):
    def __init__(self, isbila, moved=False):
        super().__init__(isbila)
        self._vektory = [(1, 0), (0, 1)]
        self._moved = moved

    def moved(self):
        self.moved = True

class Kun(Figurka):
    def __init__(self, isbila):
        super().__init__(isbila, minmult=-1, maxmult=1)
        self._vektory = [(-2, -1), (-2, 1), (-1, 2), (1, 2)]

class Pesak(Figurka):
    def __init__(self, isbila, moved=False):
        super().__init__(isbila, minmult=1, maxmult=1)
        self._vektory = [(0, 1)]
        self._uvektory = [(1, 1), (-1, 1)]
        self._svektor = [(0, 2)]
        self._moved = moved

    def moved(self):
        self.moved = True
        self._svektor = []

    def getSmery(self):
        return self._vektory + self._svektor

if __name__ == "__main__":
    testfig = Pesak(True)
    print(testfig.getSmery())
    print(testfig.isBila())
    testfig.moved()
    print(testfig.getSmery())