import copy
import pdb

def spotCalc(stack): 

	spots = set()

	x = stack.x
	y = stack.y

	for i in range(x-1, x+2):
		if i >= 0 and i <= 7:
			for j in range(y-1, y+2):
				if j >= 0 and j <= 7:
					spots.add((i,j))
	# spots.remove((x,y))


	return spots


def neighbors(squares, boomspots, done):

	neighbors = []
	# all_stacks = squares.stacks

	for i in range(8):
		for j in range(8):
			if squares[i][j] != '':
				coordinate = (squares[i][j].x, squares[i][j].y)
				if coordinate in boomspots and coordinate not in done:
					neighbors.append(squares[i][j])




	return neighbors


 # global variable


def find_boomzones(stack, squares):

	def zone_finder(stack, squares):
		# print(done)

		zones = set()
		# Find coordinates in blast radius (3x3 square around the piece)
		boomspots = spotCalc(stack)
		# print("boomspots")
		# print(boomspots)
		coordinate = (stack.x, stack.y)
		# print("done")
		done.append(coordinate)
		# print(done)
		# Find neighbors of our boomed piece
		adjacent = neighbors(squares, boomspots, done)
		# print("adjacent")
		# print(adjacent)
	

		if len(adjacent) == 0:
			# zones.extend(boomspots)
			zones.update(boomspots)
			return zones 

		zones.update(boomspots)

		for n in adjacent:

			zones.update(zone_finder(n, squares))


		return zones
	# done means we've already collected this squares boomspots
	done = []
	boomzones = set()
	boomzones.update(zone_finder(stack, squares))
	# print(boomzones)

	return boomzones