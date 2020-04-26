import copy
import boomzones
import minmax

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
	def possible_moves(self):

		new_stacks = []

		for i in range(1, self.size+1): 

			new_stacks.extend(self.up(i))
			new_stacks.extend(self.down(i))
			new_stacks.extend(self.left(i))
			new_stacks.extend(self.right(i))

		return new_stacks

	def to_string(self):
		return str(self.size) + "," + str(self.colour)

	def up(self, n):
		new_stacks = []
		# i is the  size of the move
		for i in range(1, n+1):
			# j is the number of tokens being moved
			for j in range(1, n+1):

				new_x = self.x 
				new_y = self.y + i
				# Make sure the piece keep the tokens on the board
				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, j, self.colour, self)
					new_stacks.append(stack)
				# else:
				# 	new_stack.append(None)
		return new_stacks

	def down(self, n):
		new_stacks = []
		for i in range(1, n+1):
			for j in range(1, n+1):
				new_x = self.x 
				new_y = self.y - i
				
				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, j, self.colour, self)
					new_stacks.append(stack)
				# else:
				# 	new_stack.append(None)
		
		return new_stacks

	def left(self, n):

		new_stacks = []
		for i in range(1, n+1):
			for j in range(1, n+1):
				new_x = self.x - i
				new_y = self.y

				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, j, self.colour, self)
					new_stacks.append(stack)
				# else:
				# 	new_stack.append(None)
		
		return new_stacks

	def right(self, n):
		new_stacks = []
		for i in range(1, n+1):
			for j in range(1, n+1):
				new_x = self.x + i
				new_y = self.y
				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, j, self.colour, self)
					new_stacks.append(stack)
				# else:
				# 	new_stack.append(None)
		return new_stacks

	# Update the stack post move - add/remove tokens from it
	def update_stack(self, size):

		# The stack at this position is already a copy, we just edit its size
		self.size += size

		if self.size == 0:
			return ''
		else:
			return self


	def onboard(self, x, y):
		if (x >= 0 and x < Board.HEIGHT) and (y >= 0 and y < Board.WIDTH):
			return True
		return False

	def __eq__(self, other):
		if isinstance(other, str):
			return False
		return (
				self.x == other.x and
				self.y == other.y and
				self.size == other.size and 
				self.colour == other.colour
				)

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

		#self.blacks= 
		#self.whites =

	# Creates a brand new board with white and black tokes in starting positions
	def new_board():
		# initial positions of white and black tokens
		blacks = [[1,0,7], [1,1,7],   [1,3,7], [1,4,7],   [1,6,7], [1,7,7],
         			[1,0,6], [1,1,6],   [1,3,6], [1,4,6],   [1,6,6], [1,7,6]]

		whites = [[1,0,1], [1,1,1],   [1,3,1], [1,4,1],   [1,6,1], [1,7,1],
         			[1,0,0], [1,1,0],   [1,3,0], [1,4,0],   [1,6,0], [1,7,0]]

  #       whites = [[1,0,7], [1,1,7],   [1,3,7], [1,4,7],   [1,6,7], [1,7,7],
  #       			[1,0,6], [1,1,6],   [1,3,5], [1,4,6],   [1,6,6], [1,7,6]]

		# blacks = [[1,0,1], [1,1,1],   [1,3,1], [1,4,3],   [1,6,1], [1,7,1],
  #        			[1,0,0], [1,1,0],   [1,3,0], [1,4,0],   [1,6,0], [1,7,0]]

        	# whites = [[1,0,7], [1,1,7],   [1,3,7], [1,4,7],   [1,6,7], [1,7,7],
  #        			[1,0,6], [1,1,6],   [1,3,6], [1,4,6],   [1,6,6], [1,7,6]]

		# blacks = [[1,0,1], [1,1,1],   [1,3,1], [1,4,1],   [1,6,1], [1,7,1],
  #        			[1,0,0], [1,1,0],   [1,3,0], [1,4,0],   [1,6,0], [1,7,0]]

        # Crate empty array to store representation of the board
		squares = []
		# Intilize all squares to ''
		for i in range(Board.HEIGHT):
			row = []
			for j in range(Board.HEIGHT):
				# '' signify squares that are unoccupied by stacks 
				row.append('')
			squares.append(row)
		# Populate squares with stacks
		for w in whites:
			x = w[1]
			y = w[2]
			# Fill this square with a white stack
			squares[x][y] = Stack(x, y, w[0], "white")
		
		for b in blacks:
			x = b[1]
			y = b[2]
			# Fill this square with a black stack
			squares[x][y] = Stack(x, y, b[0], "black")

		return Board(squares)

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
					# Create a copy of the stack that occupies that square
					row.append(self.squares[i][j].copy_stack())
				else: 
					row.append('')
			
			new_squares.append(row)
		
		return new_squares

	# The game is over if there are no more tokens of either colour
	def game_over(self):
		counts = self.counts()
		if counts['white'] == 0 or counts['black'] == 0:
			return True
		return False

	# A dictionary with black and white token counts, for the evaluation function
	def counts(self): 
		counts = dict()
		counts['white'] = 0
		counts['black'] = 0 

		for i in range(8):
			for j in range(8):
				if self.squares[i][j] != '':
					# Counts size of stacks
					counts[self.squares[i][j].colour] += self.squares[i][j].size
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

		# Get stacks
		# stacks = self.get_stacks(new_stacks)

		# return Board(new_stacks)
		return new_squares

	def boom(self, stack):
		# Find all coordinates affected by booming this stack
		coordinates = boomzones.find_boomzones(stack, self.squares)
		# print(coordinates)
		# Add the coordinate of the boomed stack
		# coordinates = coordinates.append((stack.x, stack.y])
		# Create copy of the board with copies of the Stack objects 
		new_squares = self.copy_squares()
		# Remove all stacks (stack -> '') in these coordinates
		for c in coordinates:
			# print(c)
			i = c[0]
			j = c[1]
			new_squares[i][j] = ''

		# return Board(new_stacks)
		return new_squares

	# Create all the possible board arrangements that can result from this board
	def possible_moves(self, colour):
		# Use priority queue for possible moves
		# sorted_moves = []
		# moves stores child board arrangements
		boom_moves = []
		moves = []
		new_stacks = []
		# All stacks that will be produced by our moves
		for i in range(Board.HEIGHT):
			for j in range(Board.WIDTH):
				if self.squares[i][j] != '':
					if self.squares[i][j].colour == colour:
						# Adds possible moves from the stack on this square
						# Moves are in the form of board layouts
						new_stacks.extend(self.squares[i][j].possible_moves())
						# Add board layouts that result from detonating given stack
						boom_moves.append(self.boom(self.squares[i][j]))
						new_move = self.boom(self.squares[i][j])
						# Checks if this board layout from given boom move is already in moves 
						# array
						if not self.check_added(moves, new_move):
							moves.append(new_move)

		for stack in new_stacks:
			# Create a board from each new board layout
			new_board = self.update_board(stack)
			# Ignores invalid moves 'None'
			if new_board != None:
				# moves array stores all new boards
				moves.append(new_board)
		# Adds all new boards from boom_moves after this
		for new_move in boom_moves:
			if not self.check_added(moves, new_move):
					moves.append(new_move)


		return moves


	def check_added(self, moves, new_move): 
		for old_move in moves:
			if self.check_equality(old_move, new_move):
				return True
		return False

	def check_equality(self, old_move, new_move):
		for i in range(8):
			for j in range(8):
				if old_move[i][j] != new_move[i][j]:
					return False
		return True

	# def adjacent(self):
	# 	for 


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

		
		if counts[my_colour] == 0:
			return -1000
		elif counts[opp_colour] == 0:
			return 10000

		else:
			diff = n_whites - n_blacks

			if player_white:
				return diff
				# return eval_sum
			else:
				# return -eval_sum
				return -diff

# chosen_move = best_move(board, player_white)


def squares_to_string(squares):
	for i in range(7,-1, -1):
		row = "["
		for j in range(8):
			if squares[j][i] != '':
				row += squares[j][i].to_string() + " "
			else: 
				row += "empty "
		row += "]"
		print(row)



board = Board.new_board()

white = AI(board, True)
black = AI(board, False)

moves = 0
while moves < 10:
	if moves % 2 == 0:
		chosen_move = white.best_move()
		squares_to_string(chosen_move)
		print("-------------------------")
		white.board.squares = chosen_move
		black.board.squares = chosen_move
	else:
		# chosen_move = black.best_move()
		chosen_move = black.board.possible_moves("black")[14]
		squares_to_string(chosen_move)
		print("-------------------------")
		white.board.squares = chosen_move
		black.board.squares = chosen_move
	
	moves +=1















