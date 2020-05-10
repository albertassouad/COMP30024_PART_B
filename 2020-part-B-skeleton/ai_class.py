import time
import openingbook
from board import Stack

class AI:

	def __init__(self, board, player_white, depth):
		# self.parent = parent
		self.board = board
		self.turn = 0 # REMOVE LATER, FOR PERFORMANCE
		# initialize whether the player is white or not
		self.player_white = player_white
		self.depth = depth
		self.first_move = False



	def how_deep(self):
		if self.first_move == False:
			return 0
		if self.board.token_count < 5:
			return 3
		if self.board.token_count < 12:
			return 2
		else:
			return 1

	
	def best_move(self):

		if self.first_move == False:
			self.first_move = True

		self.turn += 1
		print("Turn == ", self.turn)

		alpha = -1000000
		beta = 1000000
		global_score = -100000000000


		book_form = self.board.book_form()
		if book_form in openingbook.book:
			chosen_move = openingbook.book[book_form]
			old = chosen_move[0]
			new = chosen_move[1]

			old_stack = Stack(old[0], old[1], old[2], self.player_white)
			# print(old_stack.x, old_stack.y)
			new_stack = Stack(new[0], new[1], new[2], self.player_white, old_stack)
			# print(new_stack.x, new_stack.y)
			# new_stack
			chosen_move = self.board.update_board(new_stack)
			# print("BOOK MOVE")
			return chosen_move

		for move in self.board.possible_moves(self.player_white, maximizingPlayer=True):

			local_score = self.minimax(move, self.how_deep(), self.player_white, alpha, beta, False)
			# local_score = self.minimax(move, self.depth, self.player_white, alpha, beta, False)
			# print(local_score)
			if local_score >= global_score: 
				global_score = local_score
				chosen_move = move

		# print(global_score)
		print(global_score)
		# return global_score, chosen_move
		return chosen_move


	def minimax(self, board, depth, player_white, alpha, beta, maximizingPlayer):
		# if depth == 0 or board.game_over():
		
		if depth == 0:
			# evaluate move on the colour of the players terms
			return board.evaluation(player_white)

		if maximizingPlayer: 
			# value = float("-inf")
			value = -1000000	

			# for child in board.possible_moves(self.player_player_white(player_white), maximizingPlayer=True):
			for child in board.possible_moves(player_white, maximizingPlayer=True):
			
				value = max(value, self.minimax(child, depth - 1, player_white, alpha, beta, False))
				alpha = max(alpha, value)

				if beta <= alpha: 
					break
			return value

		else:
			# value = float("inf")
			value = 1000000
			# reverse the player_white passed
			# the minimizing player is the opposite colour to our player
			# print((not player_white))
			# not player_white to reverse the colour (boolean) of the maximizing player
			for child in board.possible_moves((not player_white), maximizingPlayer=False):
				# board = Board(child)
				value = min(value, self.minimax(child, depth - 1, player_white, alpha, beta, True))
				beta = min(beta, value)
				if beta <= alpha: 
					break

			return value

