import copy
from findboomzones import final_zones

class Stack: 
	def __init__(self, x, y, size, colour, parent=None):

		self.x = x
		self.y = y
		self.size = size
		self.colour = colour
		self.parent = parent


	def array_representation(self):
		return [self.size, self.x, self.y]

	def moves(self):

		moves = []

		for i in range(1, self.size+1): 

			moves.extend(self.up(i))
			moves.extend(self.down(i))
			moves.extend(self.left(i))
			moves.extend(self.right(i))

		return moves

	def up(self, n):
		new_stacks = []
		for i in range(1, n+1):
			for j in range(1, n+1):
				new_x = self.x 
				new_y = self.y + i

				if self.onboard(new_x, new_y):
					stack = Stack(new_x, new_y, self.size, "white", self)
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
					stack = Stack(new_x, new_y, self.size, "white", self)
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
					stack = Stack(new_x, new_y, self.size, "white", self)
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
					stack = Stack(new_x, new_y, self.size, "white", self)
					new_stacks.append(stack)
				# else:
				# 	new_stack.append(None)

		return new_stacks

	def update(self, size):
		self.size += size
		if self.size == 0:
			return ''
		else:
			return self

	def onboard(self, x, y):
		if (x >= 0 and x <= 7) and (y >= 0 and y <= 7):
			return True
		return False


class Board:

	def __init__(self, whites, blacks, parent = None):



		self.board = []
		self.whites = []
		self.blacks = []
		self.parent = parent

		for i in range(8):
			row = []
			for j in range(8):
				row.append('')
			self.board.append(row)
	

		for w in whites:

			size = 1		
			x = w[0]
			y = w[1]

			self.board[x][y] = Stack(x, y, size, "white")
			self.whites.append(Stack(x, y, size, "white"))


		for b in blacks:

			size = 1
			x = b[0]
			y = b[1]

			self.board[x][y] = Stack(x, y, size, "black")
			self.blacks.append(Stack(x, y, size, "black"))

		# print(self.board)
		# print(self.whites)

	def get_tokens(self, board, colour): 
		tokens = []
		for i in range(8):
			for j in range(8):
				if isinstance(board[i][j], Stack):
					if board[i][j].colour == colour:
						tokens.append(board[i][j].array_representation())

		return tokens

	def update(self, new_stack):

		new_x = new_stack.x
		new_y = new_stack.y
		move_size = new_stack.size

		#create a new board
		new_board = copy.deepcopy(self.board)
		# print(new_board)
		new_position = new_board[new_x][new_y]

		if isinstance(new_position, Stack):
			if new_position.colour == "black":
				return None
			else: 
				new_board[new_x][new_y] = new_position.update(move_size)
		
		elif new_position == '':
			new_board[new_x][new_y] = new_stack

		# Edit old position
		# print(new_stack.array_representation())
		old_x = new_stack.parent.x

		old_y = new_stack.parent.y
		# print(old_y)


		old_position = new_board[old_x][old_y]
		# print("old")
		# print(old_position)
		# print(old_position.array_representation())

		new_board[old_x][old_y] = old_position.update(-move_size)


		whites = self.get_tokens(new_board, "white")
		# print(whites)
		blacks = self.get_tokens(new_board, "black")
		# print(blacks)


		return Board(whites, blacks, self)


	def expand(self):
		child_boards = []
		child_stacks = []

		#
		for w in self.whites:
			child_stacks.extend(w.moves())

		for s in child_stacks: 
			# new_board = self.copy()
			# new = self.update(s)
			# whites = new.whites
			child_boards.append(self.update(s))
			# blacks = new.blacks
			# Board(whites, blacks, self.board)
			# child_boards.append(new_board)

		return child_boards

	def evaluation_function(self):

		# find black (opponent) boomzones --> maximize
		black_boomzones = final_zones(self.blacks)

		# find white boomzones --> minimize
		white_boomzones = final_zones(self.whites)
		
		for stack in self.blacks: print(stack.array_representation())
		
		print(white_boomzones)

		print(black_boomzones)
		
		# most simple eval function 
		return len(self.whites) - len(self.blacks)

blacks_init = [(0,7), (1,7),   (3,7), (4,7),   (6,7), (7,7),
               (0,6), (1,6),   (3,6), (4,6),   (6,6), (7,6)]

whites_init = [(0,1), (1,1),   (3,1), (4,1),   (6,1), (7,1),
                (0,0), (1,0),   (3,0), (4,0),   (6,0), (7,0)]

board = Board(whites_init, blacks_init)
# print(board.board)
print(board.evaluation_function())


