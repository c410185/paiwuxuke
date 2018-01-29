from Tkinter import *
root = Tk()
cv = Canvas(root, bg = 'white')
rt = cv.create_rectangle(10, 10, 110, 110, outline = 'red', stipple = 'gray12', fill = 'green')
cv.pack()
cv.after(500)
cv.coords(rt, (40, 40, 80, 80))
root.mainloop()