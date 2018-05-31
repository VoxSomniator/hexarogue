#Master "entity" class that holds any grid object. A lot of children.
"""
ENTITY -Sprite, name, collision, opacity?
	TERRAIN -id-referenced walls and doors and such. Special functions to deref edits.
	SPECIFIC -single things, basically. Have coordinates and movement and tick-ID.
		CHARACTER -moving characters, will get multipart code later
		CONTAINER -objects to hold dropped items etc

"""

class Entity():

	#Sprite is an override. If it's none, it'll be looked up in here and assigned to defaults.
	def __init__(self, title, solid, sprite_id=None):
		self.title = title
		#Sprite lookup
		if sprite_id is None:
			self.sprite_id = 'bee'
		else:
			self.sprite_id = sprite_id
		self.solid = solid

	#Updates sprite ID thing
	def set_sprite(self, sprite_id):
		self.sprite_id = sprite_id