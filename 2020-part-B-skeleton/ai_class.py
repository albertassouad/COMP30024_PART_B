class AI:

	def __init__(self, board, player_white):
		# self.parent = parent
		self.board = board
		self.player_white = player_white
		self.colour = self.player_colour(player_white)


	def player_colour(self, player_white):
		if self.player_white:
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
		for move in self.board.possible_moves(self.colour):
			# squares_to_string(move)
			# minimax to depth of 2
			local_score = self.minimax(Board(move), 2 , self.player_white, alpha, beta)
			# print(local_score)
			if local_score >= global_score: 
				global_score = local_score
				chosen_move = move
	
		print(global_score)
		return chosen_move

	def minimax(self, board, depth, player_white, alpha, beta, maximizingPlayer=True):

		if depth == 0 or board.game_over():
			return self.evaluation(board, player_white)

		if maximizingPlayer: 
			# value = float("-inf")
			value = -10000000

			for child in board.possible_moves(self.player_colour(player_white)):
				board = Board(child)
				value = max(value, self.minimax(board, depth - 1, player_white, alpha, beta, False))
				alpha = max(alpha, value)
				if beta <= alpha: 
					break
			return value
		else:
			# value = float("inf")
			value = 10000000

			for child in board.possible_moves(self.player_colour(not player_white)):
				board = Board(child)
				value = min(value, self.minimax(board, depth - 1, player_white, alpha, beta, True))
				beta = min(beta, value)
				if beta <= alpha: 
					break

			return value

	# Evaluation function will depend on what colour we are
	# simple evaluation function 
	def evaluation(self, board, player_white):
		# print(board)
		# squares_to_string(board.squares)
		my_colour = self.player_colour(player_white)
		opp_colour = self.player_colour(not player_white)
		counts = board.counts()
		n_blacks = counts['black']
		n_whites = counts['white']
		
		if counts[my_colour] == 0:
			return -1000
		elif counts[opp_colour] == 0:
			return 10000

		else:
			diff = n_whites - n_blacks

			if not player_white:
				diff = -diff
				# return eval_sum
		

		# feature of our tokens
		my_boomgroups = board.boomgroupCalc(player_white)
		my_n_boomgroup, my_boomgroup_avg = board.boomgroup_average(my_boomgroups) # (number of boomgroup, average of tokens per boomgroup)
		my_boomloss = board.count_boomloss(my_boomgroups)
		my_sum_boomloss = sum(my_boomloss.values()) # TODO, elaborate


		# feature of opponent tokens
		opp_boomgroups = board.boomgroupCalc(not player_white)
		opp_n_boomgroup, opp_avg_boomgroup  = board.boomgroup_average(opp_boomgroups) # (number of boomgroup, average of tokens per boomgroup)
		opp_boomloss = board.count_boomloss(opp_boomgroups)
		opp_sum_boomloss = sum(opp_boomloss.values())

		
		# weight is positive when the bigger the value the better
		# weight is negative when the smaller the value the better 
		features_weights = [[diff, 1], 
							[my_n_boomgroup, 1] , 
							[opp_n_boomgroup, -1],
							[my_boomgroup_avg, -1], 
							[opp_avg_boomgroup, 1],
							[my_sum_boomloss, -1],
							[opp_sum_boomloss, 1]]


		# compute evaluation based on features and weights
		eval_value = 0
		for f_w in features_weights:
			eval_value += f_w[0]*f_w[1]

		return eval_value


		# feature of opp tokens

		# eval_sum = 0
		# for i in range(8):
		# 	for j in range(8):
		# 		if board.squares[i][j] != '':
		# 			if board.squares[i][j].colour == 'white' and j <= 4:
		# 				if j <= 4:
		# 					eval_sum += 7
		# 				else:
		# 					eval_sum += 5
		# 			else: 
		# 				if j <= 4:
		# 					eval_sum += -5

		# 				else: 
		# 					eval_sum += -5

		# 				# counts[self.squares[i][j].colour] += self.squares[i][j].size
		# 	# return counts
