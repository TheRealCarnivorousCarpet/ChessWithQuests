"""Třídy pro práci s šachovými figurkami."""
from abc     import ABC
from enum    import Enum
from pole    import Pole
from typtahu import TypTahu

class Barva(Enum):
    """Dvě barvy."""
    BILY  = 'Bilý'
    CERNY = 'Černý'

    def __str__(self) -> str:
        return self.value


type Vektor = tuple[int,int]

class Figurka(ABC):
    """Abstraktní základní třída pro šachové figurky."""
    def __init__( self,
                  jmeno        : str,
                  jmeno_kratke : str,
                  barva        : Barva,
                  vektor       : list[Vektor] = [ ],
                  n_kroku      : int = 1,
                  hopper       : bool = False,
                  vektor_utoku : list[Vektor]|None = None,
                ) -> None :
        self.jmeno             = jmeno
        self.jmeno_kratke      = jmeno_kratke
        self.barva             = barva
        self.n_kroku           = n_kroku
        self.hopper            = hopper
        self.was_moved : bool  = False
        self.vektor : set[Vektor] = set( )
        for v in vektor:
            self.vektor |= { ( v[0]*(i+1), v[1]*(i+1) ) for i in range(n_kroku) }
        if vektor_utoku is None:
            self.vektor_utoku : set[Vektor] = self.vektor.copy( )
        else:
            self.vektor_utoku = set( )
            for v in vektor_utoku:
                self.vektor_utoku |= { ( v[0]*(i+1), v[1]*(i+1) ) for i in range(n_kroku) }


    def __str__(self) -> str:
        return self.jmeno_kratke

    def get_smery(self) -> set[Vektor] :
        return self.vektor

    def get_smery_utoku(self) -> set[Vektor] :
        return self.vektor_utoku

    def muze_tahat( self, od : Pole, do : Pole, typ_tahu : TypTahu = TypTahu.NORMALNI ) -> bool :
        # Simply according to the figure's rules, not taking into account other figures
        # Alternative: do not return bool, but an Enum of either OK or a cause for rejection
        if typ_tahu not in ( TypTahu.NORMALNI, TypTahu.UTOK ):
            return False
        delta_sloupec = do.sloupec - od.sloupec
        delta_rada    = do.rada    - od.rada
        # print(f"CONTRIL: {od=} {do=} {delta_sloupec=} {delta_rada=} {self.vektor=}")
        return ( delta_sloupec, delta_rada ) in \
               ( self.vektor if typ_tahu==TypTahu.NORMALNI else self.vektor_utoku )


class Kral(Figurka):
    """Třída pro šachovou figurku krále."""
    def __init__(self, barva : Barva):
        super().__init__( 'Král', 'K', barva,
                          [ (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) ],
                        )

    def muze_tahat( self, od : Pole, do : Pole, typ_tahu : TypTahu = TypTahu.NORMALNI ) -> bool :
        # Zvláštní pravidlo: rošáda
        if typ_tahu==TypTahu.DLOUHA_ROSADA:
            if self.was_moved:
                return False
            return ( self.barva==Barva.BILY  and od.value( )=="e1" and do.value( )=="c1" ) or \
                   ( self.barva==Barva.CERNY and od.value( )=="e8" and do.value( )=="c8" )

        if typ_tahu==TypTahu.KRATKA_ROSADA:
            if self.was_moved:
                return False
            return ( self.barva==Barva.BILY  and od.value( )=="e1" and do.value( )=="g1" ) or \
                   ( self.barva==Barva.CERNY and od.value( )=="e8" and do.value( )=="g8" )

        return super().muze_tahat( od, do, typ_tahu )


class Dama(Figurka):
    """Třída pro šachovou figurku dámy."""
    def __init__(self, barva : Barva):
        super().__init__( 'Dáma', 'D', barva,
                          [ (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) ],
                          7
                        )


class Strelec(Figurka):
    """Třída pro šachovou figurku střelce."""
    def __init__(self, barva : Barva):
        super().__init__( 'Střelec', 'S', barva, [ (1, 1), (-1, 1), (-1, -1), (1, -1) ], 7
                        )


class Kun(Figurka):
    """Třída pro šachovou figurku jezdce."""
    def __init__(self, barva : Barva):
        super().__init__( 'Kůň', 'J', barva,
                          [ (2, 1), (1, 2), (-1, 2), (-2, 1),
                            (-2, -1), (-1, -2), (1, -2), (2, -1)
                          ],
                          hopper = True
                        )


class Vez(Figurka):
    """Třída pro šachovou figurku věže."""
    def __init__(self, barva : Barva):
        super().__init__( 'Věž', 'V', barva, [ (1, 0), (0, 1), (-1, 0), (0, -1) ], 7 )

    def muze_tahat( self, od : Pole, do : Pole, typ_tahu : TypTahu = TypTahu.NORMALNI ) -> bool :
        # Zvláštní pravidlo: rošáda
        if typ_tahu==TypTahu.DLOUHA_ROSADA:
            if self.was_moved:
                return False
            return ( self.barva==Barva.BILY  and od.value( )=="a1" and do.value( )=="d1" ) or \
                   ( self.barva==Barva.CERNY and od.value( )=="d8" and do.value( )=="d8" )

        if typ_tahu==TypTahu.KRATKA_ROSADA:
            if self.was_moved:
                return False
            return ( self.barva==Barva.BILY  and od.value( )=="h1" and do.value( )=="f1" ) or \
                   ( self.barva==Barva.CERNY and od.value( )=="h8" and do.value( )=="f8" )

        return Figurka.muze_tahat( self, od, do, typ_tahu )


class Pesak(Figurka):
    """Třída pro šachovou figurku pěšaku"""
    def __init__(self, barva : Barva):
        super().__init__( 'Pěšák', '', barva,
                          vektor = [ (0, 1) ],
                          vektor_utoku = [ (1, 1), (1, -1) ],
                        )

    def muze_tahat( self, od : Pole, do : Pole, typ_tahu : TypTahu = TypTahu.NORMALNI ) -> bool :
        # Zvláštní pravidlo: první tah může přesahovat dvě políčka
        if typ_tahu==TypTahu.NORMALNI and \
           ( ( self.barva==Barva.BILY  and od.rada==2 and do.rada==4 ) or
             ( self.barva==Barva.CERNY and od.rada==7 and do.rada==5 )
           ):
            return True
        return Figurka.muze_tahat( self, od, do, TypTahu.NORMALNI \
               if typ_tahu==TypTahu.EN_PASSANT else typ_tahu )


def main( ):
    bkral = Kral(Barva.BILY)
    print( f"{bkral} Jmeno: {bkral.jmeno} Barva: {bkral.barva} #Kroku: {bkral.n_kroku}" )
    print( f"  Smer: {bkral.get_smery( )}" )
    cdama = Dama(Barva.CERNY)
    print( f"{cdama} Jmeno: {cdama.jmeno} Barva: {cdama.barva} #Kroku: {cdama.n_kroku}" )
    print( f"  Smer: {cdama.get_smery( )}" )
    bvez = Vez(Barva.BILY)
    print( f"{bvez} Jmeno: {bvez.jmeno} Barva: {bvez.barva} #Kroku: {bvez.n_kroku}" )
    print( f"  Smer: {bvez.get_smery( )}" )
    bpesak = Pesak(Barva.BILY)
    print( f"{bpesak} Jmeno: {bpesak.jmeno} Barva: {bpesak.barva} #Kroku: {bpesak.n_kroku}" )
    print( f"  Smer: {bpesak.get_smery( )}" )

    p = Pole("g5")
    print(f"{p}: {p.sloupec} {p.rada}")

    fig = bkral
    od  = Pole("a1")
    do  = Pole("a2")
    typ_tahu = TypTahu.NORMALNI
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    do  = Pole("a1")
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    do  = Pole("a3")
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    fig = cdama
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    fig = bvez
    do  = Pole("a8")
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    do  = Pole("h8")
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    fig = cdama
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    fig = bpesak
    od  = Pole("e2")
    do  = Pole("e3")
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    do  = Pole("e4")
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    do  = Pole("f3")
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    typ_tahu = TypTahu.UTOK
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")
    fig = bkral
    od  = Pole("e1")
    do  = Pole("g1")
    typ_tahu = TypTahu.KRATKA_ROSADA
    print( f"{fig}{od}-{do} {typ_tahu} ? {fig.muze_tahat(od,do,typ_tahu)}")

if __name__ == "__main__":
    main( )
