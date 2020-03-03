from Labyrinth import *

def parse_line(line) :
	# parse one line
	lst = []
	for char in line :
		lst.append(char)
	return lst;

def parse_map(pathToFile) :
	# open the file and read through it line by line
	# ensure that the file is closed at the end with the keyword 'with'
	labyrinthMap = []
	with open(pathToFile, 'r') as fp : 
		size = int(fp.readline())
		for line in fp :
			labyrinthMap.append(parse_line(line))

	labyrinth = Labyrinth(size, labyrinthMap)
	return labyrinth

lab = parse_map("maps/labyrinthe1.txt")
# print(lab.lst)

def display_map(labyrinth) :
	for row in labyrinth :
		for char in row :
			print(char, end='')

def define_assets(labyrinth) :
	minotaur = []
	wall = []
	for row,line in enumerate(labyrinth) :
		for column,char in enumerate(line) :
			print("row = {0} and column = {1}".format(row, column))
		if char == 'A' :
			# Ariane
			ariane = Ariane(row, column)
		elif char == 'T' :
			# Thésée
			thesee = Thesee(row, column)
		elif char == 'V' :
			# vertical minotaur
			minotaur.append('v', row, column)
		elif char == 'H' :
			# horizontal minotaur
			minotaur.append('h', row, column)
		elif char == '|' :
			# vertical wall
			wall.append(row, column)
		elif char == '-' :
			# horizontal wall
			wall.append(row, column)
		elif char == "+" :
			# intersection
			wall.append(row, column)
		elif char == 'P' :
			end = EndGame(row, column)
			# door
		else :
			print("bye")
			# do nothing


display_map(lab.lst)
define_assets(lab.lst)
"""
	10 points jeu
	10 points solveur
"""