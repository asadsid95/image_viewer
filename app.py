from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image Viewer')

img1 = ImageTk.PhotoImage(Image.open("/images/pic1.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("/images/pic2.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("/images/pic3.jpeg"))


next_button = Button(root, text="->")
back_button = Button(root, text="<-")
exit_button = Button(root, text="exit", command=root.quit)



laabel = Label(image=img1)
laabel.pack()

exit_button.pack()
root.mainloop()                                                                                           