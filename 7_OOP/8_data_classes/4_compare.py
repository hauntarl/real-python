"""
- Comparing Cards:

In many card games, cards are compared to each other. For instance in a typical 
trick taking game, the highest card takes the trick. As it is currently 
implemented, the PlayingCard class does not support this kind of comparison.

>>> queen_of_hearts = PlayingCard('Q', '♡')
>>> ace_of_spades = PlayingCard('A', '♠')
>>> ace_of_spades > queen_of_hearts
TypeError: '>' not supported between instances of 'Card' and 'Card'


The @dataclass decorator has two forms. So far you have seen the simple form 
where @dataclass is specified without any parentheses and parameters. However, 
you can also give parameters to the @dataclass() decorator in parentheses. The 
following parameters are supported:

- init: Add .__init__() method? (Default is True.)
- repr: Add .__repr__() method? (Default is True.)
- eq: Add .__eq__() method? (Default is True.)
- order: Add ordering methods? (Default is False.)
- unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
- frozen: If True, assigning to fields raise an exception. (Default is False.)
"""


from dataclasses import dataclass, field


@dataclass(order=True)
class OrderedPlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit} {self.rank}'


queen_hearts = OrderedPlayingCard('Q', '♡')
ace_spades = OrderedPlayingCard('A', '♠')
print(f'{ace_spades} > {queen_hearts} ? {ace_spades > queen_hearts}')
"""
You have not specified how the ordering should be done, and for some reason 
Python seems to believe that a Queen is higher than an Ace.

Data classes compare objects as if they were tuples of their fields. a Queen is 
higher than an Ace because 'Q' comes after 'A' in the alphabet.

>>> ('A', '♠') > ('Q', '♡')
False

That does not really work for us. Instead, we need to define some kind of sort 
index that uses the order of RANKS and SUITS.

>>> RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
>>> SUITS = '♣ ♢ ♡ ♠'.split()
>>> card = PlayingCard('Q', '♡')
>>> RANKS.index(card.rank) * len(SUITS) + SUITS.index(card.suit)
42

For PlayingCard to use this sort index for comparisons, we need to add a field 
.sort_index to the class. However, this field should be calculated from the 
other fields .rank and .suit automatically. This is exactly what the special 
method .__post_init__() is for. It allows for special processing after the 
regular .__init__() method is called.
"""
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


@dataclass(order=True)
class SortedPlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit} {self.rank}'


"""
The .sort_index is added as the first field of the class. That way, the
comparison is first done using .sort_index and only if there are ties are the
other fields used. Using field(), you must also specify that .sort_index
should not be included as a parameter in the .__init__() method (because it
is calculated from the .rank and .suit fields). To avoid confusing the user
about this implementation detail, it is probably also a good idea to remove
.sort_index from the repr of the class.
"""
queen_hearts = SortedPlayingCard('Q', '♡')
ace_spades = SortedPlayingCard('A', '♠')
print(f'{ace_spades} > {queen_hearts} ? {ace_spades > queen_hearts}')
