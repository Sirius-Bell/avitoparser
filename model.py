from dataclasses import dataclass


@dataclass(frozen=True)
class Advertisement:
    """
    Dataclass for Advertisements
    """
    title: str
    description: str
    price: str
