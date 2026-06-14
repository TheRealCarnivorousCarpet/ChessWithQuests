class Pole:
    """Třída pro pozice na šachovnici."""
    def __init__(self, souradnice : str ):
        if len(souradnice) != 2:
            raise ValueError(f"Illegal field id '{souradnice}'")
        self.souradnice = souradnice.lower( )
        self.sloupec    = ' abcdefghi'.find(self.souradnice[0])
        self.rada       = ' 123456789'.find(self.souradnice[0])

    def __str__(self) -> str :
        return self.souradnice

    def __repr__(self) -> str :
        return f"{self.souradnice} ({self.sloupec},{self.rada})"

    def value(self) -> str :
        return self.souradnice
