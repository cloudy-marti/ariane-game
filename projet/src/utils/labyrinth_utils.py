from assets.collectible import Collectible
from assets.minotaur import Minotaur
from assets.player import Player
from assets.labyrinth import Labyrinth
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

