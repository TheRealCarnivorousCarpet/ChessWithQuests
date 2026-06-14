from enum import Enum

class TypTahu(Enum):
    """Typy šachových tahu."""
    NORMALNI      = 'Normalní'
    UTOK          = 'Útok'
    EN_PASSANT    = 'En passant'
    DLOUHA_ROSADA = 'Dlouhá rošáda'
    KRATKA_ROSADA = 'Kratká rošáda'

    def __str__(self) -> str:
        return self.value
