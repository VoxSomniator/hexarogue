from .. import world
from .. import inputmanager
from ..hex_geo.hexcoord import HexCoord

#Movement offset references/lookup
offset_lookup = {
			'r': HexCoord.R,
			'dr': HexCoord.DR,
			'dl': HexCoord.DL,
			'l': HexCoord.L,
			'ul': HexCoord.UL,
			'ur': HexCoord.UR,
		}

#Controller.
"""
Controls a character, does turn-waiting stuff I guess, either AI or player input. Turn queueing thing.
Also does movement and collision-checking that's important
"""
class Controller():

	#Attached ID is just the ID number of whatever entity is being controlled.
	def __init__(self, attached_character):
		self.attached_character = attached_character

	#Relocate commands. Checks for collision in the desired direction, then tell the world grid to move us.

	#Step one hex in some direction.
	def step(self, direction):
		dest_coord = offset_lookup[direction] + self.attached_character.coordinate
		#If the destination hex is okay/nonsolid
		if self.collision_ok(world.Grid.GRID.read_coordinate(dest_coord)):
			self.commit_move(dest_coord)



	#Utility thing- Check collision. True if the move is okay.
	def collision_ok(self, hex_list):
		print("nothing here yet")
		return True

	#Sorta-utility, called after collision is checked to tell worldgrid and the Specific to actually do it
	def commit_move(self, destination):
		world.Grid.GRID.relocate_entity(self.attached_character, destination)
		self.attached_character.reposition(destination)

#Controller subtypes! Putting in the same file because fuck it i guess??

#Player controller- hooks up to the inputmanager.
class ControllerPlayer(Controller):

	def __init__(self, attached_character):
		Controller.__init__(self, attached_character)
		inputmanager.set_player_controller(self)
		print("Controller added")

#Most basic ai controller. Probably does nothing.
class ControllerBaseAI(Controller):

	def __init__(self, attached_character):
		Controller.__init__(self, attached_character)