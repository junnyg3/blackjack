# Blackjack
An analysis of the game blackjack.


# Introduction
Blackjack is a game where the outcomes can be determined based on previous turns that have been played. In order to optimize a game of blackjack, we need to understand the rules of the game, the varieties it comes with, and a understanding of statistical probabilities. The first strategy will be the most optimal strategy where we keep track of what cards have been played as well as what cards are left in the deck to maximize our decision making. We will then implement a realistic strategy where we don't keep track of what has been played and what cards are left. The goal is to calculate the best strategy for a single game of blackjack to maximize wins and determine how to optimize such strategy based on previous decisions made.


# The Game of Blackjack
In blackjack, everyone plays against the dealer. Everyone gets dealt two cards face up to start besides the dealer, who still gets two cards with one face down. The object of the game is to get closer to 21 than the dealer without going over. If a player goes over 21, that is a bust and the wager is lost. Jacks, Queens, and Kings count as 10. Aces can be played as a 1 or 11. All other cards are given their face value. Starting at the first player to the left of the dealer, they are given 3 options...
    1. They can choose to stand, which means they do not take another card  
    2. They can choose to hit, which means that ask for one more card, after which they can either choose to stand or hit again
    3. They can choose to double, which means they pay the same amount they wagered for one more card, after which they must stand.
There is a fourth option to split when a player is dealt two of the same cards. They must pay the same amount they wagered and can then play two hands. After the players are done making their turns, the dealer will reveal its face down card. If their number is less than 17, than the dealer hits until they get at least 17 or bust. If you are closer to 21 than the dealer, you win and are paid equal to the amount wagered, otherwise known as 2 to 1. If the dealer busts, you win and are paid 2 to 1. If you tie with the dealer, you neither win or lose your wager. If the is closer to 21 than the player, you lose what you wagered. If a player gets an ace and a 10, than it is an automatic win, called blackjack, which pays 3:2.