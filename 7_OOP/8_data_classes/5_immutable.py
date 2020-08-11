"""
- Immutable Data Classes:

One of the defining features of the namedtuple you saw earlier is that it is 
immutable. That is, the value of its fields may never change. For many types of 
data classes, this is a great idea! To make a data class immutable, set 
frozen=True when you create it.
"""


from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class FrozenPosition:
    name: str
    lon: float = 0.0
    lat: float = 0.0


pos = FrozenPosition('Oslo', 10.8, 59.9)
print(pos, pos.name)
"""
>>> pos.name = 'Stockholm'
dataclasses.FrozenInstanceError: cannot assign to field 'name'

Be aware though that if your data class contains mutable fields, those might 
still change. This is true for all nested data structures in Python.
"""


@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str


@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]


print()
queen_of_hearts = ImmutableCard('Q', '♡')
ace_of_spades = ImmutableCard('A', '♠')
deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
print(deck)
deck.cards[0] = ImmutableCard('7', '♢')
print(deck)
"""
To avoid this, make sure all fields of an immutable data class use immutable 
types (but remember that types are not enforced at runtime). The ImmutableDeck 
should be implemented using a tuple instead of a list.
"""
