class Game:

	def __init__(self, my_player, opponent, board_state):
		self.white_player = my_player 
		self.black_player = opponent
		self.board_state = board_state
		# whites turn
		self.player_white = True

	def play(self):

		play_order = []

		if self.my_player.player_white == True:
			play_order += [self.my_player] + [self.opponent]
		else:
			play_order += [self.opponent] + [self.my_player]

		# position_values = []
		# board_vectors = []

		moves = 0 
		# game will continue for 250 moves
		# or until 1 players pieces have been eliminated
		# while moves < 20:
		reward = board.outcome()
		while reward == None:

			agent = play_order[moves%2]

			chosen_move, score = agent.best_move()
			squares_to_string(chosen_move.squares)

			# print(chosen_move.vector_form())
			# print(score)

			#updates board of the players
			self.my_player.board = chosen_move 
			self.opponent.board = chosen_move

			reward = board.outcome()

			# if agent == self.my_player:
			# 	position_values.append(score)
			# 	board_vectors.append(chosen_move.vector_form())

			# moves+=1

		# return reward
		return position_values, board_vectors


from random import choice

class LearningEnvironment:

	# def __init__(self, my_player, opponent, board_state):
	def __init__(self, board_state):


		# self.white_player = my_player 
		# self.black_player = opponent
		self.board_state = board_state
		# whites turn
		self.player_white = True


	def make_random_move(self):
		all_moves = self.board_state.possible_moves(self.player_white, True)
		chosen_move = choice(all_moves)

		self.board_state = chosen_move
		self.player_white = (not self.player_white)

	def reset(self): 
		self.board_state = Board.new_board()
		# self.my_player.board = self.board_state
		# self.opponent.board = self.board_state


	def get_reward(self):
		# print(self.board_state)
		return self.board_state.outcome()


	def make_move(self, chosen_move):
		self.board_state = chosen_move
		# self.my_player.board = chosen_move 
		# self.opponent.board = chosen_move
		self.player_white = (not self.player_white)
		


	# # functions for transition table (leave for now)
	# def flatten(self, reverse=False): 
	# 	flattened = []
	# 	if reverse:
	# 		squares = self.squares[::-1]

	# 	for row in self.squares[::-1]:
	# 		for entry in row:
	# 			if entry == '':
	# 				flattened.append(13)
	# 			else:
	# 				flattened.append(entry.flatten())
	# 	return flattened


	# def hashkey(self):
	# 	k1 = 0 
	# 	k2 = 0

	# 	for x in self.flatten():
	# 		k1 *= 3
	# 		k1 += int(x)
	# 		assert k1 >= 0

	# 	for x in self.flatten(True):
	# 		k2 *= 3
	# 		k2 += int(x)
	# 		assert k2 >= 0

	# 	if k2 < k1:
	# 		return k2, True
	# 	else:
	# 		return k1, False

# class TranspositionTable:

# 	WHITE_STACK = -1
# 	BLACK_STACK = 2

# 	def __init__(self, maxitems = 100000):
# 		self.maxitems = maxitems
# 		self.cache = OrderedDict(0)

# 	def put(self, board, depth, score):
# 		entry = Entry(move, depth, int(score), state)