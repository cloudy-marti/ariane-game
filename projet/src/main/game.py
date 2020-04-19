from utils.graphics import *
from utils.labyrinth_utils import *
import sys


def game():
	if len(sys.argv) != 2:
		print("Usage: python game.py path_to_file\n")
		return

	path = "../maps/" + sys.argv[1]

	lab = parse_map(path)
	w_size = 810
	cree_fenetre(w_size + lab.margin, w_size + lab.margin)

	while True:
		if lab.player.exit_reached and lab.player.has_thesee:
			image(w_size/2, w_size/2, picturePathDictionary['E'])
			attend_clic_gauche()
			break

		efface_tout()
		draw_map(lab)

		if lab.player.has_minotaur:
			image(w_size/2, w_size/2, picturePathDictionary['D'])
			attend_clic_gauche()
			break

		event = attend_ev()
		event_type = type_ev(event)

		valid_move = False

		if event_type == 'Touche':
			key_name = touche(event)
			if key_name == 'Left':
				valid_move = lab.compute_left()
			elif key_name == 'Right':
				valid_move = lab.compute_right()
			elif key_name == 'Up':
				valid_move = lab.compute_up()
			elif key_name == 'Down':
				valid_move = lab.compute_down()
			elif key_name == 'q':
				break
			else:
				pass

		if valid_move:
			lab.move_minotaurs()


game()
