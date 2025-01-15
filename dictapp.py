from tkinter import *
from PyDictionary import PyDictionary
from tkinter import messagebox

win=Tk()
win.title("Dictionary App")
win.geometry("1000x626")
win.resizable(0,0)

pd=PyDictionary()
def search():
	word=entword.get()
	meaning=pd.meaning(word)
	textarea.insert(END,meaning)
def clear():
	entword.delete(0,END)
	textarea.delete(1.0,END)

def iexit():
	res=messagebox.askyesno("Confirm Are u sure?")
	if res==True:
		win.destroy()
	else:
		pass

bgimage=PhotoImage(file="bg.png")
lblbg=Label(win,image=bgimage)
lblbg.place(x=0,y=0)

lblword=Label(win,text="Enter Word",font=("castellar 29 bold"),fg="red3",bg="whitesmoke")
lblword.place(x=530,y=20)

entword=Entry(win,font=("Arial 29 bold"),bd=8,justify=CENTER)
entword.place(x=510,y=80)

btnsearch=Button(win,text="Search",font=("Arial 18 bold"),bd=5 ,command=search)
btnsearch.place(x=630,y=160)

lblmeaning=Label(win,text="meaning",font=("castellar 29 bold"),fg="red3",bg="whitesmoke")
lblmeaning.place(x=580,y=240)

textarea=Text(win,font=("Arial 18 bold"),height=5,width=34,bd=5)
textarea.place(x=480,y=320)


clearimage=PhotoImage(file="clear.png")
btnclear=Button(win,image=clearimage,bd=0,bg="whitesmoke",command=clear)
btnclear.place(x=600,y=510)

exitimage=PhotoImage(file="exit.png")
btnexit=Button(win,image=exitimage,bd=0,bg="whitesmoke",command=iexit)
btnexit.place(x=720,y=500)


win.mainloop()
