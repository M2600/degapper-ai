from processing.video import *
from gab.opencv import *
import java.awt.Rectangle

video = None
faces = []

def setup():
	size (640,480);
	Video=new_Capture (this,640,480)
	video. start()
def draw():
	if video.available() == true:
		video.read()
		image(video, 0, 0)

		opencv = OpenCV(this, Video)
		opencv.LoadCascade(OpenCV.CASCADE_FRONTALFACE)
		faces = opencv.detect()
		if faces. length==1:
			stroke (250,0,0);
			noFill()
			rect(faces[0].x, faces[0].y, faces[0].width, faces[0].height)
			img = LoadImage('001art-jpg')
			image(img, faces[0].x, faces[0].y, faces[0].width, faces[0].height)
