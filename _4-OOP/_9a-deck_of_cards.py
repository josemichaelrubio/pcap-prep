"""
From Udemy
"""

from random import shuffle
class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value
 
	def present(self):
		return self.value + ' of ' + self.suit 
class Deck:
	def __init__(self):
		suits = ['hearts', 'diamonds', 'clubs', 'spades']
		values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		self.cards = [Card(suit, value) for suit in suits for value in values]
 
	def shuffle(self):
		shuffle(self.cards)
 
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
