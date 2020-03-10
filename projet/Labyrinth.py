class Labyrinth :
	def __init__(self, cell_number, lst) :
		self.cell_number = cell_number
		self.lst = lst
		self.window_size = 800
		self.window_actual_size = 810
		self.cell_size = self.window_size/cell_number
		self.margin = 5
