# Blackjack
An analysis of the game blackjack.


# Introduction
Blackjack is a game where the outcomes can be determined based on previous turns that have been played. In order to optimize a game of blackjack, we need to understand the rules of the game, the varieties it comes with, and a understanding of statistical probabilities. The first strategy will be the option to Hit or Stand. The second Strategy will implement the option to Double. This is not a simulation of real events but rather to see how high your win rates are when using the Expected Value Formula to determine whether to hit, stand, or double. 


# Expected Value
Expected value (EV) is a key concept in probability and statistics that represents the average outcome you would expect from a random process if it were repeated many times. It helps in making decisions under uncertainty by quantifying the long-term average result.
E(X) :expected value of the random variable X
x_i :each possible outcome
P(x_i) :probability of each outcome
n = total number of possible outcomes

E(X) = sum_n[P(x_i)*x_i]


# The Game of Blackjack
In blackjack, everyone plays against the dealer. Everyone gets dealt two cards face up to start besides the dealer, who still gets two cards with one face down. The object of the game is to get closer to 21 than the dealer without going over. If a player goes over 21, that is a bust and the wager is lost. Jacks, Queens, and Kings count as 10. Aces can be played as a 1 or 11. All other cards are given their face value. Starting at the first player to the left of the dealer, they are given 3 options...
    1. They can choose to stand, which means they do not take another card  
    2. They can choose to hit, which means that ask for one more card, after which they can either choose to stand or hit again
    3. They can choose to double, which means they pay the same amount they wagered for one more card, after which they must stand.
There is a fourth option to split when a player is dealt two of the same cards. They must pay the same amount they wagered and can then play two hands. After the players are done making their turns, the dealer will reveal its face down card. If their number is less than 17, than the dealer hits until they get at least 17 or bust. If you are closer to 21 than the dealer, you win and are paid equal to the amount wagered, otherwise known as 2 to 1. If the dealer busts, you win and are paid 2 to 1. If you tie with the dealer, you neither win or lose your wager. If the is closer to 21 than the player, you lose what you wagered. If a player gets an ace and a 10, than it is an automatic win, called blackjack, which pays 3:2.


# Overview
We will simulate 10000 games of single deck blackjack as well as three deck blackjack and get an average win rate. The rules of blackjack will apply. If the player busts, than the dealer does not draw cards. We will assume that the player knows what cards are left and already played, as well as knowing what cards the dealer has. Assume the dealer has a chance to get 21 when we hit 21. We will assume that there is just one player versing the dealer with a single deck and aces are just worth 11. 


# Strategy-1
We have written a system that determines whether to hit or stand based on the expected value of staying under 21.

We observe that in single-deck blackjack, when we know which cards remain in the deck, the player wins approximately 43% of the time and loses 50% of the wagered amount on average. The distribution of outcomes follows a bell-shaped curve, indicating that, although the average result is predictable, individual game outcomes can vary significantly. In some cases, players might win or lose a large amount.

When additional decks are introduced into the game, the probability of winning remains consistent; however, the magnitude of potential wins or losses in any given hand increases. For example, in single-deck blackjack, a player might win or lose $7 in an isolated hand, while in a game with three decks, the player could win or lose $15 in a single hand. 

This shows that adding more decks increases the variability of outcomes, making both wins and losses potentially larger, even though the overall chances of winning remain unchanged.


# Strategy-2
In this strategy, we will introduce the option to double down. We will choose to double when the expected value is between 1 and 2, as these scenarios present the best opportunities to increase our wager. All previous assumptions will remain in place.

With the addition of the doubling option, our win rate remains at 43%, while the average loss is 50% of the wager. However, we notice that the magnitude of both wins and losses at isolated instances is higher due to the increased stakes when doubling.


# Stragegy-3
With the new assumption that we can only see one of the dealer's cards and that the hidden card is the best possible value of 10, we will calculate the probability of the dealer busting when they have a total value of less than 17. According to basic blackjack rules, the dealer must hit when their total is less than 17.

Under these conditions, if the dealer has a higher probability of busting than we do, provided that we have at least a total of 12, we will choose to stand. This strategy aligns with our earlier assumptions, which remain unchanged.

With these new assumptions, our average win rate has improved to 43.5%, while the average loss remains at 42% of whatever we wagered. This improvement reflects a more strategic approach compared to our previous assumptions. Previously, we were hitting hands where, if we had chosen to stand, the dealer would have been forced to hit and potentially bust instead of us. This scenario illustrates the importance of employing Basic Strategy in blackjack.


# Conclusion
In analyzing the game of blackjack, we have explored various strategies aimed at optimizing our chances of winning. By understanding the rules, probabilities, and expected value, we can make informed decisions regarding when to hit, stand, or double down.

Through our analysis, we found that using a basic strategy significantly enhances our win rates. The first strategy, which focuses on hitting or standing based on expected value, yielded a win rate of approximately 43%. Introducing the option to double down in the second strategy maintained this win rate while increasing the potential for larger wins and losses due to the higher stakes involved.

In the third strategy, we refined our approach by assuming knowledge of one of the dealer's cards and optimizing our decision-making based on the dealer's likelihood of busting. This adjustment improved our win rate to 43.5%, highlighting the importance of understanding the dealer's position and adjusting our strategy accordingly.

Overall, the findings suggest that a structured approach to blackjack, incorporating expected value and strategic decision-making, can significantly improve a player's chances of success. While blackjack remains a game of chance, informed strategies can lead to more favorable outcomes, demonstrating the balance between luck and skill in this classic casino game.


# References
https://www.venetianlasvegas.com/casino/table-games/how-to-play-blackjack.html#:~:text=In%20Blackjack%2C%20everyone%20plays%20against,and%20the%20wager%20is%20lost

https://math.libretexts.org/Bookshelves/Applied_Mathematics/Introduction_to_Game_Theory%3A_A_Discovery_Approach_(Nordstrom)/02%3A_Two-Person_Zero-Sum_Games/2.03%3A_Probability_and_Expected_Value

https://tunicatravel.com/blog/2017/05/why-does-the-house-have-an-edge-in-blackjack/
