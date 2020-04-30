import boomzones
import heapq

class Stack: 
	def __init__(self, x, y, size, colour, parent=None):

		self.x = x
		self.y = y
		# size of the stack
		self.size = size
		# colour of the stack - black or white
		self.colour = colour
		# stack from which this stack originated from
		self.parent = parent

	# Creates an exact copy of this stack
	def copy_stack(self):
		return Stack(self.x, self.y, self.size, self.colour, self.parent)

	# Possible moves from this stack, represented as the new stacks that can result from it
	# We integrate these new stacks into the board in the Board class
	def possible_moves(self, board, boomed):

		moves = []

		for i in range(1, self.size+1): 

			moves.extend(self.up(i, board))
			moves.extend(self.down(i, board))
			moves.extend(self.left(i, board))
			moves.extend(self.right(i, board))

			# Would it make sense considering boom moves 1st>?
			if (self.x, self.y) not in boomed:
				moves.append(self.boom(board, boomed))

		# moves are a list of boards
		return moves
		# return new_stacks

	# String representation of the stack
	def to_string(self):
		return str(self.size) + "," + str(self.colour)

	def flatten(self):
		if self.colour == "white":
			return self.size 
		else: 
			return -self.size

	# Call alberts function
	def boom(self, board, boomed):
		# Find all coordinates affected by booming this stack
		coordinates = boomzones.find_boomzones(self, board.squares)
		# We don
		boomed.update(coordinates)
		# Create copy of the board with copies of the Stack objects 
		new_squares = board.copy_squares()
		# Remove all stacks (stack -> '') in these coordinates
		for c in coordinates:
			# print(c)
			i = c[0]
			j = c[1]
			new_squares[i][j] = ''

		# return a new board with this layout
		return Board(new_squares)


	def up(self, n, board):
		moves = []
		# new_stacks = []
		# i is the  size of the move
		for i in range(1, n+1):
			# j is the number of tokens being moved
			for j in range(1, n+1):

				new_x = self.x 
				new_y = self.y + i
				# Make sure the piece keep the tokens on the board
				if self.onboard(new_x, new_y):
					# Create a new stack with these coordinte and size
					stack = Stack(new_x, new_y, j, self.colour, self)
					# Returns a board with this stack integrated and old stack edited
					updated = board.update_board(stack)
					# If the move was invalid (tried to move a white stack on a black stack 
					# None is returned
					if updated!= None:
						moves.append(updated)
		# return set of moves from this
		return moves

	def down(self, n, board):
		moves = []
		# new_stacks = []
		for i in range(1, n+1):
			for j in range(1, n+1):
				new_x = self.x 
				new_y = self.y - i
				
				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, j, self.colour, self)
					# new_stacks.append(stack)
					updated = board.update_board(stack)
					if updated!= None:
						moves.append(updated)

				# else:
				# 	new_stack.append(None)
		
		# return new_stacks
		return moves


	def left(self, n, board):
		moves = []

		# new_stacks = []
		for i in range(1, n+1):
			for j in range(1, n+1):
				new_x = self.x - i
				new_y = self.y

				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, j, self.colour, self)
					# new_stacks.append(stack)
					updated = board.update_board(stack)
					if updated!= None:
						moves.append(updated)

				# else:
				# 	new_stack.append(None)
		
		# return new_stacks
		return moves


	def right(self, n, board):
		moves = []
		# new_stacks = []
		for i in range(1, n+1):
			for j in range(1, n+1):
				new_x = self.x + i
				new_y = self.y
				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, j, self.colour, self)
					# new_stacks.append(stack)
					updated = board.update_board(stack)
					if updated!= None:
						moves.append(updated)

				# else:
				# 	new_stack.append(None)
		# return new_stacks
		return moves


	# Update the stack post move - add/remove tokens from it
	def update_stack(self, size):

		# The stack at this position is already a copy, we just edit its size
		self.size += size
		# If all tokens remove from the stack we return '' denoting empty square
		if self.size == 0:
			return ''
		else:
			return self


	def onboard(self, x, y):
		if (x >= 0 and x < Board.HEIGHT) and (y >= 0 and y < Board.WIDTH):
			return True
		return False




#Class that represents the board
# The board is the state
class Board:

	HEIGHT = 8
	WIDTH = 8

	# A board is initialized with the squares it consists of
	# These squares may be unoccupied, occupied by a stack of black tokens, or occupied by a stack 
	# of white tokens
	def __init__(self, squares):
		# self.parent = parent
		self.squares = squares
		# To shorten the time of iteration keep black and white tokens in lists
		# white are list of white tokens
		self.whites = self.get_stacks("white")
		# list of black tokens
		self.blacks = self.get_stacks("black")
		# self.score = self.
		# difference between white and black stacks
		# possibly remove
		# self.whites_minus_blacks = len(self.whites) - len(self.blacks)

	# Allow storage of boards in a priority queue
	def __lt__(self, other): 
		return self.whites_minus_blacks < other.whites_minus_blacks

		#self.blacks= 
		#self.whites =

	# Retrieves stacks of specified colour
	def get_stacks(self, colour):
		stacks = [] 
		for i in range(Board.HEIGHT):
			for j in range(Board.WIDTH):
				if self.squares[i][j] != '':
					if self.squares[i][j].colour == colour:
						stacks.append(self.squares[i][j])
		return stacks


	# Creates a brand new board with white and black tokes in starting positions
	def new_board():
		# blacks = [[1,0,7], [1,1,7],   [1,3,7], [1,4,7],   [1,6,7], [1,7,7],
  #        			[1,0,6], [1,1,6],   [1,3,6], [1,4,6],   [1,6,6], [1,7,6]]

  #       whites = [[1,0,1], [1,1,1], [1,3,1], [1,4,1], [1,6,1], [1,7,1], [1,0,0], [1,1,0], [1,3,0], [1,4,0], [1,6,0], [1,7,0]]

        # whites = [[1,0,1], [1,1,1],   [1,3,1], [1,4,1],   [1,6,1], [1,7,1],
        # 			[1,0,0], [1,1,0],   [1,3,0], [1,4,0],   [1,6,0], [1,7,0]]
		# initial positions of white and black tokens
		blacks = [[1,0,7], [1,1,7],   [1,3,7], [1,4,7],   [1,6,7], [1,7,7],
         			[1,0,6], [1,1,6],   [1,3,6], [1,4,6],   [1,6,6], [1,7,6]]

		whites = [[1,0,1], [1,1,1],   [1,3,1], [1,4,1],   [1,6,1], [1,7,1],
         			[1,0,0], [1,1,0],   [1,3,0], [1,4,0],   [1,6,0], [1,7,0]]

     
        # empty board with all squares ''
		squares = Board.empty_board()
		# adds white stacks to the
		for w in whites:
			x = w[1]
			y = w[2]
			# Fill this square with a white stack
			squares[x][y] = Stack(x, y, w[0], "white")
		# adds black stacks to the board
		for b in blacks:
			x = b[1]
			y = b[2]
			# Fill this square with a black stack
			squares[x][y] = Stack(x, y, b[0], "black")

		return Board(squares)
	# function to initialize an empty board
	def empty_board():
		squares = []
		for i in range(Board.HEIGHT):
			row = []
			for j in range(Board.HEIGHT):
				# '' signify squares that are unoccupied by stacks 
				row.append('')
			squares.append(row)
		return squares
	# def board_to_string(self):
	# 	for i in range()

	# Creates a copy of the squares on this board and copies of the stack on occupied squares
	def copy_squares(self):
		new_squares = []
		for i in range(Board.HEIGHT):
			row = []
			for j in range(Board.WIDTH):
				# If a stack occupies this square
				if self.squares[i][j] != '':
					# print(self.squares[i][j])
					# Create a copy of the stack that occupies that square
					row.append(self.squares[i][j].copy_stack())
				else: 
					row.append('')
			
			new_squares.append(row)
		
		return new_squares

	# The game is over if there are no more tokens of either colour
	def game_over(self):
		counts = self.counts()
		# no more tokens of either color - game has won or draw
		if counts["white"] == 0 or counts["black"] == 0:
			return True
		# If both parties have just 1 token, can only result in a draw
		elif counts["white"] == 1 and counts["black"] == 1:
			return True

		return False

	# A dictionary with black and white token counts, for the evaluation function
	def counts(self): 
		counts = dict()
		counts["white"] = 0
		counts["black"] = 0 

		for stack in self.whites:
			counts["white"] += stack.size

		for stack in self.blacks:
			counts["black"] += stack.size

		# for i in range(8):
		# 	for j in range(8):
		# 		if self.squares[i][j] != '':
		# 			# Counts size of stacks
		# 			counts[self.squares[i][j].colour] += self.squares[i][j].size
		return counts



	# Takes the new stack generated by a move, and creates a new board with 
	# that move taken into account
	def update_board(self, new_stack):
		# Position of the new stack
		new_x = new_stack.x
		new_y = new_stack.y
		# Size of the new stack
		tokens_moved = new_stack.size
		# Copy board just returns the squares of stacks on the board
		# New squares stores the layout of the old board
		new_squares = self.copy_squares()
		# Postion that new stack will occupy
		# We check this position to see whats in it
		new_position = new_squares[new_x][new_y]
		# Check if the position is already occupied
		if new_position != '':
		# If the position is occupied by a stack of a different colour, we abandon the move 
			if new_position.colour != new_stack.colour:
			# if new_position.colour == "black":
				return None
		# If the position is occupied by a white stack, we add our new stack to that stack
			else: 
				# new position is alreadya copy
				new_squares[new_x][new_y] = new_position.update_stack(tokens_moved)
		# If the position is unoccupied assign our new stack to it
		else:

			new_squares[new_x][new_y] = new_stack

		# Edit the position this stack has moved from
		# We check the parent stack to see the previous position of this new stack
		old_x = new_stack.parent.x
		old_y = new_stack.parent.y
		# As new_squares is the layout of the old board, we have to update this position
		old_position = new_squares[old_x][old_y]
		# print("old")
		# print(old_position)
		# print(old_position.array_representation())

		# Subtract the number of tokens that were moved from that position stack
		new_squares[old_x][old_y] = old_position.update_stack(-tokens_moved)


		return Board(new_squares)


	# Create all the possible board arrangements that can result from this board
	def possible_moves(self, colour, maximizingPlayer):
		# Use priority queue for possible moves
		# sorted_moves = []
		# moves stores child board arrangements
		# boom_moves = []
		moves = []
		# heapq.heapify(moves)
		# every time we generate moves for a board we have empty boomed set
		boomed = set()
		# new_stacks = []
		# All stacks that will be produced by our moves
		# 
		if colour == "white":
			stacks_moved = self.whites
		elif colour == "black":
			stacks_moved = self.blacks

		# Create a list of every resulting board from every move for each stack
		for stack in stacks_moved: 
			moves.extend(stack.possible_moves(self, boomed))
			# for board in stack.possible_moves(self, boomed):
			# 	heapq.heappush(moves, board)

			# if [stack.x, stack.y] not in boomed:
			# moves.extend(stack.possible_moves(self, boomed))
		if maximizingPlayer:
			moves.sort(key=lambda x: x.evaluation(colour), reverse=True)
			return moves
		else:
			moves.sort(key=lambda x: x.evaluation(colour), reverse=False)
			return moves

	def flatten(self, reverse=False): 
		flattened = []
		if reverse:
			squares = self.squares[::-1]

		for row in self.squares[::-1]:
			for entry in row:
				if entry == '':
					flattened.append(13)
				else:
					flattened.append(entry.flatten())
		return flattened


	def hashkey(self):
		k1 = 0 
		k2 = 0

		for x in self.flatten():
			k1 *= 3
			k1 += int(x)
			assert k1 >= 0

		for x in self.flatten(True):
			k2 *= 3
			k2 += int(x)
			assert k2 >= 0

		if k2 < k1:
			return k2, True
		else:
			return k1, False

		# return moves


		# if colour == "white":
		# 	return list(heapq.heapify(moves))

		# elif colour == "black":
		# 	return moves


	# Evaluation function will depend on what colour we are
	# simple evaluation function 
	def evaluation(self, player_white):
		# print(board)
		# squares_to_string(board.squares)

		# black_eval = 0
		# white_eval = 0
		score = 0

		values = [[1,1,1,1,1,1,1,1],
					[1,1,1,1,1,1,1,1],
					[2,2,2,2,2,2,2,2],
					[3,3,3,3,3,3,3,3],
					[3,3,3,3,3,3,3,3],
					[2,2,2,2,2,2,2,2],
					[1,1,1,1,1,1,1,1],
					[1,1,1,1,1,1,1,1]]

		white_counts = 0
		black_counts = 0

		for i in range(Board.HEIGHT):
			for j in range(Board.WIDTH):
				if self.squares[i][j] != '':
					if self.squares[i][j].colour == "white":
						white_counts += 100*self.squares[i][j].size + values[j][i]
						# score += values[j][i]
						# score += 10 * self.squares[i][j].size + values[j][i]
					else:
						# score -= 10 * self.squares[i][j].size + values[j][i]
						black_counts += 100*self.squares[i][j].size + values[j][i]
						# score -= values[j][i]


		# score += diff 

		if player_white: 
			return white_counts - black_counts
			# return score
		else:
			return black_counts - white_counts
			# return -score

		# return diff

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

class TranspositionTable:

	WHITE_STACK = -1
	BLACK_STACK = 2

	def __init__(self, maxitems = 100000):
		self.maxitems = maxitems
		self.cache = OrderedDict(0)

	def put(self, board, depth, score):
		entry = Entry(move, depth, int(score), state)

# chosen_move = best_move(board, player_white)


def squares_to_string(squares):
	for i in range(7,-1, -1):
		row = "["
		for j in range(8):
			if squares[j][i] != '':
				row += squares[j][i].to_string() + " "
			else: 
				row += "empty   "
		row += "]"
		print(row)


board = Board.new_board()
# squares_to_string(board.squares)
# # print(board.evaluation(True))
# # print("-------------------------")
# for new_board in board.possible_moves("white"):
# 	print(new_board.evaluation(True))

# max_list = board.possible_moves("white", True)
# min_list = board.possible_moves("white", False)

# for move in max_list: 
# 	print(move.evaluation(True))
# print("breka")
# for move in min_list: 
# 	print(move.evaluation(True))

# move_list.sort(key=lambda x: x.evaluation(True), reverse=True)
# for m in move_list:
# 	print(m.evaluation(True))
# 	squares_to_string(new_board.squares)
# 	print(new_board.evaluation(True))


white = AI(board, True)
black = AI(board, False)

squares_to_string(board.squares)
# print(board.hashkey())
print("-------------------------")

moves = 0
while moves < 10:
	if moves % 2 == 0:
		chosen_move = white.best_move()
		# chosen_move = white.board.possible_moves("white")[randint(0,100)]
		print("Turn " + str(white.turn))
		# print(chosen_move.evaluation(True))
		squares_to_string(chosen_move.squares)
		# print(len(white.board.whites))
		# print(len(white.board.blacks))
		print("-------------------------")
		# print(chosen_move.)
		white.board = chosen_move
		black.board = chosen_move
		# white.board = Board(chosen_move.squares)
		# black.board = Board(chosen_move.squares)
		white.turn += 1
		black.turn += 1
		# turn += 1
		# white.board.squares = Board.copy_squares(chosen_move.squares)
		# black.board.squares = Board.copy_squares(chosen_move.squares)
	else:
		chosen_move = black.best_move()
		# chosen_move = black.board.possible_moves("black")[randint(0,30)]
		print("Turn " + str(white.turn))
		# print(chosen_move.evaluation(False))
		squares_to_string(chosen_move.squares)
		# print(len(white.board.whites))
		# print(len(white.board.blacks))
		print("-------------------------")
		white.board = chosen_move
		black.board = chosen_move
		# white.board = Board(chosen_move.squares)
		# black.board = Board(chosen_move.squares)
		# print(len(white.board.whites))
		# print(len(white.board.blacks))
		white.turn += 1
		black.turn += 1
		# white.board.squares =  Board.copy_squares(chosen_move.squares)
		# black.board.squares =  Board.copy_squares(chosen_move.squares)
	
	moves +=1



# board = Board.new_board()
# for move in board.possible_moves("white"):













