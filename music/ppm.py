#!/usr/bin/env python

import math
import pygame
import random
import rtmidi
from rtmidi.midiconstants import *
import time

TAU = 2 * math.pi

class Object(object):
	pass

SIZE = (640, 480)

lines = []
ball = Object()
#notes = [61, 63, 66, 68, 70] # pentatonic
#notes = [60, 64, 67, 70, 72, 74]
#notes = [60, 62, 64, 66, 68, 70, 72] # whole tone
#notes = [49, 51, 54, 56, 58, 61, 63, 66, 68, 70, 73, 75, 78, 80, 82] # triple penta
#notes = [40, 45, 50, 55, 59, 64] # guitar
notes = [40, 45, 50, 55, 59, 64] # guitar
#notes = [40, 47, 52, 55, 59, 64] # mi minor chord, inst 25
#notes = [40, 45, 52, 57, 60, 64] # la minor, inst 25
notes = [38, 45, 50, 57, 62, 65] # re minor compat
notes = list(map(lambda n: n-3, [45, 50, 57, 62, 65]))
#notes = map(lambda n: n-12, [61, 82, 63, 84, 66, 68, 70])
#notes = map(lambda n: n-24, [61, 63, 66, 68, 70]) # pentatonic
random.shuffle(notes)
initial_speed = 2800
mo = rtmidi.MidiOut()

def create():
	global lines
	xcenter = SIZE[0] / 2
	ycenter = SIZE[1] / 2
	N = len(notes)
	for i in range(N):
		ir = i * TAU
		r = 100
		lines.append((
			(xcenter + r * math.cos(i * (TAU/N)), ycenter + r * math.sin(i * (TAU/N))),
			(xcenter + r * math.cos((i+1) * (TAU/N)), ycenter + r * math.sin((i+1) * (TAU/N)))
		))
	ball.pos = (xcenter, ycenter)
	d = random.random() * TAU
	ball.vel = mul(initial_speed, (math.cos(d), math.sin(d)))

def update(dt):
	global ball
	sbefore = [side(ball.pos, line) for line in lines]
	newpos = (ball.pos[0] + ball.vel[0]*dt, ball.pos[1] + ball.vel[1]*dt)
	safter = [side(newpos, line) for line in lines]

	for i in range(len(sbefore)):
		if sbefore[i] != safter[i]:
			line = lines[i]
			ball.vel = reflect(ball.vel, normal(line))
			mo.send_message([NOTE_ON, notes[i], 127])
			break

	ball.pos = (ball.pos[0] + ball.vel[0]*dt, ball.pos[1] + ball.vel[1]*dt)

def mul(n, v):
	return (n*v[0], n*v[1])

def side(point, line):
	s = ((line[1][0] - line[0][0]) * (point[1] - line[0][1]) - (line[1][1] - line[0][1]) * (point[0] - line[0][0]))
	if s > 0:
		return 1
	elif s < 0:
		return -1
	else:
		return 0

def normal(line):
	dx = line[1][0] - line[0][0]
	dy = line[1][1] - line[0][1]
	return norm((-dy, dx))

def norm(v):
	mag = math.sqrt(v[0]*v[0] + v[1]*v[1])
	return (v[0]/mag, v[1]/mag)

def dot(v1, v2):
	return (v1[0]*v2[0] + v1[1]*v2[1])

def reflect(d, n):
	m = 2 * dot(d, n)
	rx = d[0] - m * n[0]
	ry = d[1] - m * n[1]
	return (rx, ry)

def main():
	mo.open_port(1)
	print("Using port %s" % mo.get_ports()[1])

	create()
	pygame.display.init()
	pygame.display.set_mode((640, 480))

	last_frame_time = time.clock()
	while True:
		cur_frame_time = time.clock()
		dt = cur_frame_time - last_frame_time
		update(dt)
		last_frame_time = cur_frame_time

		surf = pygame.display.get_surface()
		surf.fill((0, 0, 0))
		for l in lines:
			pygame.draw.line(surf, (255, 0, 0), l[0], l[1], 5)
#			pygame.draw.line(surf, (0, 255, 0), l[0], (l[0][0] + normal(l)[0] * 50, l[0][1] + normal(l)[1] * 50))
		pygame.draw.circle(surf, (0, 0, 255), (int(ball.pos[0]), int(ball.pos[1])), 5)

		pygame.display.flip()

main()
