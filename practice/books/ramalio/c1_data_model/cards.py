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

selected_card = deck[0]

print(selected_card in deck)  # !__contains__ => __iter__ => __getitem__


suit_order = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card):
    card_rank = CardDeck.ranks.index(card.rank)

    result = card_rank * len(suit_order) + suit_order[card.suit]
    print(f'{card.rank} {card.suit}')
    print(f'{card_rank} * {len(suit_order)} + {suit_order[card.suit]} = {result}')
    return result


print(sorted(deck, key=spades_high))
