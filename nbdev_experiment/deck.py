# AUTOGENERATED! DO NOT EDIT! File to edit: ../01_deck.ipynb.

# %% auto 0
__all__ = ['Deck', 'draw_n']

# %% ../01_deck.ipynb 2
import random
from .card import *
from fastcore.utils import *

# %% ../01_deck.ipynb 4
class Deck:
    "A deck of 52 cards"
    def __init__(self): self.cards = [Card(s, r) for s in range(4) for r in range(1, 14) ]
    def __len__(self): return len(self.cards)
    def __str__(self): return "; ".join(map(str, self.cards))
    def __contains__(self, card): return card in self.cards
    __repr__ = __str__
    
    def shuffle(self):
        "Shuffle the cards in a deck"
        return random.shuffle(self.cards)

# %% ../01_deck.ipynb 12
@patch
def pop(self:Deck, 
        idx:int=-1): # Index of the card to remove, defaulting to the last card 
    "Remove and return one card"
    return self.cards.pop(idx)

# %% ../01_deck.ipynb 14
@patch
def remove(self:Deck,
           card:Card): # A card to remove
    "Removes `card` from deck and raises an exception if not there"
    return self.cards.remove(card)

# %% ../01_deck.ipynb 22
def draw_n(n:int, # Number of cards to draw
           replace:bool=True): # wheather or not you want replacement
    "Draw `n` cards from a deck with replacement (if `replace=True`)"
    d = Deck()
    d.shuffle()
    if replace: return [d.cards[random.choice(range(len(d.cards)))] for _ in range(n)]
    else: return d.cards[:n]
