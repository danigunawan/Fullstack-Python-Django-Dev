#!/usr/bin/python
# -*- coding: utf-8 -*-
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

    def __init__(self):
        print("Creating New Ordered Deck!")

        # s alias SUITE r alisa Ranks

        self.allcards = [(s, r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])


class Hand:

    '''
        This is the hand class. each player has a hand, and can add or remove
        cards from that hand. there should be an add and remove card method here.
        '''

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):

         # representasi object agar dapat dibaca secara string bkn memory

        return 'contains {} cards'.format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)  # keyword self.cards extend added_cards

    def remove_card(self):
        return self.card.pop()


class Player:

    """
        this is the player class, which takes in a name and an instance of a hand
        class object. the player can then play cards and check if they still have cards.
        """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print('{} has placed: {}'.format(self.name, drawn_card))
        print('\n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
    if len(self.hand.cards) < 3:
        return self.hand.cards
    else:
        for x in range(3):
            war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """
                Return true if player still has cards left
                """

        return len(self.hand.cards) != 0


### GAME PLAY ###

print ('Welcome to war, lets begin')

# created new deck and split it in half:

d = Deck()
d.shuffle()
(half1, half2) = d.split_in_half()

# create both players !

comp = Player('computer', Hand(half1))
name = input('what is your name?')
user = Player(name, hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1

        # menambahkan nilai kiri total_rounds = 0 dengan nilai kanan = 1

    print ('Time for a new round')
    print ('Here are the current standings')
    print (user.name + 'has the count:' + str(len(user.hand.cards)))
    print (comp.name + 'has the count:' + str(len(comp.hand.cards)))
    print ('play a card!')
    print ('\n')

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print ('war!')

        table_cards_extend(user.remove_war_cards())
        table_cards_extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print ('game over, number of rounds:' + str(total_rounds))
print ('a war happened' + str(war_count) + ' times ')            
