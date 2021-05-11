# COMP30024_PART_B
Expendibots is a two-person course project that I completed during my exchange semester at the University of Melbourne.

The game is played on a 8 × 8 board. Two players, White and Black, play the game. Each player initially controls 12 tokens of their own colour. Each board configuration represents a node in a tree and each move represents an edge in a tree. Basically, at their own turn, each players does a tree traversal to find the best next move.

In the first iteration, we had to come up with an agent that plays against a static opponent so we can get used to the game environment and easy AI techniques. We divided the work into two tasks: finding the winning positions of our tokens then moving our tokens to these positions in the least amount of moves. We used A* search algorithm to choose the most optimal move using the straight line distance to the goal positions as a heuristic function.

In the second iteration, we had to come up with a game playing agent that plays against another player. Our agent’s performance is graded by testing it against other agents, evolving from making random moves to selecting the best moves. To improve the performance of our agent, we designed a more complex evaluation function that takes the number of tokens on the board and their positions into consideration. We used minimax and alpha-beta pruning for tree traversal. In addition, we dynamically set the search depth because the deeper the search the better the chosen move despite the longer search time. Search depth can also be increased in critical situations. We also came up with an opening book of moves and implemented Zobrist Hashing to avoid computing the heuristic function for the same state twice (which occurs very frequently when the search depth increases) and reduce the time complexity.

Each iteration was submitted with the source code and a written report.

*search algorithms are implemented by us, use of libraries was forbidden
