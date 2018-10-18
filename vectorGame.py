try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

import time
import math
import numpy as np	# required pip install
import os
import random
import sys

#print('OS is ' + str(os.name))
if len(sys.argv) < 2:
	print('# of partitions not specified')
	print('Use: "$ python3 vectorGame.py <# of arrows>"')
	exit(0)
elif len(sys.argv) > 2:
	print('Too many arguments')
	print('Use: "$ python3 vectorGame.py <# of arrows>"')
	exit(0)

class App:

	def __init__(self, master, short, buffer):
		self.shortSide = short
		self.buffer = buffer
		#master.geometry("600x600")
		master.geometry(str(short + buffer)+"x"+str(short))	# add screen start pos by + "+x_off+y_off"

		self.myCanvas = tk.Canvas(master, width=(short+buffer), height=short)

		self.myCanvas.pack()


	def newLine(self):
		myLine = self.myCanvas.create_line(300, 40, 300, 300, arrow=tk.LAST)	# parameters arbitrary, only meant for creating line object
		return myLine

	def newRect(self):
		#myRect = self.myCanvas.create_rectangle(self.shortSide, 0, self.shortSide, self.shortSide + self.buffer-1, fill='blue')
		myRect = self.myCanvas.create_rectangle(self.shortSide, 0, (self.shortSide + self.buffer), self.shortSide, fill='black')
		return myRect

def updateLine(line, canvas, newXstart,newXend ,newYstart,newYend):
	canvas.coords(line,newXstart, newYstart, newXend, newYend )

def updateRect(rect, canvas, flip):
	if flip:
		canvas.itemconfig(rect, fill='white')
	else:
		canvas.itemconfig(rect, fill='black')


#creates a matrix of start and end coordinates defining arrow
def makePoints(r, n):

	thetas = np.array(range(0, n)) * (2*math.pi/n)
	#print("thetas: ")
	#print(thetas)
	x_cos = np.cos(thetas)
	start_x = x_cos * r + r
	end_x = x_cos * -1 * r + r
	y_sin = np.sin(thetas)
	start_y = y_sin * r + r
	end_y = y_sin * -1*r + r
	values = np.stack((start_x, end_x, start_y, end_y))

	return values


window = tk.Tk()
width = window.winfo_screenwidth()-100
height = window.winfo_screenheight()-100

bufferWidth = 300;

shortSide = min(width, height)

n = int(sys.argv[1])			# number of partitions of circle
r = shortSide/2	# radius of circle which can fit on screen
#delayTime = 1 	# number of seconds to pause after printing
points = makePoints(r, n)
#print('screen width is ' + str(window.winfo_screenwidth()))
#print('screen height is ' + str(window.winfo_screenheight()))

app = App(window, shortSide, bufferWidth)
myLine = app.newLine()
app.myCanvas.itemconfig(myLine, width=r/15)					# increase width of line
app.myCanvas.itemconfig(myLine,arrowshape=(r/10, math.sqrt(math.pow(r/10,2)+math.pow(r/9,2)), r/9))		# allow for arrow

#drawing rectangular light/dark section
rect = app.newRect()
#app.myCanvas.itemconfig(rect, fill='blue')

#updateLine(myLine, app.myCanvas, 600, 200, 0, 0)
#window.update()
#time.sleep(2)
message = "hit 'enter' to change arrow direction or 'q'/'quit' to exit\n"
txt = ""
#for i in range(0,n):
	#print('point ' + str(n) + ' = (' + str(points[0][i]) +", "+str(points[1][i]) + ", " + str(points[2][i]) + ", " + str(points[3][i])+")" )

#	updateLine(myLine, app.myCanvas, points[0][i], points[1][i], points[2][i], points[3][i])
#	window.update()
#	time.sleep(delayTime)
f = open('testData.txt', 'w+')

t0 = time.time()
flip = True	#always set equal to true initially
while not(txt=='q' or txt == 'quit'):
	index = random.randint(0,n-1)
	updateLine(myLine, app.myCanvas, points[0][index], points[1][index], points[2][index], points[3][index])
	f.write("Time: %d\t\t division: %d\n" % (time.time()-t0, index))
	txt=input(message)
	updateRect(rect, app.myCanvas, flip)
	#change the value of flip
	if flip:
		flip=False
	else:
		flip=True

f.close()
print('game over')


#time.sleep(0.01)


#def drawLine()


#window.update()
#time.sleep(3)

#updateLine(myLine, app.myCanvas, x_startPoints[0], y_startPoints[0], x_endPoints[0], y_endPoints[0])

#window.update()
#time.sleep(3)
