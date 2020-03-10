from upemtk import *
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

# def draw_horizontal_wall(row, column, width, height, cell_number) :
# 
# def draw_vertical_wall(row, column) :

def draw_map(labyrinth, width, height) :

	margin = 5

	cell_number = labyrinth.size
	cell_size = width / cell_number

	cree_fenetre(width+margin, height+margin)
	rectangle(margin, margin, width, height, epaisseur=2)

	for i, row in enumerate(labyrinth.lst) :
		for j, char in enumerate(row) :
			x = (i/2*width/cell_number) + margin
			y = (j/2*height/cell_number) + margin
			if char == '|' :
				ligne(x, y, x, y + cell_size, epaisseur=2)
			# if char == '-' :
			# 	ligne(x, y, x + cell_size, y, epaisseur=2)
			if char == '+' :
				point(x, y, epaisseur=5)
				if(row[i+1] == '-') :
					ligne(x, y, x + cell_size, y, epaisseur=2)
				if(labyrinth.lst[i][j+1] == '|') :
					ligne(x + cell_size, y, x + cell_size, y + cell_size, epaisseur=2)

	attente_clic()
	ferme_fenetre()


# def define_assets(labyrinth) :
# 	minotaur = []
# 	wall = []
# 	for row,line in enumerate(labyrinth) :
# 		for column,char in enumerate(line) :
# 			#print("row = {0} and column = {1}".format(row, column))
# 			if char == 'A' :
# 				# Ariane
# 				ariane = Ariane(row, column)
# 			elif char == 'T' :
# 				# Thésée
# 				thesee = Thesee(row, column)
# 			elif char == 'V' :
# 				# vertical minotaur
# 				minotaur.append('v', row, column)
# 			elif char == 'H' :
# 				# horizontal minotaur
# 				minotaur.append('h', row, column)
# 			elif char == '|' :
# 				# vertical wall
# 				wall.append(row, column)
# 			elif char == '-' :
# 				# horizontal wall
# 				wall.append(row, column)
# 			elif char == "+" :
# 				# intersection
# 				wall.append(row, column)
# 			elif char == 'P' :
# 				end = EndGame(row, column)
# 				# door
# 			else :
# 				print("bye")
# 				# do nothing

display_map(lab.lst)
draw_map(lab, 800, 800)
# define_assets(lab.lst)
"""
	10 points jeu
	10 points solveur
"""