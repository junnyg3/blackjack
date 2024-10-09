import random
import matplotlib.pyplot as plt
import numpy as np
import sys

from functions import StandardDeck, card_value, prob2


def BlackJack_d(games,decks):
    """
        Prints Average Win Rate and Average Profit for a game of blackjack with histogram visuals of how much won per game

        Parameters: games,wager,decks
            Tell it how many games of blackjack you want to play, how much each wager per hand, and how many decks to play
        
        Returns: print
            Prints
    """
    ###> Play games n times
    games = int(games)
    wager = 1
    decks = int(decks)

    avgWR = 0
    avgPOT = 0
    totWR = 0
    totPOT = 0
    pplot = np.zeros(games)
    x = np.linspace(1,games,games)
    k = 0
    for i in range(0,games):
        games_won = 0
        games_played = 0
        wr = 0
        pot = 0
        ###> Initialize n Decks
        deck = StandardDeck()
        for j in range (0,decks-1):
            temp = StandardDeck()
            deck = deck + temp

        ###> Shuffle Deck
        random.shuffle(deck)
        #random.Random(3).shuffle(deck)

        ###> Play till cards reach a minimum of 6
        while len(deck) > 10:
            pbust = False
            dbust = False
            dwin = False
            #print("Round #",games_played+1)
            ###>Deal cards
            pC = [deck.pop(), deck.pop()]
            dC = [deck.pop(), deck.pop()]

            ###> Calculate Score
            pS = sum(card_value(card) for card in pC)
            dS = sum(card_value(card) for card in dC)
            #print("Players Cards:",pC,"Score: ",pS)
            #print("Dealers Cards:",dC[0],"Score: ",dS)
            if pS>21:
                #print("Player busted with:",pS)
                pbust = True

            if dS>21:
                #print("Dealer busted with:",dS)
                dbust = True


            ###> Calculate probability of hitting and not busting
            hit = False
            stand = False
            double = False
            ds = card_value(dC[0])+10
            hit,stand,double = prob2(pS,deck,ds)

            ###> Loop players turn
            while (hit == True) & (pbust == False) & (dbust == False):
                new_card = deck.pop()
                pC.append(new_card)
                pS = sum(card_value(card) for card in pC)
                #print("Players Cards:",pC,"Score: ",pS)
                if pS>21:
                    #print("Player busted with:", pS)
                    pbust = True
                    break
                hit,stand,double = prob2(pS,deck,ds)

            if double == True:
                new_card = deck.pop()
                pC.append(new_card)
                pS = sum(card_value(card) for card in pC)
                #print("Players Cards:",pC,"Score: ",pS)
                if pS>21:
                    #print("Player busted with:", pS)
                    pbust = True

            ###> If player busted, stop the game
            if pbust == True:
                #print("Dealer Wins")
                if double == True:
                    pot = pot - 2*wager
                else:
                    pot = pot - wager

            ###> Else, loop dealers turn
            else:
                while dS < 17:
                    new_card = deck.pop()
                    dC.append(new_card)
                    dS += card_value(new_card)
                    #print("Dealers Cards:",dC,"Score: ",dS)
                    if dS>21:
                        #print("Dealer busted with:",dS)
                        dbust = True

                if dbust == True:
                    #print("Player Wins")
                    if double == True:
                        pot = pot + 2*wager
                        games_won +=1
                    else:
                        pot = pot + wager
                        games_won +=1
                else:
                    if pS==dS:
                        #print("Tie")
                        do_nothing = True
                    elif pS>dS:
                        #print("Player Wins")
                        if double == True:
                            pot = pot + 2*wager
                            games_won +=1
                        else:
                            pot = pot + wager
                            games_won +=1
                    else:
                        #print("Dealer Wins")
                        if double == True:
                            pot = pot - 2*wager
                        else:
                            pot = pot - wager
            #print(len(deck))
            #print(pot)
            i +=1
            pC = 0
            pS = 0
            dC = 0
            dS = 0
            games_played +=1

        #Game Over
        wr = games_won/games_played*100
        #print("GAME OVER ")
        #print("Number of games played: ",games_played)
        #print("Number of games won: ",games_won)
        #print("Win Rate: ",wr,"%")
        #print("Amount wagered per game:$",wager)
        #print("Total Gains:$",pot)
        totWR = totWR + wr
        totPOT = totPOT + pot
        pplot[k] = pot
        k += 1
    avgWR = totWR/games
    avgPOT = totPOT/games
    print("Average Win Rate: ",avgWR)
    print("Average Gain: ",avgPOT)
    plt.hist(pplot)
    plt.show()

if __name__ == "__main__":
    g = sys.argv[1]
    d = sys.argv[2]
    BlackJack_d(g,d)