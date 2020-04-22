
from board import Board
import random
class ExamplePlayer:
    def __init__(self, colour):
        """
        This method is called once at the beginning of the game to initialise
        your player. You should use this opportunity to set up your own internal
        representation of the game state, and any other information about the 
        game state you would like to maintain for the duration of the game.

        The parameter colour will be a string representing the player your 
        program will play as (White or Black). The value will be one of the 
        strings "white" or "black" correspondingly.
        """
        # TODO: Set up state representation.

        self.board = Board(whites_init, blacks_init)


    def action(self):
        """
        This method is called at the beginning of each of your turns to request 
        a choice of action from your program.

        Based on the current state of the game, your player should select and 
        return an allowed action to play on this turn. The action must be
        represented based on the spec's instructions for representing actions.
        """
        # TODO: Decide what action to take, and return it
        board = self.board
        token = board.whites[random.randint(0, len(board.whites) - 1)]
        move = token.moves()[random.randint(0, len(token.moves()) - 1)]
        return ('MOVE', 1, (token.x, token.y), (move.x,move.y))

    def update(self, colour, action):
        """
        This method is called at the end of every turn (including your player’s 
        turns) to inform your player about the most recent action. You should 
        use this opportunity to maintain your internal representation of the 
        game state and any other information about the game you are storing.

        The parameter colour will be a string representing the player whose turn
        it is (White or Black). The value will be one of the strings "white" or
        "black" correspondingly.

        The parameter action is a representation of the most recent action
        conforming to the spec's instructions for representing actions.

        You may assume that action will always correspond to an allowed action 
        for the player colour (your method does not need to validate the action
        against the game rules).
        """
        # TODO: Update state representation in response to action.
        print(action)
        self.board.update(action[3][0], action[3][1], action[1])


blacks_init = [(0,7), (1,7),   (3,7), (4,7),   (6,7), (7,7),
               (0,6), (1,6),   (3,6), (4,6),   (6,6), (7,6)]

whites_init = [(0,1), (1,1),   (3,1), (4,1),   (6,1), (7,1),
                (0,0), (1,0),   (3,0), (4,0),   (6,0), (7,0)]
