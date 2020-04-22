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