# import boomzones
# from board import Board
# class Stack: 
# 	def __init__(self, x, y, size, player_white, parent=None):

# 		self.x = x
# 		self.y = y
# 		# size of the stack
# 		self.size = size
# 		self.player_white = player_white
# 		# stack from which this stack originated from
# 		self.parent = parent

# 	# Creates an exact copy of this stack
# 	def copy_stack(self):
# 		return Stack(self.x, self.y, self.size, self.player_white, self.parent)

# 	# Possible moves from this stack, represented as the new stacks that can result from it
# 	# We integrate these new stacks into the board in the Board class
# 	# def possible_moves(self, board, boomed, terminal=False):
# 	def possible_moves(self, board, boomed):

# 		moves = []

# 		for i in range(1, self.size+1): 
# 			# there is an up, down, left, right and boommove for each stack
# 			moves.extend(self.up(i, board))
# 			moves.extend(self.down(i, board))
# 			moves.extend(self.left(i, board))
# 			moves.extend(self.right(i, board))
# 			# if this tack has already been boomed for the given move
# 			if (self.x, self.y) not in boomed:
# 				moves.append(self.boom(board, boomed))

# 		# moves are a list of boards
# 		return moves
# 		# return new_stacks

# 	# String representation of the stack
# 	# eg 2,black 
# 	def to_string(self):
# 		if self.player_white == True:
# 			colour = "white"
# 		elif self.player_white == False:
# 			colour = "black"

# 		# return str(self.size) + "," + str(self.player_white)
# 		return str(self.size) + "," + colour


# 	def boom(self, board, boomed = None):
# 		# Find all coordinates affected by booming this stack
# 		coordinates = boomzones.find_boomzones(self, board.squares)
# 		# Add affected coordinate to boomed
# 		boomed.update(coordinates)
# 		# Create copy of the board with copies of the Stack objects 
# 		new_squares = board.copy_squares()
# 		# Remove all stacks (stack -> '') in these coordinates
# 		for c in coordinates:
# 			# print(c)
# 			i = c[0]
# 			j = c[1]
# 			new_squares[i][j] = ''

# 		# return a new board with this layout
# 		return Board(new_squares, boom_at = (self.x, self.y))


# 	def up(self, n, board):
# 		moves = []
# 		# new_stacks = []
# 		# i is the  size of the move
# 		for i in range(1, n+1):
# 			# j is the number of tokens being moved
# 			for j in range(1, n+1):

# 				new_x = self.x 
# 				new_y = self.y + i
# 				# Make sure the piece keep the tokens on the board
# 				if self.onboard(new_x, new_y):
# 					# Create a new stack with these coordinte and size
# 					# self denotes parent of the stack we used to get here
# 					stack = Stack(new_x, new_y, j, self.player_white, self)
# 					# Returns a board with this stack integrated and old stack edited
# 					# if not terminal:
# 					#Create a board out of this stack
# 					updated = board.update_board(stack)
# 					# If the move was invalid (tried to move a white stack on a black stack 
# 					# None is returned
# 					# We never have Nones in our move array - because they're never added
# 					if updated!= None:
# 						moves.append(updated)
# 		# return set of moves from this
# 		return moves

# 	def down(self, n, board):
# 		moves = []
# 		# new_stacks = []
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				new_x = self.x 
# 				new_y = self.y - i
				
# 				if self.onboard(new_x, new_y):
# 					stack = Stack(new_x, new_y, j, self.player_white, self)
# 					# new_stacks.append(stack)
					
# 					updated = board.update_board(stack)

# 					# updated = board.update_board(stack)
# 					if updated!= None:
# 						moves.append(updated)

# 				# else:
# 				# 	new_stack.append(None)
		
# 		# return new_stacks
# 		return moves


# 	def left(self, n, board):
# 		moves = []

# 		# new_stacks = []
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):

# 				new_x = self.x - i
# 				new_y = self.y

# 				if self.onboard(new_x, new_y):
# 					stack = Stack(new_x, new_y, j, self.player_white, self)
# 					# new_stacks.append(stack)
# 					updated = board.update_board(stack)
					
# 					if updated != None:
# 						moves.append(updated)

# 				# else:
# 				# 	new_stack.append(None)
		
# 		# return new_stacks
# 		return moves


# 	def right(self, n, board):
# 		moves = []
# 		# new_stacks = []
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				new_x = self.x + i
# 				new_y = self.y
# 				if self.onboard(new_x, new_y):
# 					stack = Stack(new_x, new_y, j, self.player_white, self)
# 					# new_stacks.append(stack)
# 					updated = board.update_board(stack)
	

# 					if updated!= None:
# 						moves.append(updated)

# 				# else:
# 				# 	new_stack.append(None)
# 		# return new_stacks
# 		return moves


# 	# Update the stack post move - add/remove tokens from it
# 	def update_stack(self, size):

# 		# The stack at this position is already a copy, we just edit its size
# 		self.size += size
# 		# If all tokens remove from the stack we return '' denoting empty square
# 		if self.size == 0:
# 			return ''
# 		else:
# 			return self


# 	def onboard(self, x, y):
# 		if (x >= 0 and x < 8) and (y >= 0 and y < 8):
# 			return True
# 		return False

