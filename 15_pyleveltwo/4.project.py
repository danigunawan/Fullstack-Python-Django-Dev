# OOP PROJECT

from random import shuffle

# two useful variables for creating cards

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class DECK:
    """
    Thisis the Deck Class. this object will create a deck of cards to initiate
    play. you can then use this deck list of cards to split in half and give to the players.
    it will use SUITE and RANKS to create the deck. It should also have a method for splitting/cutting
    the deck in half and shuffling the deck.
    """
    pass


class Hand:
    '''
    This is the hand class. each player has a hand, and can add or remove
    cards from that hand. there should be an add and remove card method here.
    '''
    pass
class Player:
	"""
	this is the player class, which takes in a name and an instance of a hand
	class object. the player can then play cards and check if they still have cards.
	"""
	pass


### GAME PLAY ###
