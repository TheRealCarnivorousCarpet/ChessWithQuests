from figurky import *
from casovac import *
from logovac import *

class Sachovnice:
    def __init__(self, preload=True, timer=None, logger=Logovac()):
        self._playarray=[[None]*8 for i in range(8)]
        self._bilaMove=True
        self._finished=False
        self._timer=timer
        self._logger=logger
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

    def move(self, xstart, ystart, xfin, yfin):
        if self.precheckmove(xstart, ystart, xfin, yfin):
            deadfig=self.delfig(xfin, yfin)
            self.setfig(self.getfig(xstart, ystart), xfin, yfin)
            self.delfig(xstart, ystart)
            if not self.postcheckmove():
                self.setfig(self.getfig(xfin, yfin), xstart, ystart)
                self.setfig(deadfig, xfin, yfin)

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

    def checkvect(self, xstart, ystart, xfin, yfin):
        xdiff=xfin-xstart
        ydiff=yfin-ystart
        if xdiff == 0 and ydiff == 0:
            return None, None
        fig=self.getfig(xstart, ystart)
        normvektory=fig.getnormvektory()
        xbase = None

        # Whether the performed motion vector is a multiple of one of the basic motion vectors of the figure
        # is determined qualitatively by the scalar product. First, a normal vector to each basic motion vector
        # is multiplied (scalar product) with the performed vector. If the result of that operation is 0, the
        # vectors are collinear and we have found a fitting basic vector.

        for i in range(len(normvektory)):
            x,y = normvektory[i]
            if x*xdiff+y*ydiff==0:
                xbase, ybase = fig.getSmery()[i]
                break
        if xbase is None:
            return None, None

        # To determine whether the multiple is valid, ydiff is divided  by the basic vector's y component if
        # nonzero, else xdiff is used.

        mult = xdiff/xbase if ybase == 0 else ydiff/ybase
        minmult,maxmult = fig.getminmaxmult
        if mult< minmult or mult > maxmult:
            return None, None
        return xbase, ybase


        # Do something with uvektory



    def precheckmove(self, xstart, ystart, xfin, yfin):
        #check vector
        #check target (my own fig)
        #way blocked

        # special cases (castling, en passant)
        if not self.checkcoord(xstart, ystart):
            return False

        if not self.checkcoord(xfin, yfin):
            return False


        return True

    def postcheckmove(self):
        #am I in check?
        return True

if __name__ == '__main__':
    sacho=Sachovnice()
    sacho.setfig(Kvida(True), 5, 8)
    print(sacho.position())
    sacho.setdefaultpos()
    print(sacho.position())
