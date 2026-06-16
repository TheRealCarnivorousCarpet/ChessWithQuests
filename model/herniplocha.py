from figurky import Figurka
from pole    import Pole
from tah     import Tah

class HerniPlocha:
    """Třída pro reprezentaci šachovnice."""
    def __init__( self,
                  vyhozene_figurky_b : list[Figurka],
                  vyhozene_figurky_c : list[Figurka],
                  rozmery : tuple[int,int] = (8,8)
                ):
        # self._herni_deska : list[list[Figurka]] = [ ]
        # Zkuste raději: self._herni_deska : dict[Pole,Figurka] = { }
        self.vyhozene_figurky_b = vyhozene_figurky_b.copy( ) # Nutné?
        self.vyhozene_figurky_c = vyhozene_figurky_c.copy( ) # Nutné?
        if not 1 <= rozmery[0] <= 9 or not 1 <= rozmery[1] <= 9:
            raise ValueError(f"Nesprávná rozměry plochy '{rozmery}'")
        self.rozmery = rozmery                               # Nutné? Jak o tom informovat Pole?

    def vrat_obsah( self, pole: Pole ) -> Figurka:
        return ...

    def posun_figurky( self, tah : Tah ) -> bool :
        return ...

    def nahrad_figurku( self, figurka : Figurka, tah : Tah ):
        ...
        return
