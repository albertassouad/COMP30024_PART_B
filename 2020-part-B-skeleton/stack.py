class Stack: 
	def __init__(self, x, y, size, colour, parent=None):

		self.x = x
		self.y = y
		# size of the stack
		self.size = size
		# colour of the stack - True (white) or False (black)
		self.colour = colour
		# stack from which this stack originated from
		self.parent = parent

	def __hash__(self):
		return hash((self.colour, self.size, self.x, self.y))



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
		if self.colour == True: 
			c = "w" 
		else :
			c = "b"
		# ((x,y), size, colour)
		return "(("  + str(self.x) + "," + str(self.y) + ")," + str(self.size) + "," + c + ")"

	def flatten(self):
		if self.colour == True:
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