def setup():
	createCanvas(500, 500)

def draw():
	fill(255,0,0,80)
	nostroke()
	x = random(50)
	ellipse(mouseX, mouseY, 50,50)