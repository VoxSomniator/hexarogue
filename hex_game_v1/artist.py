import pygame
import math
from . import world

#Does the screen stuff, handles displaying sprites/elements/pretty much everything lol
"""
Current draw order:
Black back-fill
Hexagon map background
Entity sprites
"""

screen_x = 800
screen_y = 600
screen = None
grid = None

hex_size = 15

#Dictionary of sprites and sprite IDs, for drawing objects.
sprite_id = {
	'player': pygame.image.load("./hex_game_v1/sprites/smallswirly.png"),
	'bee': pygame.image.load("./hex_game_v1/sprites/wall_1.png")
}

def init_screen():
	print("Activating")
	global screen
	screen = pygame.display.set_mode((screen_x, screen_y))
	pygame.display.set_icon(sprite_id['bee'])
	pygame.display.flip()

#Real janky method to give artist a reference to World, from main.
def insert_grid(grid_object):
	global grid
	grid = grid_object

def draw_update():
	#Redraws everything. Sort this later to only redraw necessary things maybe?
	draw_fill()
	draw_hexes()
	draw_entities()
	pygame.display.flip()


def draw_fill():
	#Fills the screen with background color
	screen.fill((0, 0, 0))

def draw_hexes():
	#Hexagon statistics
	line_width = 1
	color = (0, 255, 0)
	#Derived values
	hex_height = 2 * hex_size
	hex_width = math.sqrt(3) * hex_size

	#Hexagon draw offsets
	#Fill in later, to make stuff "start" off-screen
	y_offset = -14
	x_offset_base = -15

	for y in range(screen_y // math.floor(hex_height * 0.75) +1):
		#For each row, draw a bunch of segments. Every other row will need to be offset.
		for x in range(screen_x // math.floor(hex_width)):
			if (y % 2 == 0):
				x_offset = x_offset_base + (hex_width * 0.5)
			else:
				x_offset = x_offset_base

			#garbage fire
			first_point = (hex_width * x + x_offset, hex_height * ((y*.75) + 0.25) + y_offset)
			second_point = (hex_width * x + x_offset, hex_height * ((y*.75) + 0.75) + y_offset)
			third_point = (hex_width * (x + 0.5) + x_offset, hex_height * ((y*.75) + 1) + y_offset)
			fourth_point = (hex_width * (x + 1) + x_offset, hex_height * ((y*.75) + 0.75) + y_offset)

			point_list = [first_point, second_point, third_point, fourth_point]

			pygame.draw.aalines(screen, color, False, point_list, True)

#Scans through the grid, puts appropriate sprites on the screen.
#Later it'll like, follow the right object to center it.

#Basic offsets for actually putting stuff on-screen, added to all coordinates
corner_x = 12
corner_y = 10
def draw_entities():
	for q in range(len(world.Grid.GRID.world_grid)):
		for r in range(len(world.Grid.GRID.world_grid[0])):
			current_hex = world.Grid.GRID.read_hex(q, r)
			if not current_hex == []:
				draw_x = hex_size * (math.sqrt(3) * q + math.sqrt(3)/2 * r)
				draw_y = hex_size * (3/2 * r)
				draw_x += corner_x
				draw_y += corner_y
				screen.blit(sprite_id[current_hex[0].sprite_id], (draw_x, draw_y))