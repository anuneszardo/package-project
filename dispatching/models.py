from decimal import Decimal
from enum import Enum

BULKY_VOLUME = Decimal('1000000')
BULKY_DIMENSION = Decimal('150')
HEAVY_MASS = Decimal('20')

class DispatchType(Enum):
    SPECIAL = 'SPECIAL'
    REJECTED = 'REJECTED'
    STANDARD = 'STANDARD'


class Package:
    def __init__(self, width: float, height: float, length: float, mass: int):
            self.width = width
            self.height = height
            self.length = length
            self.mass = mass

    @property
    def volume(self) -> float:
        return self.width * self.height * self.length

    @property
    def dimensions(self) -> tuple:
        return (self.width, self.height, self.length)

    @property
    def is_bulky(self) -> bool:
        return (
                any(dim >= BULKY_DIMENSION for dim in self.dimensions)
                or self.volume >= BULKY_VOLUME
        )

    @property
    def is_heavy(self) -> bool:
        return self.mass >= HEAVY_MASS
