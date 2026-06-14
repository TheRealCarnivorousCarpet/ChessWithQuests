from figurky import Barva
from kwest   import Kwest

class Hrac:
    """Třída pro reprezentaci šachisty účastnícího se partie."""
    def __init__( self, barva : Barva, uzivatel : Uzivatel ):
        self.barva    = barva
        self.uzivatel = uzivatel

    def get_elo_rating(self) -> int :
        return self.uzivatel.elo


class Uzivatel:
    """Třída pro reprezentaci šachového nadšence."""
    def __init__( self,
                  uzivatelske_jmeno : str,
                  jmeno             : str,
                  email             : str,
                  elo               : int,
                  splnene_kwesty    : list[Kwest]
                 ):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.jmeno             = jmeno
        self.email             = email
        self.elo               = elo
        self.splnene_kwesty    = splnene_kwesty.copy( )

    def pridej_kwest( self, kwest: Kwest ):
        self.splnene_kwesty.append(kwest)