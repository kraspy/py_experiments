from collections import namedtuple

Card = namedtuple('Card', ('rank', 'suit'))


class CardDeck:
    ranks = [str(i) for i in range(6, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(' ')

    def __init__(self) -> None:
        self._cards = [
            Card(
                rank=rank,
                suit=suit,
            )
            for suit in self.suits
            for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


deck = CardDeck()

print(deck[0], deck[-1])
