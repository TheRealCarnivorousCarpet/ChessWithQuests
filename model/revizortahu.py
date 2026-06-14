from herniplocha import HerniPlocha
from tah         import Tah

class RevizorTahu:
    """Třída pro šachové tahy."""
    def __init__( self,
                  plocha : HerniPlocha,
                  tah    : Tah
                 ):
        self.plocha = plocha
        self.tah    = tah

    def simulovej_tah(self) -> ...:
        return ...
