from .valid import check_valid_group, check_valid_resp
from .rect_collision import collision


def sprite_sprite_collision(sprite1, sprite2, resp):
	check_valid_resp(resp)
	if collision(sprite1, sprite2):
		resp(sprite1, sprite2)
	return

def sprite_group_collision(sprite1, group, resp):
	check_valid_resp(resp)
	check_valid_group(group)
	for obj in group:
		if collision(sprite1, obj):
			resp(sprite1, obj)
	return

def group_group_collision(group1, group2, resp):
	check_valid_resp(resp)
	check_valid_group(group1)
	check_valid_group(group2)
	for obj in group1:
		for pbj in group2:
			if collision(obj, pbj):
				resp(obj, pbj)
	return