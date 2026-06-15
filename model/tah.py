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
        # 1. Obsahuje vychozi_pole tuto figurku?
        # 2. Obsahuje cilova_pole figurku stejné barvy?
        # 3. Obsahuje cilova_pole figurku opačné barvy, a hodí se to k tomu?
        # 4. Zkontroluj figurka.muze_tahat( vychozi_pole, cilova_pole )
        # 5. Pokud ne figurka._hopper( ): jsou mezikroky prázdné?
        # 6. Dává tento tah šach králi stejné barvy?
        # 7. V případě rošády: smí se král přesunout přes pole, na kterém je ohrožen?
        # 8. V případě tahu en passant: nachází se vedle tohoto pěšáku protější pěšák 
        #    a byl tento pěšák právě teď tažen?
        # -> Mnoho kontrol vyžaduje přístup k herni_plocha, a tah č. 8 vyžaduje přístup 
        #    k historii nebo alespoň k předchozímu (polo)tahu.
        #    Možná by Tah měla být jen jednoduchá třída kontejneru a akce by měly být v RevizorTahu?
        return ...

    def proved(self):
        # Je třeba mít přístup k herni_plocha
        # Nezapominej aktualizovat figurka._was_moved
        ...
