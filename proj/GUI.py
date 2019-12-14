#IMPORT ALL LIBRARIES THAT ARE NEEDED 
import vidtoimg as py
import crop as cr
import transpose as tr
import rot as rt
import resize as rz
from tkinter import  *
from tkinter import ttk
#CREATING MAIN FRAME  WITH TITLE "WORKING WITH IMAGES"
frame1 = Tk()
frame1.title("WORKING WITH IMAGES")
frame1.geometry("300x500")
frame1.config(bg='cyan')

#DEFINING A FUNCTION "NEW_FRAME1", THIS FUNCTION WILL INVOKED WHEN CLICKING ON THE BUTTON "CONVERT" 
def new_frame1():
	top = Toplevel()
	top.title("CONVERTING VIDEO TO IMAGES")
	top.geometry("500x500")
	top.config(bg='cyan')
	l1 = Label(top,text = "Enter the location where video file is located : ",font=("TIMES",20))
	l2 = Label(top,text = "Enter the filename where you want to store the images : ",font=("TIMES",20))
	l1.grid(column = 0,row = 0,sticky = W,padx = 10,pady = 10)
	l2.grid(column = 0,row = 1,sticky = W,padx = 10, pady = 10)
	l1.config(bg = 'black',fg = 'yellow')
	l2.config(bg = 'black',fg = 'yellow')
	x = StringVar()
	y = StringVar()
	
	#GIVE THE PATH OF VIDEO
	e1 = ttk.Entry(top,textvariable = x)
	
	#GIVE THE FOLDER NAME TO SAVE THE IMAGES IN DESIRED LOCATION
	e2 = ttk.Entry(top,textvariable = y)
	
	e1.grid(column = 1,row = 0,padx = 10, pady = 10)
	e2.grid(column = 1,row = 1,padx = 10, pady = 10)
	
	#CREATING A BUTTON WITH NAME "CONVERT", ON CLICKING THIS BUTTON WILL INVOKE THE FUNCTION WITH NAME "Converting" AND PERFORM CONVERTING THE VIDEO INTO IMAGES OPERATION
	B = ttk.Button(top, text ="CONVERT",width = 50, command = lambda:py.Converting(x.get(),y.get()))
	B.grid(row = 2,column =3, padx = 10,pady = 10)

#DEFINING A FUNCTION "NEW_FRAME2", THIS FUNCTION WILL INVOKED WHEN CLICKING ON THE BUTTON "CROP"
def new_frame2():
	top1 = Toplevel()
	top1.title("CROP THE IMAGE")
	top1.geometry("500x500")
	top1.config(bg='cyan')
	l3 = Label(top1,text = "Enter the location where image file is located : ",font=("TIMES",20))
	l4 = Label(top1,text = "Enter the location where you want to store the image : ",font=("TIMES",20))
	m = Label(top1,text = "Enter how much of width to be cropped : ",font = ("TIMES",20))
	n = Label(top1,text = "Enter how much of height to be cropped : ",font = ("TIMES",20))
	l3.grid(column = 0,row = 0,sticky = W,padx = 10, pady = 10)
	l4.grid(column = 0,row = 1,sticky = W,padx = 10, pady = 10)
	m.grid(column = 0,row = 2,sticky = W,padx = 10, pady = 10)
	n.grid(column = 0,row = 3,sticky = W,padx = 10, pady = 10)
	l3.config(bg = 'black',fg = 'yellow')
	l4.config(bg = 'black',fg = 'yellow')
	m.config(bg = 'black',fg = 'yellow')
	n.config(bg = 'black',fg = 'yellow')
	x1 = StringVar()
	y1 = StringVar()
	w1 = IntVar()
	h1 = IntVar()
	#GIVE THE PATH OF IMAGE
	e3 = ttk.Entry(top1,textvariable = x1)
	
	#GIVE PATH TO SAVE THE IMAGE IN DESIRED LOCATION
	e4 = ttk.Entry(top1,textvariable = y1)
	
	#GIVE THE HOW MUCH OF WIDTH AND HEIGHT TO BE CROPPED IN INTEGER VALUES
	m1 = ttk.Entry(top1,textvariable = w1)
	n1 = ttk.Entry(top1,textvariable = h1)
	
	e3.grid(column = 1,row = 0,padx = 10, pady = 10)
	e4.grid(column = 1,row = 1,padx = 10, pady = 10)
	m1.grid(column = 1,row = 2,padx = 10, pady = 10)
	n1.grid(column = 1,row = 3,padx = 10, pady = 10)
	
	#CREATING A BUTTON WITH NAME "CROP", ON CLICKING THIS BUTTON WILL INVOKE THE FUNCTION WITH NAME "Croping" AND PERFORM CROP OPERATION
	B = ttk.Button(top1, text ="CROP",width = 50, command = lambda:cr.Croping(x1.get(),y1.get(),w1.get(),h1.get()))
	B.grid(row = 4,column =3,padx = 10, pady = 10)

#DEFINING A FUNCTION "NEW_FRAME3", THIS FUNCTION WILL INVOKED WHEN CLICKING ON THE BUTTON "TRANSPOSE"
def new_frame3():
	top2 = Toplevel()
	top2.title("TRANSPOSE THE IMAGE")
	top2.geometry("500x500")
	top2.config(bg='cyan')
	l5 = Label(top2,text = "Enter the location where image file is located : ",font=("TIMES",20))
	l6 = Label(top2,text = "Enter the location where you want to store the image : ",font=("TIMES",20))
	l5.grid(column = 0,row = 0,sticky = W,padx = 10, pady = 10)
	l6.grid(column = 0,row = 1,sticky = W,padx = 10, pady = 10)
	l5.config(bg = 'black',fg = 'yellow')
	l6.config(bg = 'black',fg = 'yellow')
	x2 = StringVar()
	y2 = StringVar()
	
	#GIVE THE PATH OF IMAGE
	e5 = ttk.Entry(top2,textvariable = x2)
	
	#GIVE PATH TO SAVE THE IMAGE IN DESIRED LOCATION
	e6 = ttk.Entry(top2,textvariable = y2)
	
	e5.grid(column = 1,row = 0,padx = 10, pady = 10)
	e6.grid(column = 1,row = 1,padx = 10, pady = 10)
	
	#CREATING A BUTTON WITH NAME "TRANSPOSE", ON CLICKING THIS BUTTON WILL INVOKE THE FUNCTION WITH NAME "Transpose" AND PERFORM TRANSPOSE OPERATION
	B = ttk.Button(top2, text ="TRANSPOSE",width = 50, command = lambda:tr.Transpose(x2.get(),y2.get()))
	B.grid(row = 2,column =3,padx = 10, pady = 10)
	
#DEFINING A FUNCTION "NEW_FRAME4", THIS FUNCTION WILL INVOKED WHEN CLICKING ON THE BUTTON "ROTATE"
def new_frame4():
	top3 = Toplevel()
	top3.title("ROTATE THE IMAGE")
	top3.geometry("500x500")
	top3.config(bg='cyan')
	l7 = Label(top3,text = "Enter the location where image file is located : ",font=("TIMES",20))
	l8 = Label(top3,text = "Enter the location where you want to store the image : ",font=("TIMES",20))
	l9 = Label(top3,text = "Enter how many degrees to rotate image : ",font=("TIMES",20))
	l7.grid(column = 0,row = 0,sticky = W,padx = 10, pady = 10)
	l8.grid(column = 0,row = 1,sticky = W,padx = 10, pady = 10)
	l9.grid(column = 0,row = 2,sticky = W,padx = 10, pady = 10)
	l7.config(bg = 'black',fg = 'yellow')
	l8.config(bg = 'black',fg = 'yellow')
	l9.config(bg = 'black',fg = 'yellow')
	x3 = StringVar()
	y3 = StringVar()
	a3 = IntVar()
	
	#GIVE THE PATH OF IMAGE
	e7 = ttk.Entry(top3,textvariable = x3)
	
	#GIVE PATH TO SAVE THE IMAGE IN DESIRED LOCATION
	e8 = ttk.Entry(top3,textvariable = y3)
	
	#GIVE THE ANGLE TO ROTATE THE IMAGE
	e9 = ttk.Entry(top3,textvariable = a3)
	
	e7.grid(column = 1,row = 0,padx = 10, pady = 10)
	e8.grid(column = 1,row = 1,padx = 10, pady = 10)
	e9.grid(column = 1,row = 2,padx = 10, pady = 10)
	
	#CREATING A BUTTON WITH NAME "ROTATE", ON CLICKING THIS BUTTON WILL INVOKE THE FUNCTION WITH NAME "Rotate" AND PERFORM ROTATION OPERATION
	B = ttk.Button(top3, text ="ROTATE",width = 50, command = lambda:rt.Rotate(x3.get(),y3.get(),a3.get()))
	B.grid(row = 4,column =3,padx = 10, pady = 10)

#DEFINING A FUNCTION "NEW_FRAME5", THIS FUNCTION WILL INVOKED WHEN CLICKING ON THE BUTTON "RESIZE"
def new_frame5():
	top4 = Toplevel()
	top4.title("RESIZE THE IMAGE")
	top4.geometry("500x500")
	top4.config(bg='cyan')
	l10 = Label(top4,text = "Enter the location where image file is located : ",font=("TIMES",20))
	l11 = Label(top4,text = "Enter the location where you want to store the image : ",font=("TIMES",20))
	l12 = Label(top4,text = "Enter the width of the image : ",font=("TIMES",20))
	l13 = Label(top4,text = "Enter the height of the image : ",font=("TIMES",20))
	l10.grid(column = 0,row = 0,sticky = W,padx = 10, pady = 10)
	l11.grid(column = 0,row = 1,sticky = W,padx = 10, pady = 10)
	l12.grid(column = 0,row = 2,sticky = W,padx = 10, pady = 10)
	l13.grid(column = 0,row = 3,sticky = W,padx = 10, pady = 10)
	l10.config(bg = 'black',fg = 'yellow')
	l11.config(bg = 'black',fg = 'yellow')
	l12.config(bg = 'black',fg = 'yellow')
	l13.config(bg = 'black',fg = 'yellow')
	x4 = StringVar()
	y4 = StringVar()
	w = IntVar()
	h = IntVar()
	
	#GIVE THE PATH OF IMAGE
	e10 = ttk.Entry(top4,textvariable = x4)
	
	#GIVE PATH TO SAVE THE IMAGE IN DESIRED LOCATION
	e11 = ttk.Entry(top4,textvariable = y4)
	
	#GIVE THE WIDTH TO RESIZE THE IMAGE
	e12 = ttk.Entry(top4,textvariable = w)
	
	#GIVE THE HEIGHT TO RESIZE THE IMAGE
	e13 = ttk.Entry(top4,textvariable = h)
	
	e10.grid(column = 1,row = 0,padx = 10, pady = 10)
	e11.grid(column = 1,row = 1,padx = 10, pady = 10)
	e12.grid(column = 1,row = 2,padx = 10, pady = 10)
	e13.grid(column = 1,row = 3,padx = 10, pady = 10)
	
	#CREATING A BUTTON WITH NAME "RESIZE", ON CLICKING THIS BUTTON WILL INVOKE THE FUNCTION WITH NAME "Resize" AND PERFORM RESIZING OPERATION
	B = ttk.Button(top4, text ="RESIZE",width = 50, command = lambda:rz.Resize(x4.get(),y4.get(),w.get(),h.get()))
	B.grid(row = 4,column =3,padx = 10, pady = 10)

#CREATING A BUTTON WITH NAME "CONVERT VIDEO INTO IMAGES", ON CLICKING THIS BUTTON WILL OPEN A FRAME "NEW_FRAME1"
B = ttk.Button(frame1, text ="CONVERT VIDEO INTO IMAGES", command = new_frame1)

#CREATING A BUTTON WITH NAME "CROP THE IMAGE", ON CLICKING THIS BUTTON WILL OPEN A FRAME "NEW_FRAME2"
B1 = ttk.Button(frame1, text ="CROP THE IMAGE", command = new_frame2)

#CREATING A BUTTON WITH NAME "TRANSPOSE THE IMAGE", ON CLICKING THIS BUTTON WILL OPEN A FRAME "NEW_FRAME3"
B2 = ttk.Button(frame1, text ="TRANSPOSE THE IMAGE", command = new_frame3)

#CREATING A BUTTON WITH NAME "ROTATE THE IMAGE", ON CLICKING THIS BUTTON WILL OPEN A FRAME "NEW_FRAME4"
B3 = ttk.Button(frame1, text ="ROTATE THE IMAGE", command = new_frame4)

#CREATING A BUTTON WITH NAME "RESIZE THE IMAGE", ON CLICKING THIS BUTTON WILL OPEN A FRAME "NEW_FRAME5"
B4 = ttk.Button(frame1, text ="RESIZE THE IMAGE", command = new_frame5)

#ADDING THIS BUTTONS TO MAIN FRAME "FRAME1" AT PARTICULAR POSITIONS USING GRID FUNCTION
B.grid(row = 1, column = 20,padx = 30,pady = 20)
B1.grid(row = 2, column = 20,padx = 30,pady = 20)
B2.grid(row = 3, column = 20,padx = 30,pady = 20)
B3.grid(row = 4, column = 20,padx = 30,pady = 20)
B4.grid(row = 5, column = 20,padx = 20,pady = 20)

#THE FUNCTION "MAINLOOP" IS AN INFINITE LOOP ,WAITS FOR EVENTS AND UPDATING THE GUI
frame1.mainloop()
