from .entities.character import Character
from .entities.terrain import Terrain
from .entities.specific import Specific
from .hex_geo import HexCoord

#Holds the WORLD GRID
"""
With the weird hexagonal axial coordinates, it's kind of a rhombus.
0,0 is the bottom left blunt corner, increasing Y sort of goes up and rightwards.
This is to match all the examples in redblobgames because I dont wanna fuck with that
"""

world_width = 15
world_height = 15


#Returns the grid object for my dumb shenanigans
def get_grid():
	return grid


class Grid():
	#Holds the world grid, moves stuff around, reads and outputs stuff. It's not as weird as the Entities list
	# but it's nice to have it all grouped together I guess.
	world_grid = []

	#Initializes empty 2d list for world
	def __init__(self):
		#Make grid into a list of lists. The individual lists are columns. Individual elements are null when empty
		# (or just floor), and become lists of object references/ints when there's something in them. Ints are used
		# for terrain IDs.
		for q in range(world_width):
			self.world_grid.append([])
			for r in range(world_height):
				self.world_grid[q].append(None)

	#"override" to add new things to the grid. Enemy spawning and player initializing.
	def new_entity(self, entity, q_pos, r_pos):
		self.init_hex(q_pos, r_pos)
		self.world_grid[q_pos][r_pos].append(entity)

	#Entity-mover methods. Will check collision later I guess lol
	"""
	Will have a few types probably?
	-move 1 in direction,
		with coordinates and reference
		with reference and no coordinates
	oh thats actually just one type with default args
	"""
	def relocate_entity(self, entity, destination):
		from_hex = self.world_grid[entity.coordinate.q][entity.coordinate.r]

		#Turns probably-empty destination hex into a list to prepare for adding
		self.init_hex(destination.q, destination.r)
		to_hex = self.world_grid[destination.q][destination.r]

		from_hex.remove(entity)
		to_hex.append(entity)

		#Check the previous location- If that list is empty now, turn it back to Null (empty).
		if len(from_hex) < 1:
			self.world_grid[entity.coordinate.q][entity.coordinate.r] = None


	#Returns list of objects in a hex, used by artist and collision-detector
	def read_hex(self, q_pos, r_pos):
		if self.world_grid[q_pos][r_pos] is not None:
			return self.world_grid[q_pos][r_pos]
		else:
			return []

	#Similar to read_hex but with a HexCoord lol
	def read_coordinate(self, coordinate):
		return self.read_hex(coordinate.q, coordinate.r)

	#Oft-used helper function. Hexes start out as nulls, this turns them to lists to add things to later.
	def init_hex(self, q_pos, r_pos):
		if self.world_grid[q_pos][r_pos] is None:
			self.world_grid[q_pos][r_pos] = []


class Entities():
	#Holds the entity list, handles its adding/removing, because it's weird.

	entity_list = []
	empty_spaces = []

	def __init__(self):
		self.entity_list = []
		#empty_spaces tracks gaps from removed entities that new stuff can be added to. Order unimportant.
		self.empty_spaces = []

	#Adds an entity to the list, filling empty spaces first if there are any.
	def add_entity(self, entity):
		#If the entity list is empty, just stick it on
		if len(self.entity_list) == 0:
			self.entity_list.append(entity)
		#If there's empty spaces, put it in one of those
		elif len(self.empty_spaces) > 1:
			self.entity_list[self.empty_spaces.pop()] = entity
		#If there's no empty spaces, add to the end.
		else:
			self.entity_list.append(entity)
		#Sets the entity's ID to whatever index it was given.
		entity.set_id(self.entity_list.index(entity))

	#Turns an entity's reference to None, instead of removing, to avoid shuffling IDs around.
	#Adds the now-vacant idex to empty_spaces.
	#Can pass an ID number or a reference.
	def remove_entity(self, entity_id):
		#If we were passed an entity, get its ID number and call again with the int.
		if isinstance(entity_id, character.Character):
			#Test code to check isinstnace
			self.remove_entity(self.entity_list.index(entity_id))
		#This section will have the ID number regardless.
		else:
			entity_list[entity_id] = None
			empty_spaces.append(entity_id)

	#Searches the list to find something with a particular title. Returns the first one.
	def find_entity(self, title):
		for i in self.entity_list:
			if (i is not None) and (i.get_title() == title):
				return i

#world singletons because im kind of bad at this- This way, anything importing world should be able to
#access entities and grid.

#The 2D grid thing that stores world hex positions
Grid.GRID = Grid()
#The list of active entities
Entities.ENTITIES = Entities()

def add_test_object():

	#This just kinda sticks a "player" dummy in a hex somewhere.
	new_object = Character(2, 2, "player", "player")
	Grid.GRID.new_entity(new_object, 2, 2)
	Entities.ENTITIES.add_entity(new_object)

	#Adds THE BEE
	bee_object = Character(4, 5, "bee")
	Grid.GRID.new_entity(bee_object, 4, 5)
	Entities.ENTITIES.add_entity(bee_object)

	#Returns to main for temporary FUN
	return(new_object)

