from utils.graphics import *
from utils.labyrinth_utils import *


def game():
	lab = parse_map("../../maps/sandbox.txt")
	w_size = 810
	cree_fenetre(w_size + lab.margin, w_size + lab.margin)

	while True:

		efface_tout()
		draw_map(lab)

		if lab.player.has_thesee and lab.player.exit_reached:
			image(w_size/2, w_size/2, picturePathDictionary['E'])
			attend_clic_gauche()
			break
		if lab.player.has_minotaur:
			image(w_size/2, w_size/2, picturePathDictionary['D'])
			attend_clic_gauche()
			break

		event = attend_ev()
		event_type = type_ev(event)

		if event_type == 'Touche':
			key_name = touche(event)
			if key_name == 'Left':
				lab.compute_left()
			elif key_name == 'Right':
				lab.compute_right()
			elif key_name == 'Up':
				lab.compute_up()
			elif key_name == 'Down':
				lab.compute_down()
			elif key_name == 'q':
				break
			else:
				pass

		lab.move_minotaurs()
		mise_a_jour()


game()
