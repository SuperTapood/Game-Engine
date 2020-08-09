from INDIGO import Screen
from INDIGO.objects.shapes import Rect, Circle, Line, Polygon
from INDIGO.objects.sprites import Group
from INDIGO.colors import *


if __name__ == "__main__":
	group = Group()
	scr = Screen(500, 500, BLACK)
	group.append(Rect(scr, WHITE, scr.MIDDLEX, scr.MIDDLEY, 50, 50))
	group.append(Circle(scr, WHITE, (50, 50), 4))
	group.append(Rect(scr, WHITE, 6, 7, 50, 50))
	print(group[group ==])