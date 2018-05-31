from .specific import Specific

#Character things in the world. Will eventually be the master for all non-tile world entities to inherit from.

class Character(Specific):
	
	#Title is the general-purpose name at this point.
	#Controller determines controller type. "player" for player-controlled.
	def __init__(self, q_pos, r_pos, title, controller="baseAI"):
		Specific.__init__(self, q_pos, r_pos, title)
		self.set_sprite(self.title)
		self.make_controller(controller)

	def get_title(self):
		return self.title

	#Makes the controller object, saves it etc. Does the right stuff based on type string.
	def make_controller(controller_type):
		if controller_type == "player":
			print("oops we need to make player controller")
		elif controller_type == "baseAI":
			print("oops we need to make ai controller")
