from dataclasses import dataclass, field
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str

    # to have an user-friendly output. Comment this and run UserFriendlyDeck
    # code to see verbose developer friendly version.
    def __str__(self):
        return f'{self.suit} {self.rank}'


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(rank=r, suit=s) for s in SUITS for r in RANKS]


@dataclass
class UserFriendlyDeck:
    # field is imported from dataclasses module
    # The argument to default_factory can be any zero parameter callable.
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    # overriding the __repr__ method provided by @dataclass, to have a more
    # user-friendly output
    def __repr__(self):
        # 'c!s' - !s forces Python to use the __str__ representation
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


print(UserFriendlyDeck())
