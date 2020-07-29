# base collision rules
def collision(sprite1, sprite2):
	if sprite1.x < sprite2.x + sprite2.w:
		if sprite1.x + sprite1.w > sprite2.x:
			if sprite1.y < sprite2.y + sprite2.h:
				if sprite1.y + sprite1.h > sprite2.y:
					return True
	return False