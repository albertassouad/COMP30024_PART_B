class AI:

	def __init__(self, board, player_white, depth):
		# self.parent = parent
		self.board = board
		# initialize whether the player is white or not
		self.player_white = player_white
		self.depth = depth
	
	def best_move(self):
	
		alpha = -1000000
		beta = 1000000
		global_score = -1000000

		for move in self.board.possible_moves(self.player_white, maximizingPlayer=True):
			
			local_score = self.minimax(move, self.depth, self.player_white, alpha, beta, False)

			if local_score >= global_score: 
				global_score = local_score
				chosen_move = move

		print("EVALUATION == ",global_score)

		return global_score, chosen_move

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
