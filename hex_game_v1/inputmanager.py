import pygame
from . import world

#Does INPUT STUFF. State machine I guess? Routes button events to the correct controller/menu/etc.

player_obj = None
player_moves = None

#Will do some kinda state-engine thing later but for now lol
state = "playermove"

#Starts up manager. Gets player object for now.
def init_input():
	global player_obj
	player_obj = world.Entities.ENTITIES.find_entity("player")

	global player_moves
	player_moves = {
		263: 'ul',
		260: 'l',
		257: 'dl',
		265: 'ur',
		262: 'r',
		259: 'dr'
	}


#Called by main every frame. Reads pygame inputs, updates held keys, etc.
#Usually returns true, returns false if the game is exited.
def check_input():
	continuing = True
	for event in pygame.event.get():
		#print(pygame.event.event_name(event.type))
		if event.type == pygame.QUIT:
			continuing = False
		elif event.type == pygame.KEYDOWN:
			print("key pressed: ",event.key)

			if state == "playermove":
				#Do player movement key stuff.
				if event.key in player_moves:
					world.Grid.GRID.relocate_entity(player_obj, player_moves[event.key])
	return continuing