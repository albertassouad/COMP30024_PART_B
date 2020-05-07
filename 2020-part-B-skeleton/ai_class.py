import time
class AI:

	def __init__(self, board, player_white, depth):
		# self.parent = parent
		self.board = board
		# initialize whether the player is white or not
		self.player_white = player_white
		self.depth = depth
		self.turn = 0
	
	def best_move(self):
		
		alpha = -1000000
		beta = 1000000
		global_score = -1000000

		self.turn += 1
		
		# depth depenjds opn number of turns
		# if self.turn < 5: 
		# 	self.depth = 1
		# else: 	
		# 	self.depth = 2 

		# depth depends on number of tokens
		# white_token_count = 0
		# black_token_count = 0
		# for stack in self.board.stack_list:

		# 	if stack.player_white: white_token_count += 1
		# 	else: black_token_count += 1

		# if self.player_white and black_token_count < 5:
		# 	self.depth = 3
		# if not self.player_white and white_token_count < 5:
		# 	self.depth = 3


		tic = time.perf_counter()

		possible_moves = self.board.possible_moves(self.player_white, maximizingPlayer=True)
		tic = time.perf_counter() - tic 

		print("possible_moves returned in ",tic)
		
		tic = time.perf_counter()
		for move in possible_moves:

			
			local_score = self.minimax(move, self.depth, self.player_white, alpha, beta, False)

			if local_score >= global_score: 
				global_score = local_score
				chosen_move = move
		tic = time.perf_counter() - tic 

		print("Best move returned in ",tic)
		print("EVALUATION == ",global_score)
		print("TURN == ", self.turn)
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
