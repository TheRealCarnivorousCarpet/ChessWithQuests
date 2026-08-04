from sachovnice import *
from  figurky import *
class Tah:
    def __init__(self, xstart, ystart, xfin, yfin, sacho):
        self._xstart = xstart
        self._ystart = ystart
        self._xfin = xfin
        self._yfin = yfin
        self._sacho = sacho

    def checkvect(self):
        xdiff=self._xfin-self._xstart
        ydiff=self._yfin-self._ystart
        if xdiff == 0 and ydiff == 0:
            return None, None
        fig = self._sacho.getfig(self._xstart, self._ystart)
        ispesattak = isinstance(fig, Pesak) and self._sacho.isfig(self._xfin, self._yfin)
        # If the target contains a piece, it is certain to be the opponent's, as it has been checked before.
        # When not attacking, a pawn is like any other piece.
        normvektory=fig.getnormvektory()
        if ispesattak:
            normvektory=fig.getnormuvektory()
        xbase = None

        # Whether the performed motion vector is a multiple of one of the basic motion vectors of the figure
        # is determined qualitatively by the scalar product. First, a normal vector to each basic motion vector
        # is multiplied (scalar product) with the performed vector. If the result of that operation is 0, the
        # vectors are collinear and we have found a fitting basic vector.

        for i in range(len(normvektory)):
            x,y = normvektory[i]
            if x*xdiff+y*ydiff==0:
                if not ispesattak:
                    xbase, ybase = fig.getSmery()[i]
                else:
                    xbase, ybase = fig.getuSmery()[i]
                break
        if xbase is None:
            return None, None

        # To determine whether the multiple is valid, ydiff is divided  by the basic vector's y component if
        # nonzero, else xdiff is used.

        mult = xdiff/xbase if ybase == 0 else ydiff/ybase
        minmult,maxmult = fig.getminmaxmult()
        if ispesattak:
            maxmult = 1
        if mult< minmult or mult > maxmult:
            return None, None
        return xbase, ybase


        # Do something with uvektory

    def checktarget(self):
        return (not self._sacho.isfig(self._xfin, self._yfin)) or \
            self._sacho.getfig(self._xstart, self._ystart).isbila() != self._sacho.getfig(self._xfin, self._yfin).isbila()

    def isclearpath(self, xbase, ybase):
        x = self._xstart + xbase
        y = self._ystart + ybase
        while not (x == self._xfin and y == self._yfin):
            if self._sacho.isfig(x,y):
                return False

            x += xbase
            y += ybase
        return True

    def checkenpassant(self):
        # Is the move a legal en passant move? Ignores checkvect.
        fig = self._sacho.getfig(self._xstart, self._ystart)
        if not isinstance(fig, Pesak):
            return False
        lastmove = self._sacho.getlastmove()
        lastxstart = lastmove._xstart
        lastystart = lastmove._ystart
        lastxfin = lastmove._xfin
        lastyfin = lastmove._yfin
        lastfig = self._sacho.getfig(lastxfin, lastyfin)

        if not isinstance(lastfig, Pesak):
            return False
        if not abs(lastystart-lastyfin) == 2:
            return False
        if not self._yfin == (lastyfin+lastystart)/2:
            return False
        if not lastxstart == self._xfin:
            return False
        if lastfig.isBila() == fig.isBila():
            return False

        return True

    def checkcastling(self):
        fig = self._sacho.getfig(self._xstart, self._ystart)
        if not isinstance(fig, Kral):
            return False
        if fig.ismoved():
            return False
        # Some of the following lines will cause trouble in the case of Fischer random chess,
        # but so does the entire concept of castling.
        if not (abs(5-self._xfin) == 2 and self._yfin == self._ystart):
            return False
        if self._xfin == 7:
            targetfig = self._sacho.getfig(8, self._yfin)
        else:
            targetfig = self._sacho.getfig(1, self._yfin)
        if not isinstance(targetfig, Vez):
            return False
        if targetfig.ismoved():
            return False
        # This loop should also check whether any of the fields the king moves over is being attacked.
        # checkcheck is a dummy method as of August 04th, 2026. The extra check for check before the loop is
        # needed as the king may himself not be in check but a piece is obviously present there.
        if self.checkcheck(xstart, ystart):
            return False
        # The 3rd argument of range is the step direction.
        for x in range (self._xfin, self._xstart, (self._xstart-self._xfin)/2):
            if self._sacho.isfig(x, self._yfin) or self.checkcheck(x, self._yfin) :
                return False


    def precheckmove(self):

        # special cases (castling, en passant)

        if not self._sacho.checkcoord(self._xstart, self._ystart):
            return False

        if not self._sacho.checkcoord(self._xfin, self._yfin):
            return False

        if not self._sacho.isfig(self._xstart, self._ystart):
            return False

        if not self.checktarget():
            return False

        xbase,ybase = self.checkvect()
        if xbase is None:
            return False

        if not self.isclearpath(xbase, ybase):
            return False

        return True

    def checkcheck(self, x, y):
        retrun False

    def postcheckmove(self):
        #am I in check?
        #do I give it my colour or king's coords?
        return True

    def move(self):
        if self.precheckmove():
            deadfig = self._sacho.delfig(self._xfin, self._yfin)
            # Creates a reference to the moved piece in its destination.
            self._sacho.setfig(self._sacho.getfig(self._xstart, self._ystart), self._xfin, self._yfin)
            # Deletes the reference to the moved piece in its origin.
            self._sacho.delfig(self._xstart, self._ystart)
            isenpassant = False
        elif self.checkenpassant():
            lastmove = self._sacho.getlastmove()
            lastxfin = lastmove._xfin
            lastyfin = lastmove._yfin
            deadfig = self._sacho.delfig(lastxfin, lastyfin)
            # Creates a reference to the moved piece in its destination.
            self._sacho.setfig(self._sacho.getfig(self._xstart, self._ystart), self._xfin, self._yfin)
            # Deletes the reference to the moved piece in its origin.
            self._sacho.delfig(self._xstart, self._ystart)
            isenpassant = True

        if not self.postcheckmove():
            # Undoes the moving and resurrects the removed piece if applicable.
            self._sacho.setfig(self._sacho.getfig(self._xfin, self._yfin), self._xstart, self._ystart)
            if not isenpassant:
                self._sacho.setfig(deadfig, self._xfin, self._yfin)
            else:
                self._saacho.delfig(self._xfin, self._yfin)
                self._sacho.setfig(deadfig, lastxfin, lastyfin)
            return False
        #check when these should be triggered
        self._sacho.setlastmove(self)
        return True