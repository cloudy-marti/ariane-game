from utils.graphics import picturePathDictionary


class Player:
	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.has_thesee = False
		self.has_minotaur = False
		self.exit_reached = False
		self.picture_path = picturePathDictionary['A']
