import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDesk(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                       for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


# Create a single instance
beer_card = Card('7', 'spades')
print(beer_card)

# Complete desk
french_desk = FrenchDesk()
print(len(french_desk))

print()

print(french_desk[0])
print(french_desk[42])
print(french_desk[19])
print(french_desk[-1])

print()

print(choice(french_desk))
print(choice(french_desk))
print(choice(french_desk))

print()

print(french_desk[:3])
print(french_desk[12::13])

print()

for card in french_desk:
    print(card)

print()

for card in reversed(french_desk):
    print(card)
