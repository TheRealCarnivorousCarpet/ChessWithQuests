"""Třídy pro protokolování her."""
from enum import Enum
import io
from tah import Tah


class NotationType(Enum):
    """Různé typy notace."""
    SINGLE_LETTER = 'Single letter'
    # ...


class GameLogger:
    """Třída pro protokolování hry."""
    def __init__( self, soubor : io.TextIOBase ):
        self.soubor = soubor
        self.log : list[Tah] = [ ]

    def uloz_tah( self, tah : Tah ):
        ...

    def vytvor_soubor( self, s : str ):
        ...


class ExportWriter:
    """Třída pro zaznamenávání tahů."""
    def __init__( self, field : XXX ):
        self.field = field


class MetadataWriter:
    """Třída pro dokumentaci metadat o hře."""
    def method( self, xxx: XXX) -> XXX :
        return ...


class ChessNotationWriter:
    """Třída pro zaznamenávání tahů v šachové notaci."""
    def __init__( self, typ : NotationType ):
        self.typ = typ

    def item( self):
        ...
