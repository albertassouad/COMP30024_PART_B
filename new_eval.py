#COPY PASTE INTO AI CLASS
def how_deep(self):
		if self.turn <= 8:
			return 0
		elif self.board.token_count < 5:
			return 2
		else:
			return 1


#COPY PASTE INTO BOARD CLASS

def neighbours(self, stack):

		count = 0
		x = stack.x
		y = stack.y
		for i in range(x-1, x+2):
			if i >= 0 and i <= 7:
				for j in range(y-1, y+2):
					if j >= 0 and j <= 7:
						if self.squares[i][j] != '' and (i,j) != (x, y):
							if self.squares[i][j].player_white == stack.player_white:
								# count += 1
								count += self.squares[i][j].size
		return count

	def manhattan(self, stack1, stack2):
		return abs(stack1.x - stack2.x) + abs(stack1.y - stack2.y)

	def evaluation(self, player_white):

		values = [[0,0,0,0,0,0,0,0],
					[1,1,1,1,1,1,1,1],
					[2,2,2,2,2,2,2,2],
					[2,3,3,3,3,3,3,2],
					[2,3,3,3,3,3,3,2],
					[2,2,2,2,2,2,2,2],
					[1,1,1,1,1,1,1,1],
					[0,0,0,0,0,0,0,0]]

		white_score = 0 
		black_score = 0

		best_white = None
		max_white = 0
		
		best_black = None
		max_black = 0
		# neighbour_dict = {}
		white_moves = 0 
		black_moves = 0

		white_neighbours = 0
		black_neighbours = 0

		white_dist = 0 
		black_dist = 0

		n_whites = 0
		n_blacks = 0

		for s in self.stack_list:
			n = self.neighbours(s)
			if s.player_white:
				n_whites += s.size
				white_neighbours += n
				if best_white == None:
					best_white = s
				if n >= max_white:
					max_white = n
					best_white = s
				if s.size == 1:
					white_moves += s.size*values[s.y][s.x]
				else:
					white_moves += 2 * values[s.y][s.x]
			else:
				n_blacks += s.size
				black_neighbours += n
				if best_black == None:
					best_black = s
				if n >= max_black:
					max_black = n
					best_black = s
				if s.size == 1:
					black_moves += s.size*values[s.y][s.x]
				else:
					black_moves += 2 * values[s.y][s.x]

		if n_whites == 0 and n_blacks == 0:
			white_score = black_score == 0
		elif n_whites != 0 and n_blacks == 0:
			white_score = 100000000000000000
		elif n_whites == 0 and n_blacks != 0:
			black_score = 100000000000000000
		else:
			for s in self.stack_list: 

				if s.player_white == True:
					white_dist += self.manhattan(s, best_black)
				elif s.player_white == False:
					black_dist += self.manhattan(s, best_white)

			white_score += 1000*n_whites
			black_score += 1000*n_blacks

			white_score -= white_dist/n_whites
			black_score -= black_dist/n_whites

			white_score += white_moves
			black_score += black_moves

			white_score -= white_neighbours/n_whites
			black_score -= black_neighbours/n_blacks

		if player_white == True:
			return (white_score - black_score)
			# return white_score - black_score
		elif player_white == False:
			return (black_score - white_score)
