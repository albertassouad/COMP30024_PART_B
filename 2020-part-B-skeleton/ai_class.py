import time
import random
from board import Board

class AI:

	def __init__(self, board, player_white, depth):
		# self.parent = parent
		self.board = board
		# initialize whether the player is white or not
		self.player_white = player_white
		self.depth = depth
		self.turn = 0
		self.zorbist_table = [] # 
		self.board_cache = {} # {zorbist hash key : [move (board) , evaluation, alpha, beta]}
		self.init_zorbist_table()
	
	
	def init_zorbist_table(self):
		# fill a table of random numbers/bitstrings
  
		for i in range(8): # width
			zorbist1 = []
			for j in range(8): # length
				zorbist2 = []
				for k in range(23): # 24 possible configuration of this position
					zorbist2.append(random.getrandbits(64))

				zorbist1.append(zorbist2)

			self.zorbist_table.append(zorbist1)



	def get_zorbist_hash(self, board):
		h = 0
		for i in range(8): # width
			for j in range(8): # length
				if board.squares[i][j] != '': # True/player_white

					# white
					if board.squares[i][j].player_white:
						config = 0 + board.squares[i][j].size # range [0,11]
						h = h ^ self.zorbist_table[i][j][config] # XOR operartion

					# black
					else:
						config = 11 + board.squares[i][j].size # range [12,23]
						h = h ^ self.zorbist_table[i][j][config]  # XOR operartion

		return h



	def how_deep(self):
		if self.turn <= 3:
			return 0
		elif self.board.token_count < 5:
			return 2
		elif self.board.token_count < 3:
			return 3
		else:
			return 1

	def best_move(self):
		
		alpha = -1000000
		beta = 1000000
		global_score = -1000000

		self.turn += 1
		print("I AM AI 1111")
		print("Turn == ", self.turn)

		possible_moves = self.board.possible_moves(self.player_white, maximizingPlayer=True)
		
		for move in possible_moves:

			
			local_score = self.minimax(move, self.how_deep(), self.player_white, alpha, beta, False)

			if local_score >= global_score: 
				global_score = local_score
				chosen_move = move
	
		return global_score, chosen_move

	def minimax(self, board, depth, player_white, alpha, beta, maximizingPlayer):
		# if depth == 0 or board.game_over():
		v = 0
		if depth == 0:
			# evaluate move on the colour of the players terms
			return board.evaluation(player_white)

		if maximizingPlayer: 
			# value = float("-inf")
			value = -1000000

			
			# for child in board.possible_moves(self.player_player_white(player_white), maximizingPlayer=True):
			for child in board.possible_moves(player_white, maximizingPlayer=True):

				# CHECK IF BOARD ALREADY EVALUATED IN TABLE
				z_hash = self.get_zorbist_hash(child)

				# if board state in board_cache and needed value exist
				if z_hash in self.board_cache and self.board_cache[z_hash][0] != None and self.board_cache[z_hash][2] != None :
					v += 1
					print("Z From cache", v)
					value = self.board_cache[z_hash][0]
					alpha = self.board_cache[z_hash][2]

				# else update board cache
				else:
					value = max(value, self.minimax(child, depth - 1, player_white, alpha, beta, False))
					alpha = max(alpha, value)

					# update entry in board_cache
					if z_hash in self.board_cache:
						self.board_cache[z_hash][0] = value
						self.board_cache[z_hash][2] = alpha

					# new entry in board_cache
					else: 
						array = [value, None, alpha, None] # [max_value, min_value, alpha, beta]
						self.board_cache[z_hash] = array 

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

				# CHECK IF BOARD ALREADY EVALUATED IN TABLE
				z_hash = self.get_zorbist_hash(child)

				# if board state in board_cache and needed value exist
				if z_hash in self.board_cache and self.board_cache[z_hash][1] != None and self.board_cache[z_hash][3] != None :
					v += 1
					print("Z From cache", v)
					value = self.board_cache[z_hash][1]
					beta = self.board_cache[z_hash][3]

				# else update board cache
				else:
					value = min(value, self.minimax(child, depth - 1, player_white, alpha, beta, True))
					beta = min(beta, value)

					# update entry in board_cache
					if z_hash in self.board_cache:
						self.board_cache[z_hash][1] = value
						self.board_cache[z_hash][3] = beta

					# new entry in board_cache
					else: 
						array = [None, value, None, beta] # [max_value, min_value, alpha, beta]
						self.board_cache[z_hash] = array 

				if beta <= alpha: 
					break

		
		
			return value

# zorbist_table = [] 
# board = Board.new_board()


# for i in range(8): # width
# 		zorbist1 = []
# 		for j in range(8): # length
# 			zorbist2 = []
# 			for k in range(23): # 24 possible configuration of this position
# 				zorbist2.append(random.getrandbits(64))

# 			zorbist1.append(zorbist2)

# 		zorbist_table.append(zorbist1)



# h = 0
# for i in range(8): # width
# 	for j in range(8): # length
# 		if board.squares[i][j] != '': # True/player_white

# 			# white
# 			if board.squares[i][j].player_white:
# 				config = 0 + board.squares[i][j].size # range [0,11]
# 				h = h ^ zorbist_table[i][j][config] # XOR operartion

# 			# black
# 			else:
# 				config = 11 + board.squares[i][j].size # range [12,23]
# 				h = h ^ zorbist_table[i][j][config]  # XOR operartion

# print("hash", h)

# # boom
# new_stack = Stack(6, 6, 1, False)
# board = new_stack.boom(board)

# for i in range(8): # width
# 	for j in range(8): # length
# 		if board.squares[i][j] != '': # True/player_white

# 			# white
# 			if board.squares[i][j].player_white:
# 				config = 0 + board.squares[i][j].size # range [0,11]
# 				h = h ^ zorbist_table[i][j][config] # XOR operartion

# 			# black
# 			else:
# 				config = 11 + board.squares[i][j].size # range [12,23]
# 				h = h ^ zorbist_table[i][j][config]  # XOR operartion

# print("hash", h)
