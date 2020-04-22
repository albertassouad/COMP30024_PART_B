import copy
import pdb

def spotCalc(black):
	#fix up to exclude spots in tokens
	spots = []
	x = black[0]
	y = black[1]

	for i in range(x-1, x+2):
		if i >= 0 and i <= 7:
			for j in range(y-1, y+2):
				if j >= 0 and j <= 7:
					spots.append([i,j])
	spots.remove([x,y])


	return spots


def neighbors(tokens, black, boomspots):
	neighbors = []
	for b in tokens:
		if b in boomspots and b != black and b not in done:
			neighbors.append(b)

	return neighbors


done = [] # global variable
def zonesearch(black, tokens):
	boomzones = []
	#adjacent is [2,2]
	boomspots = spotCalc(black)
	adjacent = neighbors(tokens, black, boomspots)
	# print(black)
	# print(adjacent)
	# print(len(adjacent))
	if len(adjacent) == 0:
		boomzones.extend(boomspots)
		done.append(black)
		return boomzones
	
	boomzones.extend(boomspots)
	#print(boomzones)
	done.append(black)
	#print(done)
	for n in adjacent:
		boomzones.extend(zonesearch(n, tokens))
	#print(boomzones)
	return boomzones

def boomzones(tokens):
	zones = []
	for b in tokens:
		if b not in done:
			zones.append(zonesearch(b, tokens))
	return zones

def setCreator(zones, tokens):
	token_set = listToSet(tokens)
	sets = []
	for z in zones:
		sets.append(listToSet(z).difference(token_set))
	return sets


def listToSet(listoflists):
	return set(tuple(i) for i in listoflists)



def boomZones_intersection(zones):
	new_zones = []
	intersection_done = []
	for zone in zones:
		# temporary list of zones without the zone, so it does not find the intersection with itself
		zones_temp = copy.copy(zones)
		zones_temp.remove(zone)
		
		no_intersection = True # Flag: if there are no intersection with any other zones, just add the whole set to new_zones

		# check intersections with other zones
		for other in zones_temp:
			if zone & other:
				# if intersection not already added
				if (zone & other) not in new_zones:
					new_zones.append(zone.intersection(other))
				no_intersection = False

		# Flag: add the whole zone if there are no intersection
		if no_intersection: new_zones.append(zone) 

	return new_zones #length of new zones is the minimum number of white tokens needed

def final_zones(tokens_input):
	tokens = []
	for token in tokens_input:
		tokens.append([token.x,token.y])
	bz = boomzones(tokens)
	zones = setCreator(bz, tokens)
	finalbz = boomZones_intersection(zones)

	return finalbz

