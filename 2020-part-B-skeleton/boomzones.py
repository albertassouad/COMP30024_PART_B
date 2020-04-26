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

	








# def setCreator(zones, tokens):
# 	token_set = listToSet(tokens)
# 	sets = []
# 	for z in zones:
# 		sets.append(listToSet(z).difference(token_set))
# 	return sets


# def listToSet(listoflists):
# 	return set(tuple(i) for i in listoflists)



# def boomZones_intersection(zones):
# 	new_zones = []
# 	intersection_done = []
# 	for zone in zones:
# 		# temporary list of zones without the zone, so it does not find the intersection with itself
# 		zones_temp = copy.copy(zones)
# 		zones_temp.remove(zone)
		
# 		no_intersection = True # Flag: if there are no intersection with any other zones, just add the whole set to new_zones

# 		# check intersections with other zones
# 		for other in zones_temp:
# 			if zone & other:
# 				# if intersection not already added
# 				if (zone & other) not in new_zones:
# 					new_zones.append(zone.intersection(other))
# 				no_intersection = False

# 		# Flag: add the whole zone if there are no intersection
# 		if no_intersection: new_zones.append(zone) 

# 	return new_zones #length of new zones is the minimum number of white tokens needed

# def final_zones(tokens_input):
# 	tokens = []
# 	for token in tokens_input:
# 		tokens.append([token[1],token[2]])
# 	bz = boomzones(tokens)
# 	zones = setCreator(bz, tokens)
# 	finalbz = boomZones_intersection(zones)

# 	return finalbz

# white = [[1,0,7], [1,1,7],   [1,3,7], [1,4,7],   [1,6,7], [1,7,7],
#          [1,0,6], [1,1,6],   [1,3,6], [1,4,6],   [1,6,6], [1,7,6]]

# black = [[1,0,1], [1,1,1],   [1,3,1], [1,4,1],   [1,6,1], [1,7,1],
#          [1,0,0], [1,1,0],   [1,3,0], [1,4,0],   [1,6,0], [1,7,0]]


# print(final_zones(white))
# print(final_zones(black))




