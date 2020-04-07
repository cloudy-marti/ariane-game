from projet.src.utils.upemtk import *


def display_map(labyrinth):
    for row in labyrinth:
        for char in row:
            print(char, end='')
        print('\n')


def draw_map(labyrinth):
    for row, line in enumerate(labyrinth.lst):
        for column, char in enumerate(line):
            functionDictionary[char](labyrinth, row, column)
    draw_door(labyrinth)


def draw_door(labyrinth):
    row = labyrinth.end_point_row
    column = labyrinth.end_point_column
    if labyrinth.lst[row][column] == 'P' or labyrinth.lst[row][column] == ' ':
        draw_picture(labyrinth, row, column, picturePathDictionary['P'])
    elif labyrinth.lst[row][column] == 'A':
        draw_picture(labyrinth, row, column, picturePathDictionary['C'])
    elif labyrinth.lst[row][column] == 'V':
        draw_picture(labyrinth, row, column, picturePathDictionary['W'])
    elif labyrinth.lst[row][column] == 'H':
        draw_picture(labyrinth, row, column, picturePathDictionary['I'])


def apply_graphical_offset(labyrinth, position):
    return (position / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin


def draw_vertical_wall(labyrinth, row, column):
    start_point = [apply_graphical_offset(labyrinth, column + 1) - labyrinth.cell_size / 2,
                   apply_graphical_offset(labyrinth, row - 1)]

    end_point = [apply_graphical_offset(labyrinth, column + 1) - labyrinth.cell_size / 2,
                 apply_graphical_offset(labyrinth, row + 1)]

    ligne(start_point[0], start_point[1], end_point[0], end_point[1], epaisseur=2)


def draw_horizontal_wall(labyrinth, row, column):
    start_point = [apply_graphical_offset(labyrinth, column - 1),
                   apply_graphical_offset(labyrinth, row + 1) - labyrinth.cell_size / 2]

    end_point = [apply_graphical_offset(labyrinth, column + 1),
                 apply_graphical_offset(labyrinth, row + 1) - labyrinth.cell_size / 2]

    ligne(start_point[0], start_point[1], end_point[0], end_point[1], epaisseur=2)


def draw_invisible_comma(labyrinth, row, column):
    x = (column / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
    y = (row / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
    point(x, y, epaisseur=0)


def draw_picture(labyrinth, row, column, path_to_file):
    x = (column / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
    y = (row / 2 * labyrinth.window_size / labyrinth.cell_number) + labyrinth.margin
    image(x, y, path_to_file)


picturePathDictionary = {
    'A': "../../media/ariane.png",
    'T': "../../media/thesee.png",
    'B': "../../media/arianeWithThesee.png",
    'C': "../../media/porteWithAriane.png",
    'V': "../../media/minoV.png",
    'W': "../../media/porteWithV.png",
    'H': "../../media/minoH.png",
    'I': "../../media/porteWithH.png",
    'P': "../../media/porte.png",
    'D': "../../media/game_over.png",
    'E': "../../media/game_win.png"
}


functionDictionary = {
    '+': lambda l, r, c: draw_invisible_comma(l, r, c),
    '\n': lambda l, r, c: draw_invisible_comma(l, r, c),
    ' ': lambda l, r, c: draw_invisible_comma(l, r, c),
    '|': lambda l, r, c: draw_vertical_wall(l, r, c),
    '-': lambda l, r, c: draw_horizontal_wall(l, r, c),
    'A': lambda l, r, c: draw_picture(l, r, c, l.player.picture_path),
    'T': lambda l, r, c: draw_picture(l, r, c, l.thesee.picture_path),
    'V': lambda l, r, c: draw_picture(l, r, c, picturePathDictionary['V']),
    'H': lambda l, r, c: draw_picture(l, r, c, picturePathDictionary['H']),
    'P': lambda l, r, c: draw_invisible_comma(l, r, c)
}
