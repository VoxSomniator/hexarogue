from .entity import Entity
from ..hex_geo import HexCoord

#Entity child that represents a specific thing, with position and movement and a specificID

class Specific(Entity):

	def __init__(self, q_pos, r_pos, title):
		Entity.__init__(self, title, False)
		self.coordinate = HexCoord(q_pos, r_pos)

	def set_id(self, ID_number):
		self.ID_number = ID_number

	def get_coordinate(self):
		return self.coordinate

	#Changes x and y coordinates, will do collision-checking later
	def reposition(self, coordinate):
		self.coordinate = HexCoord(coordinate.q, coordinate.r)
