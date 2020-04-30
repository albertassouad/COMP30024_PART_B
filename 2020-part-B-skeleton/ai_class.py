class AI:

	def __init__(self, board, player_white):
		# self.parent = parent
		self.board = board
		# initialize whether the player is white or not
		self.player_white = player_white
		# colour of the player
		self.colour = self.player_colour(player_white)
		# turn number
		self.turn = 1

	# function to determine how deep our minimax fucnction will search
	# shoudl depend on number of tokens left on the board
	def how_deep(self):
		if self.turn < 5:
			return 1
		elif self.turn < 20:
			return 2
		else:
			return 3

	def player_colour(self, player_white):
		if player_white:
			return "white"
		return "black"

	# def best_move(self, board, player_white):
	def best_move(self):
	# def best_move(board, player_white):
		# if move_number == 1: 
		# 	opening_book()
		alpha = -1000000
		beta = 10000000
		global_score = -1000000
		# colour = player_colour(player_white)
		# for move in board.possible_moves(colour):
		# for each move that can result from this board
		# a move is a board object
		# print(self.colour)
		# print(self.player_white)
		for move in self.board.possible_moves(self.colour, maximizingPlayer=True):
			# squares_to_string(move)
			# minimax to depth of 2
			# local_score = self.minimax(Board(move), 2 , self.player_white, alpha, beta)
			# local_score = self.minimax(move, self.how_deep() , self.player_white, alpha, beta, True)
			local_score = self.minimax(move, 2, self.player_white, alpha, beta, False)
			# local_score = self.minimax(move, self.how_deep(), self.player_white, alpha, beta, False)

			# print(local_score)
			# squares_to_string(move.squares)
			if local_score >= global_score: 
				global_score = local_score
				chosen_move = move

		print(self.colour)
		print(global_score)
		return chosen_move

	def minimax(self, board, depth, player_white, alpha, beta, maximizingPlayer):
		# if depth == 0 or board.game_over():
		if depth == 0:
			# evaluate move on the colour of the players terms
			return board.evaluation(player_white)

			# if maximizingPlayer:
			# 	return -1*board.evaluation(player_white) 
			# else:
			# 	return board.evaluation(player_white) 
		
			

			# if player_white: 
			# 	return board.evaluation(player_white) 
			# else:
			# 	return -board.evaluation(player_white) 
			# return self.evaluation(board, player_white)
			# return board.evaluation(player_white) 


		# we try to return the move that 
		if maximizingPlayer: 
			# value = float("-inf")
			value = -10000000	
			# we are the maximizing player
			# print(player_white)
			# player_white = not player_white
			# print(not player_white)
			# print(self.player_colour(player_white))
			# print(self.player_colour(not player_white))
			# if maximimzing the moves generated will be opposite

			for child in board.possible_moves(self.player_colour(player_white), maximizingPlayer=True):
				# print(child)
				# board = Board(child)
				value = max(value, self.minimax(child, depth - 1, player_white, alpha, beta, False))
				alpha = max(alpha, value)
				if beta <= alpha: 
					break
			return value
		else:
			# value = float("inf")
			value = 10000000
			# reverse the colour passed
			for child in board.possible_moves(self.player_colour(not player_white), maximizingPlayer=False):
				# board = Board(child)
				value = min(value, self.minimax(child, depth - 1, player_white, alpha, beta, True))
				beta = min(beta, value)
				if beta <= alpha: 
					break


			return value