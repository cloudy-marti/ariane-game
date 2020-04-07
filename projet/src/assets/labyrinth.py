from utils.graphics import picturePathDictionary


class Labyrinth:
	def __init__(self, cell_number, lst, player, thesee, minotaurs, end_point):
		self.cell_number = cell_number
		self.lst = lst
		self.window_size = 800
		self.window_actual_size = 810
		self.cell_size = self.window_size/cell_number
		self.margin = 5
		self.player = player
		self.thesee = thesee
		self.minotaurs = minotaurs
		self.end_point = end_point
		self.end_point_row = end_point.row
		self.end_point_column = end_point.column

	def update_asset_lst(self, asset, old_row, old_column, new_row, new_column):
		self.lst[old_row][old_column] = ' '
		self.lst[new_row][new_column] = asset

	def move_minotaurs(self):
		for minotaur in self.minotaurs:
			# case: Vertical minotaur
			# it will move mainly up and down
			# It will move horizontally towards the player if they are on the same row
			if minotaur.type == 'V':
				if minotaur.row == self.player.row:
					self.move_horizontally(minotaur)
				else:
					self.move_vertically(minotaur)
			# case: Horizontal minotaur
			# it will move mainly left and right
			# It will move vertically towards the player if they are on the same column
			if minotaur.type == 'H':
				if minotaur.column == self.player.column:
					self.move_vertically(minotaur)
				else:
					self.move_horizontally(minotaur)

	def move_vertically(self, minotaur):
		index = minotaur.row
		while index != self.player.row:
			last_index = index
			if minotaur.row > self.player.row:
				index -= 1
			else:
				index += 1
			# case: a wall or another minotaur is encountered
			# stop
			if self.lst[index][minotaur.column] == '-'\
				or self.lst[index][minotaur.column] == '|'\
				or self.lst[index][minotaur.column] == '+'\
				or self.lst[index][minotaur.column] == 'V'\
				or self.lst[index][minotaur.column] == 'H':
				break
			# case: either Ariane or Thesee are encountered
			# defeat condition (player.has_minotaur) to be set
			if self.lst[index][minotaur.column] == 'A' or self.lst[index][minotaur.column] == 'T':
				print(minotaur.type + " has killed you")
				minotaur.row = index
				self.update_asset_lst(minotaur.type, last_index, minotaur.column, minotaur.row, minotaur.column)
				self.player.has_minotaur = True
				break
			# case: nothing is encountered
			# advance and continue
			else:
				minotaur.row = index
				self.update_asset_lst(minotaur.type, last_index, minotaur.column, minotaur.row, minotaur.column)

	def move_horizontally(self, minotaur):
		index = minotaur.column
		while index != self.player.column:
			last_index = index
			if minotaur.column > self.player.column:
				index -= 1
			else:
				index += 1
			# case: a wall or another minotaur is encountered
			# stop
			if self.lst[minotaur.row][index] == '-' \
				or self.lst[minotaur.row][index] == '|' \
				or self.lst[minotaur.row][index] == '+' \
				or self.lst[minotaur.row][index] == 'V' \
				or self.lst[minotaur.row][index] == 'H':
				break
			# case: either Ariane or Thesee are encountered
			# defeat condition (player.has_minotaur) to be set
			if self.lst[minotaur.row][index] == 'A' or self.lst[minotaur.row][index] == 'T':
				print(minotaur.type + " has killed you")
				minotaur.column = index
				self.update_asset_lst(minotaur.type, minotaur.row, last_index, minotaur.row, minotaur.column)
				self.player.has_minotaur = True
				break
			# case: nothing is encountered
			# advance and continue
			else:
				minotaur.column = index
				self.update_asset_lst(minotaur.type, minotaur.row, last_index, minotaur.row, minotaur.column)

	def check_thesee(self, side_row, side_column, t_row, t_column):
		if self.lst[side_row][side_column] == ' '\
			and self.lst[t_row][t_column] == 'T':
			self.player.has_thesee = True
			self.lst[t_row][t_column] = ' '
			self.player.picture_path = picturePathDictionary['B']

	def collect_thesee(self):
		row_of_interest = self.player.row
		column_of_interest = self.player.column
		# check above
		self.check_thesee(row_of_interest-1, column_of_interest, row_of_interest-2, column_of_interest)
		# check under
		self.check_thesee(row_of_interest+1, column_of_interest, row_of_interest+2, column_of_interest)
		# check left
		self.check_thesee(row_of_interest, column_of_interest-1, row_of_interest, column_of_interest-2)
		# check right
		self.check_thesee(row_of_interest, column_of_interest+1, row_of_interest, column_of_interest+2)

	def compute_position(self, old_row, old_column, check_row, check_column, row, column):
		if self.lst[check_row][check_column] != '|'\
			and self.lst[check_row][check_column] != '-'\
			and self.lst[check_row][check_column] != '+':
			# Ariane collects Thesee
			# Thesee is no longer displayed on map
			if self.lst[row][column] == 'T':
				self.player.has_thesee = True
				self.player.picture_path = picturePathDictionary['B']
				self.lst[row][column] = ' '
			# Success condition : Ariane has Thesee and reaches the exit
			if self.player.row == self.end_point_row\
				and self.player.column == self.end_point_column \
				and self.player.has_thesee:
				self.player.exit_reached = True
			# Defeat condition : Ariane encounters minotaur
			if self.lst[row][column] == 'V' or self.lst[row][column] == 'H':
				self.player.has_minotaur = True
			self.player.row = row
			self.player.column = column
			self.update_asset_lst('A', old_row, old_column, row, column)
			self.collect_thesee()

	def compute_left(self):
		row = self.player.row
		column = self.player.column
		self.compute_position(row, column, row, column-1, row, column-2)

	def compute_right(self):
		row = self.player.row
		column = self.player.column
		self.compute_position(row, column, row, column+1, row, column+2)

	def compute_up(self):
		row = self.player.row
		column = self.player.column
		self.compute_position(row, column, row-1, column, row-2, column)

	def compute_down(self):
		row = self.player.row
		column = self.player.column
		self.compute_position(row, column, row+1, column, row+2, column)
