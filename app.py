from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Image Viewer')

# for filename in os.listdir


img1 = ImageTk.PhotoImage(Image.open("images\pic1.jpg").resize((600, 400),Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("images\pic2.jpg").resize((600, 400),Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("images\pic3.jpg").resize((600, 400),Image.ANTIALIAS))

img_list = [img1, img2, img3]

my_label= Label(image=img1)
my_label.grid(row=0,column=0, columnspan=3)

def next(img_number):

    global my_label
    global next_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image=img_list[img_number-1]) # img_number is n+1 so shifting to next pic in list requires -1 to move to 1th element & etc
    next_button = Button(root, text='->', command=lambda: next(img_number+1))
    back_button = Button(root, text='<-', command=lambda: next(img_number-1))

    if img_number == len(img_list):
        next_button = Button(root, text = "->", state='disabled')

    my_label.grid(row=0,column=0,columnspan=3)
    next_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)


def back():
    global my_label
    global next_button    
    global back_button

    my_label.grid_forget()
    my_label = Label(root, image=img_list[])

next_button = Button(root, text="->",command=lambda: next(2))
back_button = Button(root, text="<-", state='disabled', command=back)
exit_button = Button(root, text="Exit", command=root.quit)


back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
next_button.grid(row=1,column=2)

# exit_button.pack()
root.mainloop()                                                                                           