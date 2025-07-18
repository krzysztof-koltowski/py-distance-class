from __future__ import annotations
from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km: Union[int, float] = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented  # type: ignore

    def __iadd__(self, other: Union[Distance, int, float]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented  # type: ignore
        return self

    def __mul__(self, factor: Union[int, float]) -> Distance:
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        return NotImplemented  # type: ignore

    def __truediv__(self, divisor: Union[int, float]) -> Distance:
        if isinstance(divisor, (int, float)):
            if divisor == 0:
                raise ValueError("Cannot divide by zero.")
            return Distance(round(self.km / divisor, 2))
        return NotImplemented  # type: ignore

    def __lt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented  # type: ignore

    def __gt__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented  # type: ignore

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False

    def __le__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented  # type: ignore

    def __ge__(self, other: Union[Distance, int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented  # type: ignore
