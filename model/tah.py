from figurky     import Figurka
from pole        import Pole
from typtahu     import TypTahu

class Tah:
    """Třída pro šachové tahy."""
    def __init__( self,
                  vychozi_pole : Pole,
                  cilova_pole  : Pole,
                  figurka      : Figurka,
                  typ_tahu     : TypTahu
                 ):
        self.vychozi_pole = vychozi_pole
        self.cilova_pole  = cilova_pole
        self.figurka      = figurka
        self.typ_tahu     = typ_tahu

    def __str__(self):
        if self.typ_tahu==TypTahu.DLOUHA_ROSADA:
            return "0-0-0"
        if self.typ_tahu==TypTahu.KRATKA_ROSADA:
            return "0-0"
        symbol1 = 'x'    if self.typ_tahu==TypTahu.UTOK       else '-'
        symbol2 = 'e.p.' if self.typ_tahu==TypTahu.EN_PASSANT else ''
        return f"{self.figurka.jmeno_kratke}{self.vychozi_pole}{symbol1}{self.cilova_pole}{symbol2}"

    def over_platnost(self) -> bool:
        # Checks needed:
        # 1. Does vychozi_pole contain this figurka?
        # 2. Does cilova_pole contain a figure of the same colour?
        # 3. Does cilova_pole contain a figure of the opposite colour, and does typ_tahu
        #    fit to this?
        # 4. Check figurka.muze_tahat( vychozi_pole, cilova_pole )
        # 5. If not figurka._hopper( ): are intervening fields empty?
        # 6. Does the move put the king of the same colour in check?
        # 7. In case of rochade: does the king move over a field under threat?
        # 8. In case of en passant: is an opposite pawn next to this pawn, and was that pawn
        #    moved just now?
        # -> Many checks need access to herni_plocha, and check 8 needs access to the history
        #    or at least the previous (half-)move.
        #    Maybe Tah should be a simple container class, and actions should be in RevizorTahu?
        return ...

    def proved(self):
        # Needs access to herni_plocha
        # Do not forget to update figurka._was_moved
        ...
