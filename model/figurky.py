class Figurka:
    def __init__(self, isbila, minmult=-7, maxmult=7):
        self._isbila = isbila
        self._minmult = minmult
        self._maxmult = maxmult
        self._moved = False
        self._vektory = None
        self._normvektory = None


    def getSmery(self):
        return self._vektory

    def getminmaxmult(self):
        return self._minmult, self._maxmult


    def _vektornormer(self, vektory):
        normvektory = []
        for vektor in vektory:
            x,y = vektor
            normvektory.append((-y,x))
        return normvektory

    def getnormvektory(self):
        return self._normvektory

    def isBila(self):
        return self._isbila

    def getminmult(self):
        return self._minmult

    def getmaxmult(self):
        return self._maxmult

    def moved(self):
        self.moved = True


class Kral(Figurka):
    def __init__(self, isbila, moved=False):
        super().__init__(isbila, minmult=-1, maxmult=1)
        self._vektory = [(0, 1), (1, 1), (1, 0), (1, -1)]
        self._normvektory = self._vektornormer(self._vektory)
        self._moved = moved

class Kvida(Figurka):
    def __init__(self, isbila):
        super().__init__(isbila)
        self._vektory = [(0, 1), (1, 1), (1, 0), (1, -1)]
        self._normvektory = self._vektornormer(self._vektory)

class Strelec(Figurka):
    def __init__(self, isbila):
        super().__init__(isbila)
        self._vektory = [(1, 1), (-1, 1)]
        self._normvektory = self._vektornormer(self._vektory)

class Vez(Figurka):
    def __init__(self, isbila, moved=False):
        super().__init__(isbila)
        self._vektory = [(1, 0), (0, 1)]
        self._normvektory = self._vektornormer(self._vektory)
        self._moved = moved

class Kun(Figurka):
    def __init__(self, isbila):
        super().__init__(isbila, minmult=-1, maxmult=1)
        self._vektory = [(-2, -1), (-2, 1), (-1, 2), (1, 2)]
        self._normvektory = self._vektornormer(self._vektory)

class Pesak(Figurka):
    def __init__(self, isbila, moved=False):
        super().__init__(isbila, minmult=1, maxmult=1 if moved else 2)
        self._vektory = [(0, 1)]
        self._normvektory = self._vektornormer(self._vektory)
        self._uvektory = [(1, 1), (-1, 1)]
        self._normuvektory = self._vektornormer(self._uvektory)
        self._moved = moved

    def moved(self):
        super().moved()
        self._maxmult = 1

    def getuSmery(self):
        return self._uvektory

    def getnormuvektory(self):
        return self._normuvektory

if __name__ == "__main__":
    testfig = Pesak(True)
    print(testfig.getSmery())
    print(testfig.isBila())
    testfig.moved()
    print(testfig.getSmery())