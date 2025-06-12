from processing.serial import *

attack=0
score=0

def setup():
	size (640,480);
	microbit = Serial(this, "COM11" ,115200);
	microbit.clear()
	microbit.bufferUntil(10)

def draw():
	intums=millis();
	if ms > 10000:
		noLoop()
	noStroke();
	fill(0);
	rect(random(640), random(640), random(100), random(100))
	for x in range(attack):
		fill(255);
		rect (random (640), random (480), 50,50)
	score = score + attack
	println(score)

def serialEvent(microbit):
	string = trim(str)
	string = str.substring(2)
	attack = int(string)
	attack = (attack - 1080) / 100
