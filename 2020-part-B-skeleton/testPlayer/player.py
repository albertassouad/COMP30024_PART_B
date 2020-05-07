
from board2 import Board
from board2 import Stack
from board2 import squares_to_string
from ai_class2 import AI
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
        colour_bool = True
        if colour == "black": colour_bool = False
        self.board = Board.new_board()
        self.agent = AI(self.board, player_white = colour_bool, depth = 2)


    def action(self):
        """
        This method is called at the beginning of each of your turns to request 
        a choice of action from your program.

        Based on the current state of the game, your player should select and 
        return an allowed action to play on this turn. The action must be
        represented based on the spec's instructions for representing actions.
        """
        # TODO: Decide what action to take, and return it
        
        # agent decide move
        

        chosen_move = self.agent.best_move()[1]

        if chosen_move.boom_at == None: # it is "MOVE"
            return ("MOVE", chosen_move.to_.size, (chosen_move.from_.x, chosen_move.from_.y), (chosen_move.to_.x,chosen_move.to_.y))
        else: # it is "BOOM"
            return ("BOOM", (chosen_move.boom_at[0], chosen_move.boom_at[1])) # boom_at is a tuple

        
    
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
        colour_bool = True
        if colour == "black": colour_bool = False
        if action[0] == "BOOM":
            new_stack = Stack(action[1][0], action[1][1], 1, colour_bool)
            self.board = new_stack.boom(self.board) # board update to boom move
            self.agent.board = self.board
        else:
            parent_stack = self.board.squares[action[2][0]][action[2][1]]
            new_stack = Stack(action[3][0], action[3][1], action[1], colour_bool, parent = parent_stack)
            self.board = self.board.update_board(new_stack) # board update to stack move
            self.agent.board = self.board
        
        
