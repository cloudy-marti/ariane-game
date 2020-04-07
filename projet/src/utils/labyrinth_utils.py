from assets.collectible import Collectible
from assets.minotaur import Minotaur
from assets.player import Player
from projet.src.assets.labyrinth import Labyrinth
from utils.graphics import picturePathDictionary


def parse_line(line):
    # parse one line
    lst = []
    for char in line:
        if char != '\n':
            lst.append(char)
    return lst


def parse_map(path_to_file):
    labyrinth_map = []
    with open(path_to_file, 'r') as fp:
        size = int(fp.readline())
        for line in fp:
            labyrinth_map.append(parse_line(line))

    minotaurs = []

    for i, row in enumerate(labyrinth_map):
        for j, column in enumerate(row):
            if column == 'A':
                ariane = Player(i, j)
            if column == 'T':
                thesee = Collectible(i, j, picturePathDictionary['T'])
            if column == 'V':
                minotaurs.append(Minotaur(i, j, 'V'))
            if column == 'H':
                minotaurs.append(Minotaur(i, j, 'H'))
            if column == 'P':
                exit_door = Collectible(i, j, picturePathDictionary['P'])

    labyrinth = Labyrinth(size, labyrinth_map, ariane, thesee, minotaurs, exit_door)
    return labyrinth


def win_game():
    print("yeepee")


def display_board_game(board_game):
    for row in board_game:
        for char in row:
            print(char, end="")
        print('\n')


def load_board_game(labyrinth):
    board_game = []
    for row in labyrinth:
        board_line = []
        for char in row:
            if char != '\n' and char != '+':
                board_line.extend(char)
            if char == '\n':
                board_game.append(board_line)
    del(board_game[len(board_game)-1])
    del(board_game[0])
