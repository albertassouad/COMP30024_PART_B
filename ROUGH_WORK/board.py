import copy

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

		# self.whites = stack_representation(whites)
		# self.blacks = stack_representation(blacks)


		self.board = []
		#store whites for expansion
		self.whites = []
		# self.blacks = []
		self.parent = parent

		for i in range(8):
			row = []
			for j in range(8):
				row.append('')
			self.board.append(row)
	

		for w in whites:

			size = w[0]		
			x = w[1]
			y = w[2]

			self.board[x][y] = Stack(x, y, size, "white")

			self.whites.append(Stack(x, y, size, "white"))

		for b in blacks:

			size = w[0]
			x = w[1]
			y = w[2]

			self.board[x][y] = Stack(x, y, size, "black")

			# self.blacks.append(Stack(x, y, size, "black"))

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

	# def expand(self):
	# 	children = []
	# 	for i in range(8):
	# 		for j in range(8):
	# 			if isinstance(board[i][j], Token) and board[i][j].colour == 'white':
	# 				for m in board[i][j].moves():
	# 						self.board.append(row)



	# 	children.append(Board(whites, self.blacks))

	def expand(self):
		child_boards = []
		child_stacks = []

		#
		for w in self.whites:
			child_stacks.extend(w.moves())


		[0,7] -> [1,7]
		for s in child_stacks: 
			# new_board = self.copy()
			# new = self.update(s)
			# whites = new.whites
			child_boards.append(self.update(s))
			# blacks = new.blacks
			# Board(whites, blacks, self.board)
			# child_boards.append(new_board)

		return child_boards

whites = [[1,0,7], [1,1,7],   [1,3,7], [1,4,7],   [1,6,7], [1,7,7],
         [1,0,6], [1,1,6],   [1,3,6], [1,4,6],   [1,6,6], [1,7,6]]

blacks = [[1,0,1], [1,1,1],   [1,3,1], [1,4,1],   [1,6,1], [1,7,1],
         [1,0,0], [1,1,0],   [1,3,0], [1,4,0],   [1,6,0], [1,7,0]]

board = Board(whites, blacks)
print(board.board)


# for b in board.whites:
# 	print(b.array_representation())
# print("------------------------------------------------------------------------------")
# children = board.expand()
# print(len(children))
# for c in children:
# 	print(c.array_representation())






	# def update():


	# def stack_representation(tokens) 




# for white in whites:
# 	print(actions(whites))


# def actions(coordinate):

# 	size = coordinate[0]
# 	actions = []
# 	for i in range(1, size+1): 
# 		actions.extend(self.up(coordinate, i))
# 		actions.extend(self.down(coordinate, i))
# 		actions.extend(self.left(coordinate, i))
# 		actions.extend(self.right(coordinate,i))
# 	return actions



# def up(token, n):
# 		actions = []
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				up = [i, token[1], token[2] + j]
# 				if self.onboard(up) and not self.black_token(up):
# 					stack = [[token[0] - i, token[1], token[2]]]
# 					stack.append(up)
# 					actions.append(Move(stack, up, token, i))
		
# 		return actions

# 	def down(token, n):
# 		actions = []
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				down = [i, token[1], token[2] - j]
# 				if self.onboard(down) and not self.black_token(down):
# 					stack = [[token[0] - i, token[1], token[2]]]
# 					stack.append(down)
# 					actions.append(Move(stack, down, token, i))

# 		return actions


# 	def left(token, n):
# 		actions = []
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				left = [i, token[1] - j, token[2]]
# 				if self.onboard(left) and not self.black_token(left):
# 					stack = [[token[0] - i, token[1], token[2]]]
# 					stack.append(left)
# 					actions.append(Move(stack, left, token, i))

# 		return actions


# 	def right(self, token, n):
# 		actions = []
# 		for i in range(1, n+1):
# 			for j in range(1, n+1):
# 				right = [i, token[1] + j, token[2]]
# 				if self.onboard(right) and not self.black_token(right):
# 					stack = [[token[0] - i, token[1], token[2]]]
# 					stack.append(right)
# 					actions.append(Move(stack, right, token, i))

# 		return actions



