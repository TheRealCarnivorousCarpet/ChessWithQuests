from figurky import *
from casovac import *
from logovac import *

class Sachovnice:
    def __init__(self, preload=True, timer = None, logger = Logovac()):
        self._playarray = [[None]*8 for i in range(8)]
        # Needs to be updated by a manager of some sort.
        self._bilaMove =  True
        self._finished = False
        self._lastmove = None
        self._timer = timer
        self._logger = logger
        # False if ongoing, else: White checkmate, Black checkmate, White surrender, Black surrender, remis, stalemate
        # (potentially type of stalemate)
        #logger runs: nothing, PGN, 5 byte notation, potentially FEN or more esoteric

    def getfig(self, xpos, ypos):
        return self._playarray[ypos-1][xpos-1]

    def setfig(self, fig, xpos, ypos):
        if self.checkcoord(xpos, ypos):
            self._playarray[ypos-1][xpos-1]=fig

    def delfig(self, xpos, ypos):
        if self.checkcoord(xpos, ypos):
            deadfig=self.getfig(xpos, ypos)
            self.setfig(None, xpos, ypos)
            return deadfig
        else:
            return None

    def setlastmove(self, move):
        self._lastmove=move

    def getlastmove(self):
        return self._lastmove

    def position(self):
        return self._playarray

    def setdefaultpos(self):
        for i in range(1,9):
            self.setfig(Pesak(True), i, 2)
            self.setfig(Pesak(False), i, 7)
        self.setfig(Vez(True), 1, 1)
        self.setfig(Vez(True), 8, 1)
        self.setfig(Vez(False), 1, 8)
        self.setfig(Vez(False), 8, 8)
        self.setfig(Kun(True), 2, 1)
        self.setfig(Kun(True), 7, 1)
        self.setfig(Kun(False), 2, 8)
        self.setfig(Kun(False), 7, 8)
        self.setfig(Strelec(True), 3, 1)
        self.setfig(Strelec(True), 6, 1)
        self.setfig(Strelec(False), 3, 8)
        self.setfig(Strelec(False), 6, 8)
        self.setfig(Kral(True), 5, 1)
        self.setfig(Kvida(True), 4, 1)
        self.setfig(Kral(False), 5, 8)
        self.setfig(Kvida(False), 4, 8)

    def checkcoord(self, xpos, ypos):
        if xpos in range(1,9) and ypos in range(1,9):
            return True
        else:
            print('invalid position')
            return False

    def isfig(self, xpos, ypos):
        return self.getfig(xpos, ypos) is not None


if __name__ == '__main__':
    sacho=Sachovnice()
    sacho.setfig(Kvida(True), 5, 8)
    print(sacho.position())
    sacho.setdefaultpos()
    print(sacho.position())
