"""
- More Flexible Data Classes:

So far, you have seen some of the basic features of the data class: it gives 
you some convenience methods, and you can still add default values and other 
methods. Now you will learn about some more advanced features like parameters 
to the @dataclass decorator and the field() function. Together, they give you 
more control when creating a data class.
"""

from dataclasses import dataclass, field, fields
from typing import List


@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]  # List comes from typing module


queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)


"""
- Advanced Default Values:

Say that you want to give a default value to the Deck. It would for example be 
convenient if Deck() created a regular (French) deck of 52 playing cards. First,
specify the different ranks and suits. Then, add a function make_french_deck() 
that creates a list of instances of PlayingCard.
"""
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(rank=r, suit=s) for s in SUITS for r in RANKS]


print()
print(make_french_deck())


"""
In theory, you could now use this function to specify a default value for 
Deck.cards

@dataclass
class Deck:  # Will NOT work
    cards: List[PlayingCard] = make_french_deck()

Don’t do this! This introduces one of the most common anti-patterns in Python: 
using mutable default arguments. The problem is that all instances of Deck will 
use the same list object as the default value of the .cards property. This means
that if, say, one card is removed from one Deck, then it disappears from all 
other instances of Deck as well. Actually, data classes try to prevent you from 
doing this, and the code above will raise a ValueError.

Instead, data classes use something called a default_factory to handle mutable 
default values. To use default_factory (and many other cool features of data 
classes), you need to use the field() specifier.
"""


@dataclass
class DeckWithDefaults:
    # field is imported from dataclasses module
    # The argument to default_factory can be any zero parameter callable.
    cards: List[PlayingCard] = field(default_factory=make_french_deck)


print()
print(DeckWithDefaults())
print()
print(fields(DeckWithDefaults))  # comes from dataclasses module
"""
The field() specifier is used to customize each field of a data class 
individually. You will see some other examples later. For reference, these are 
the parameters field() supports:

- default: Default value of the field
- default_factory: Function that returns the initial value of the field
- init: Use field in .__init__() method? (Default is True.)
- repr: Use field in repr of the object? (Default is True.)
- compare: Include the field in comparisons? (Default is True.)
- hash: Include the field when calculating hash()? (Default is to use the same 
        as for compare.)
- metadata: A mapping with information about the field

In the Position example, you saw how to add simple default values by writing 
lat: float = 0.0. However, if you also want to customize the field, for instance
to hide it in the repr, you need to use the default parameter: 
lat: float = field(default=0.0, repr=False). 
You may not specify both default and default_factory.

More: https://realpython.com/python-data-classes/#more-flexible-data-classes
"""
