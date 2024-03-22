"""
My code for the Deck of Cards assignment
"""

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def present(self):
        return self.value + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
    
    def count_remaining(self):
        return len(self.cards)
    
    def get_remaining(self):
        return [x.present() for x in self.cards]

deck = Deck()

print(deck.count_remaining())
deck.shuffle()
print(deck.count_remaining())
print(deck.get_remaining())
print(deck.deal().present())
print(deck.count_remaining())
print(deck.get_remaining())
print(deck.deal().present())
print(deck.count_remaining())
print(deck.get_remaining())
print(deck.deal().present())
print(deck.count_remaining())


    