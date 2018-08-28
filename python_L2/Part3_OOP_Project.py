#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle



class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    

    def __init__(self):
	    self.DECK = [(suite, ranks) for suite in self.SUITE for ranks in self.RANKS]
	
    def shuffleDeck(self):
	    return shuffle(self.DECK)

    def splitDeck(self):
        return (self.DECK[:26], self.DECK[26:])#creates a tuple which can be partitioned between multiple variables

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self, cards):
    	self.cards = cards

    def addCard(self, newCard):
    	return self.cards.extend(newCard)


    def removeCard(self):
    	return self.cards.pop()

class Player():
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards
    """
    def __init__(self, name, hand):
    	self.hand = hand
    	self.name = name

    def playCards(self):
    	return self.hand.removeCard()

    def cardCount(self):
    	return len(self.hand.cards) 


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#instantiate all necessary variables
rounds = 0
war = 0;


#instantiate the deck 
deck = Deck()
deck.shuffleDeck()

#create variables to hold the split deck
playerOneHand, playerTwoHand = deck.splitDeck()

print("Player 1 hand:")
print(playerOneHand)
print("Player 2 hand:")
print(playerTwoHand)


#instantiate player classes; taking in a name and Hand object as arguments
player1 = Player("John", Hand(playerOneHand))
player2 = Player("Nic", Hand(playerTwoHand))

# Use the 3 classes along with some logic to play a game of war!
#create the game here
while player1.cardCount() > 0 and player2.cardCount() > 0:
	print(player1.cardCount())
	print(player2.cardCount())

	rounds += 1
	tableCards = []
	print("Round: {r}".format(r = rounds))


	p1Card = player1.playCards()
	p2Card = player2.playCards()
	print(p1Card)
	print(p2Card)

	tableCards.append(p1Card)
	tableCards.append(p2Card)

	if deck.RANKS.index(p1Card[1]) > deck.RANKS.index(p2Card[1]):
		print("Player 1 wins this round...")
		player1.hand.addCard(tableCards)
	elif deck.RANKS.index(p1Card[1]) < deck.RANKS.index(p2Card[1]):
		print("Player 2 wins this round...")
		player2.hand.addCard(tableCards)
	else:
		war += 1
		print("WAR!")

		if player1.cardCount() < 4 or player2.cardCount() < 4:
			break

		for c in range(3):
			tableCards.append(player1.playCards())
			tableCards.append(player2.playCards())

		if deck.RANKS.index(p1Card[1]) > deck.RANKS.index(p2Card[1]):
			print("Player 1 won this battle...")
			player1.hand.addCard(tableCards)
		elif deck.RANKS.index(p1Card[1]) < deck.RANKS.index(p2Card[1]):
			print("Player 2 won this battle...")
			player2.hand.addCard(tableCards)


print("------------------------------------------------")
print("GAME OVER!")
print("Total number of War Rounds: {w}".format(w = war))
print("Total number of Rounds: {r}".format(r = rounds))
print("------------------------------------------------")

if(player1.cardCount() > player2.cardCount()):
	print("Player 1 wins with {c} cards remaining".format(c = player1.cardCount()))
else:
	print("Player 2 wins with {c} cards remaining".format(c = player2.cardCount()))







