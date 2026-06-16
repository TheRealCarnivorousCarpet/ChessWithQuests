from gamelogger  import GameLogger
from herniplocha import HerniPlocha
from hrac        import Hrac
from revizortahu import RevizorTahu
from tah         import Tah
from hrac        import Uzivatel

class GameManager:
    """Třída pro správu hry."""
    def __init__( self,
                  plocha        : HerniPlocha,
                  activni_hrac  : int,
                  hraci         : list[Hrac],
                  # aktualni_tah : Tah,
                  # casovac     : GameTimer,
                  game_logger   : GameLogger,
                  # revizor_tahu : RevizorTahu
                ):
        self.plocha = plocha
        self.activni_hrac = activni_hrac
        self.hraci        = hraci.copy( )
        self.actualni_tah : Tah|None = None
        self.casovac      = GameTimer(self.hraci)
        self.game_logger  = game_logger
        # self.revizor_tahu = RevizorTahu( self.plocha, self.actualni_tah ) # ???

    def proved_tah(self) -> bool :
        return ...

    def zacni_tah(self) -> Tah :
        return ...

    def mozne_tahy(self) -> list[Tah] :
        return ...

    def zrus_tah(self):
        ...

    def ulos_log(self):
        ...

    def najdi_uzivatele( self, i : int ) -> Uzivatel :
        return self.hraci[i].uzivatel


class GameTimer:
    """Třída pro sledování času stráveného hráči ve hře."""
    def __init__( self, cas_hrac : list[Hrac] ):
        self.cas_hrac = cas_hrac.copy( )

    def nuluj_cas(self):
        ...

    def pocitej_cas( self, hrac : int ):
        ...
