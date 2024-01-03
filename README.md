# snake-ladder
Snake and ladder graphic game in Python language
To run the project, first run the Welcome file. Because the first page of the game is in it.
When the game starts, every player's turn, that player's name turns red, and from here you can tell which player's turn it is. To throw the dice, click on the button on the left, which is the name of the button:
Roll Me
By pressing this button, a dice is thrown and the player moves forward by the same number of dice. The random number of the dice is also written on the word dice so that you can see it. The house where each player is located is written in front of his name.
According to the normal routine of the game, if you get bitten by a snake, your score will be reduced, which is the same house you are in, and if you get to the stairs, you will go up. Even if a player is 100 before the house and throws a dice and his score is more than 100, the player does not move until the dice comes with a number that can go directly to the house 100. Just like normal games.
Finally, every player who reaches home 100 is the winner, and when a player wins, a new page will open to announce the winner and a song will be played. I specified from the bottom of the page that the game can be exited by clicking on the button.

Functions:
When the mouse is clicked on the dice button, the move function is executed. In this function, the position of each player and how to move, for example, how much to move for each amount of dice.
Since the game board is a two-dimensional list, I defined a two-dimensional list that gives us the position of each house based on horizontal and vertical rows. The rest of the functions are related to the fact that if the position of the player or the house the player is in is in one of these areas of the list, it gives us the X and Y of that house, which, as a result, gives the X and Y of each player as his movement. adds
We have two functions nish and pele, which are related to nish and pele lists. Each of these two lists has two values, including the primary value and the secondary value. The bite and step function takes the player's score as input and checks if the player's score is equal to one of the primary values, then change the score to the secondary value.
Each button consists of two rectangles, one of which is a strip around that button. These buttons are based on the position and position of the mouse, what happens when it is clicked.

                                                                                             Alireza Mehraban 2021 - 21 - 24
