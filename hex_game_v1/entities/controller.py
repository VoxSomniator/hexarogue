from ..world import Grid

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


#Controller subtypes! Putting in the same file because fuck it i guess??

#Player controller- hooks up to the inputmanager.
class ControllerPlayer(Controller):

	def __init__(self, attached_character):
		Controller.__init__(self, attached_character)