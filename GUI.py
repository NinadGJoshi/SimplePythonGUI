from tkinter import *           #importing tkinter library for python version 3.x onwards
window=Tk()                     #creating empty window
window.geometry("20x26")        #setting height and width
window.title("Increment Decrement Number")
current=[10]                                        
space=Label(window,text="     ").grid(row=0,column=0)
number=Label(window,text=""+str(current[0]))
number.grid(row=0,column=2)
def increment(event):
	current[0]+=1
	number.configure(text=""+str(current[0]))

def decrement(event):
	temp=current[0]
	temp-=1
	current[0]=temp
	number.configure(text=""+str(current[0]))


leftbtn=Button(window, text="  -  ")
leftbtn.bind('<1>',decrement)           #Bind the button with Function when left click event occurs
leftbtn.grid(row=0,column=1)

rightbtn=Button(window,text="  +  ")
rightbtn.bind('<1>',increment)
rightbtn.grid(row=0,column=3)


window.mainloop()               
