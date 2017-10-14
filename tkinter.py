import Tkinter
import tkMessageBox
import os
import subprocess


top = Tkinter.Tk()
canvas_width = 500
canvas_height = 200
w = Tkinter.Canvas(top, 
           width=canvas_width,
           height=canvas_height)

w.pack()
top.title("Lock System".center(100))
def helloCallBack1():
	os.system('python capture-positives.py')
	print("hi")
	os.system('python train.py')
	print("hello")
	os.system('python facerecog.py')
	print("hi hi")

def helloCallBack2():
	print("resume ")
	os.system('python facerecog.py')
	

def helloCallBack3():
#deletion
	os.system('rm -R training/positive')
	print("hi")
	os.system('rm capture.pgm')
	print("hello")
	os.system('rm mean.png')
	print("hi")
	os.system('rm positive_eigenface.png')
	print("hello")
	os.system('rm negative_eigenface')
	os.system('rm training.xml')

	print("hi hi")
#start again
	helloCallBack1()

def helloCallBack4():
	top.destroy()
	
	#print("hi hi")

B1 = Tkinter.Button(top, text ="Start",width=25,bg="green",fg="white", command = helloCallBack1)
B2 = Tkinter.Button(top, text ="Resume", width=25,bg="yellow",fg="black",command = helloCallBack2)
B3 = Tkinter.Button(top, text ="Reset", width=25,bg="blue",fg="white",command = helloCallBack3)
B4 = Tkinter.Button(top, text ="Quit", width=25,bg="red",fg="white",command = helloCallBack4)

B1.pack()
B2.pack()
B3.pack()
B4.pack()
top.mainloop()
