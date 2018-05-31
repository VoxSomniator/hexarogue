from .entity import Entity
from ..hex_geo import HexCoord

#Handles terrain pseudo-objects.
"""
The world grid holds *a lot* of references to the same object. All "wall" hexes have a reference
 to the same wall entity. There are special methods for detaching if a wall is manipulated etc.
 so that it doesn't alter every wall.
"""
class Terrain(Entity):

	def __init__(self, title, solid, sprite_id):
		Entity.__init__(self, title, solid, sprite_id)