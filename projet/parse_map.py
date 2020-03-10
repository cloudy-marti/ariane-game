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

lab = parse_map("maps/big/big1.txt")

def display_map(labyrinth) :
	for row in labyrinth :
		for char in row :
			print(char, end='')

# def draw_horizontal_wall(row, column, width, height, cell_number) :
# 
# def draw_vertical_wall(row, column) :

def draw_map(labyrinth, width, height) :

	margin = labyrinth.margin
	cell_number = labyrinth.cell_number
	cell_size = labyrinth.cell_size

	cree_fenetre(width+margin, height+margin)
	# rectangle(margin, margin, width, height, epaisseur=2)

	for row, line in enumerate(labyrinth.lst) :
		for column, char in enumerate(line) :
			functionDictionnary[char] (labyrinth, row, column)

	attente_clic()
	ferme_fenetre()

def apply_graphical_offset(labyrinth, position) :
	return (position / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin

def draw_vertical_wall(labyrinth, row, column) :
	start_point = []
	start_point.append(apply_graphical_offset(labyrinth, column + 1) - labyrinth.cell_size/2)
	start_point.append(apply_graphical_offset(labyrinth, row - 1))

	end_point = []
	end_point.append(apply_graphical_offset(labyrinth, column + 1) - labyrinth.cell_size/2)
	end_point.append(apply_graphical_offset(labyrinth, row + 1))

	ligne(start_point[0], start_point[1], end_point[0], end_point[1], epaisseur=2)

def draw_horizontal_wall(labyrinth, row, column) :
	start_point = []
	start_point.append(apply_graphical_offset(labyrinth, column - 1))
	start_point.append(apply_graphical_offset(labyrinth, row + 1) - labyrinth.cell_size/2)

	end_point = []
	end_point.append(apply_graphical_offset(labyrinth, column + 1))
	end_point.append(apply_graphical_offset(labyrinth, row + 1) - labyrinth.cell_size/2)

	ligne(start_point[0], start_point[1], end_point[0], end_point[1], epaisseur=2)

def draw_invisible_comma(labyrinth, row, column) :
	x = (column / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
	y = (row / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
	point(x, y, epaisseur=0)

def draw_picture(labyrinth, row, column, pathToFile) :
	x = (column / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
	y = (row / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
	image(x, y, pathToFile)

picturePathDictionnary = {
	'A' : "media/ariane.png",
	'T' : "media/thesee.png",
	'V' : "media/minoV.png",
	'H' : "media/minoH.png",
	'P' : "media/porte.png"
}

functionDictionnary = {
	'+' : lambda l,r,c : draw_invisible_comma(l,r,c),
	'\n' : lambda l,r,c : draw_invisible_comma(l,r,c),
	' ' : lambda l,r,c : draw_invisible_comma(l,r,c),
	'|' : lambda l,r,c : draw_vertical_wall(l,r,c),
	'-' : lambda l,r,c : draw_horizontal_wall(l,r,c),
	'A' : lambda l,r,c : draw_picture (l,r,c,picturePathDictionnary['A']),
	'T' : lambda l,r,c : draw_picture (l,r,c,picturePathDictionnary['T']),
	'V' : lambda l,r,c : draw_picture (l,r,c,picturePathDictionnary['V']),
	'H' : lambda l,r,c : draw_picture (l,r,c,picturePathDictionnary['H']),
	'P' : lambda l,r,c : draw_picture (l,r,c,picturePathDictionnary['P']),
}

display_map(lab.lst)
draw_map(lab, 810, 810)
# define_assets(lab.lst)
"""
	10 points jeu
	10 points solveur
"""