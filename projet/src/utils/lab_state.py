class LabState:
	def __init__(self, lab):
		self.lab = lab
		self.saved_state = ()

	def defeat(self):
		return self.lab.player.has_minotaur

	def success(self):
		return self.lab.player.has_thesee and self.lab.player.exit_reached

	'''
		Save current configuration of the labyrinth into an immutable structure
	'''
	def save(self):
		player_position = (self.lab.player.row, self.lab.player.column, self.lab.player.has_thesee, self.lab.player.has_minotaur)
		thesee_position = (self.lab.thesee.row, self.lab.thesee.row)
		minotaurs_positions = []

		for minotaur in self.lab.minotaurs:
			minotaurs_positions.append((minotaur.row, minotaur.column))

		minotaurs = tuple(minotaurs_positions)

		self.saved_state = (player_position, thesee_position, minotaurs)

	'''
		Reload labyrinth with the given configuration
	'''
	def load(self, state):
		load_state_to_lab(self.lab, state)
		self.saved_state = state


def load_state_to_lab(lab, state):
	# update player configuration
	player = state[0]

	# update labyrinth state
	player_row = lab.player.row
	player_column = lab.player.column
	lab.lst[player_row][player_column] = ' '
	# update player position
	lab.player.row = player[0]
	lab.player.column = player[1]
	player_row = lab.player.row
	player_column = lab.player.column
	lab.lst[player_row][player_column] = 'A'
	# update player's collectibles
	lab.player.has_thesee = player[2]
	lab.player.has_minotaur = player[3]

	# update thesee configuration
	thesee = state[1]
	if lab.player.has_thesee:
		lab.lst[thesee[0]][thesee[1]] = ' '
	else:
		lab.lst[thesee[0]][thesee[1]] = 'T'

	# update minotaurs configuration
	minotaurs = state[2]

	for index, minotaur in enumerate(lab.minotaurs):
		# update labyrinth state
		minotaur_row = minotaur.row
		minotaur_column = minotaur.column
		lab.lst[minotaur_row][minotaur_column] = ' '
		# update minotaur position
		minotaur.row = minotaurs[index][0]
		minotaur.column = minotaurs[index][1]
		minotaur_row = minotaur.row
		minotaur_column = minotaur.column
		# should not change, update just in case
		lab.lst[minotaur_row][minotaur_column] = minotaur.type
