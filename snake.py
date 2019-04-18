'''
Authors: Kunal Dani, Shyanne Salen, Marina Morrow
Last Modified: April 18th, 2019

This file contains the code used to play a game of snake with a twist.
The goal is for the snake to eat a set of cherries (or units of something) without eating itself.
Everytime the snake eats one cherry, it will get bigger by one unit.
After it eats 10 cherries, it will change color. Users can try to see who can
eat the most cherries or who can finish the 5 levels (50 cherries total?).

Planning
The we can break this down into components:
First making the snake class and giving it the ability to move using arrow keys
Next we can set up our grid, its dimensions as well as randomize the location of the cherry
everytime the snake position overlaps with the cherry position (can use overlap from lazor)
Then we can give the snake the attribute of growing everytime it overlaps/eats the cherry.
Finally we can worry about the twist, and the different snake skins
If we would like to add extra, we can add scores or do a multiplayer game like slither.io, where
we can give another user their own snake and the ability to move using other keys (like -w,-a,-s,-d etc.)

'''

