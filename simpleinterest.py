from tkinter import *
window = Tk()

window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

headingLabel = Label(window, text="Interest Calculator", fg="#2d2e30", bg='#a5a9ad', bd=5, font=("Calibri", 20))
headingLabel.place(x=50, y=20)


principalLabel = Label(window, text="Principal", fg="#2d2e30", bg='#a5a9ad', bd=5, font=("Calibri", 12))
principalLabel.place(x=70, y=85)

principalEntry = Entry(window, text="", bd=2, width=20)
principalEntry.place(x=150, y=90)

rateLabel = Label(window, text="Rate", fg="#2d2e30", bg='#a5a9ad', bd=5, font=("Calibri", 12))
rateLabel.place(x=70, y=125)

rateEntry = Entry(window, text="", bd=2, width=20)
rateEntry.place(x=150, y=130)

timeLabel = Label(window, text="Time", fg="#2d2e30", bg='#a5a9ad', bd=5, font=("Calibri", 12))
timeLabel.place(x=70, y=165)

timeEntry = Entry(window, text="", bd=2, width=20)
timeEntry.place(x=150, y=170)

resultFrame = LabelFrame(window, text="Result", bg="#a5a9ad", font=("Calibri", 12))
resultFrame.pack(padx=20, pady=20)
resultFrame.place(x=70,y=280)

showLabel=Label(resultFrame, text=" ", width=25, bg="#fff", font=("Calibri", 12))
showLabel.pack()

def calculateInterest():
  p = float(principalEntry.get())
  r = float(rateEntry.get())
  t = float(timeEntry.get())
  i = (p*r*t)/100
  interest = round(i,2)
  
  showLabel.destroy()

  resultLabel=Label(resultFrame, text=f"Simple Interest = {interest}", width=25, bg="#fff", font=("Calibri", 12))
  resultLabel.pack()

calButton = Button(
  window, text="Calculate Interest", 
  width=14, fg="#a5a9ad", bg="#2d2e30", bd=4, 
  font=("Calibri", 12), 
  command=calculateInterest)
calButton.place(x=150, y=220)

window.mainloop()