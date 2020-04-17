from assets.lab_state import LabState
from utils.graphics import *
from utils.labyrinth_utils import *
import sys


class Solver:
	def __init__(self, labyrinth):
		self.labyrinth = labyrinth
		self.visited_states = set()
		self.moves = []

	def solve_state(self, state):
		if state.success():
			return True
		if state.defeat():
			return False
		else:
			self.visited_states.add(state.save())
			previous_state = state.saved_state
			valid_move = False
			for direction in ['Up', 'Down', 'Left', 'Right']:
				self.moves.append(direction)
				if direction == 'Up':
					valid_move = state.lab.compute_up()
				if direction == 'Down':
					valid_move = state.lab.compute_down()
				if direction == 'Left':
					valid_move = state.lab.compute_left()
				if direction == 'Right':
					valid_move = state.lab.compute_right()
				if valid_move:
					state.lab.move_minotaurs()
					state.save()
					current_position = state.saved_state
					if current_position not in self.visited_states:
						self.visited_states.add(current_position)
						if self.solve_state(state):
							return True
						else:
							self.moves.pop()
							state.load(previous_state)
					else:
						self.moves.pop()
						state.load(previous_state)
				else:
					self.moves.pop()
					state.load(previous_state)
		return False


def solve():
	if len(sys.argv) != 2:
		print("invalid number of arguments\n")
		return

	path = "../../maps/" + sys.argv[1]

	lab = parse_map(path)

	solver = Solver(lab)
	solver.solve_state(LabState(lab))

	print(solver.moves)


def graphical_solve():
	if len(sys.argv) != 2:
		print("Usage: python game.py path_to_file\n")
		return

	path = "../../maps/" + sys.argv[1]

	lab = parse_map(path)

	solver = Solver(lab)
	solver.solve_state(LabState(lab))

	print(solver.visited_states)
	print(solver.moves)

	w_size = 810
	cree_fenetre(w_size + lab.margin, w_size + lab.margin)

	lab = parse_map(path)

	while True:
		move = solver.moves.pop(0)

		if move == 'Up':
			lab.compute_up()
		if move == 'Down':
			lab.compute_down()
		if move == 'Left':
			lab.compute_left()
		if move == 'Right':
			lab.compute_right()

		lab.move_minotaurs()

		if lab.player.exit_reached and lab.player.has_thesee:
			image(w_size / 2, w_size / 2, picturePathDictionary['E'])
			attend_clic_gauche()
			break

		efface_tout()
		draw_map(lab)

		attente(0.2)

		if lab.player.has_minotaur:
			image(w_size / 2, w_size / 2, picturePathDictionary['D'])
			attend_clic_gauche()
			break


def positive_input(user_input):
	return user_input == 'Y' or user_input == 'y' or user_input == 'Yes' or user_input == 'YES' or user_input == 'yes'


def negative_input(user_input):
	return user_input == 'N' or user_input == 'n' or user_input == 'No' or user_input == 'NO' or user_input == 'no'


def main():
	print("Do you want a graphical mode ? Y/N")
	while True:
		user_input = input()
		if positive_input(user_input):
			graphical_solve()
			break
		elif negative_input(user_input):
			solve()
			break
		else:
			pass


main()
