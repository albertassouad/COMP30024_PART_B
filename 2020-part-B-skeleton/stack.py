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

	def __hash__(self):
		return hash((self.colour, self.size, self.x, self.y))



	# Creates an exact copy of this stack
	def copy_stack(self):
		return Stack(self.x, self.y, self.size, self.colour, self.parent)

	# Possible moves from this stack, represented as the new stacks that can result from it
	# Does not take into account black and white stacks already on the board
	# We do this later
	def possible_moves(self):

		new_stacks = []

		for i in range(1, self.size+1): 

			new_stacks.extend(self.up(i))
			new_stacks.extend(self.down(i))
			new_stacks.extend(self.left(i))
			new_stacks.extend(self.right(i))

		return new_stacks

	def to_string(self):
		if self.colour == "white": 
			c = "w" 
		else :
			c = "b"
		# ((x,y), size, colour)
		return "(("  + str(self.x) + "," + str(self.y) + ")," + str(self.size) + "," + c + ")"

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