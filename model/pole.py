class Pole:
    """Třída pro pozice na šachovnici."""

    SLOUPCE = ' abcdefghij'
    RADY    = ' 123456789'

    def __init__(self, souradnice : str ):
        if len(souradnice) != 2:
            raise ValueError(f"Illegal field id '{souradnice}'")
        self.souradnice = souradnice.lower( )
        self.sloupec    = self.SLOUPCE.find(self.souradnice[0])
        self.rada       = self.RADY.find(self.souradnice[1])

    @classmethod
    def from_sloupec_rada( cls, s : int, r : int ) -> Pole:
        if not 1 <= s <= 9 or not 1 <= r <= 9:
            raise ValueError(f"Coordinates out of bounds: ({s},{r})")
        return Pole(f"{cls.SLOUPCE[s]}{cls.RADY[r]}")

    def __str__(self) -> str :
        return self.souradnice

    def __repr__(self) -> str :
        return f"{self.souradnice} ({self.sloupec},{self.rada})"

    def value(self) -> str :
        return self.souradnice


def main( ):
    p = Pole("g5")
    print(f"{p}: ({p.sloupec},{p.rada})")
    p = Pole.from_sloupec_rada(4,2)
    print(f"{p}: ({p.sloupec},{p.rada})")


if __name__ == "__main__":
    main( )
