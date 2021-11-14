from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Image Viewer')

# for filename in os.listdir


img1 = ImageTk.PhotoImage(Image.open("images\pic1.jpg").resize((600, 400),Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("images\pic2.jpg").resize((600, 460),Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("images\pic3.jpg").resize((600, 460),Image.ANTIALIAS))


next_button = Button(root, text="->")
back_button = Button(root, text="<-")
exit_button = Button(root, text="exit", command=root.quit)

laabel = Label(image=img1)
laabel.grid(row=0,column=0, columnspan=3)

back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
next_button.grid(row=1,column=2)

# exit_button.pack()
root.mainloop()                                                                                           