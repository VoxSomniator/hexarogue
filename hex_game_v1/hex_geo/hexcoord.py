import math

#Holds 2D hex coordinates and can do fancy math. Basically a tuple pair with MORE FEATURES.
#Coordinates will never actually be changed, all modifiers just return a new coordinate for assigning.

#The coordinates!
class HexCoord():

	def __init__(self, q=0, r=0):
		self.q = q
		self.r = r

	#Basic addition of both values, for offsets
	def __add__(self, other):
		return HexCoord(self.q + other.q, self.r + other.r)

	def pixelize(self, size):
		return (size)

#Axial offset singletons.
HexCoord.R = HexCoord(1, 0)
HexCoord.DR = HexCoord(0, 1)
HexCoord.DL = HexCoord(-1, 1)
HexCoord.L = HexCoord(-1, 0)
HexCoord.UL = HexCoord(0, -1)
HexCoord.UR = HexCoord(1, -1)