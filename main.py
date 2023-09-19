import pyqrcode
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

def put_location_qr():
    output_place = filedialog.askdirectory()
    if output_place:
        my_qr_location_entry.delete(0, END)
        my_qr_location_entry.insert(0, output_place)

def qr_generator():
    if len(my_qr_link_entry.get()) == 0 or len(my_qr_name_entry.get()) == 0 or len(my_qr_location_entry.get()) == 0:
        status_label.config(text="Please enter all info!")
    else:
        try:
            url = my_qr_link_entry.get()
            qr_code = pyqrcode.create(url)
            output_filename = my_qr_name_entry.get() + '.svg'
            output_location = os.path.join(my_qr_location_entry.get(), output_filename)
            qr_code.svg(output_location, scale=5)
            status_label.config(text="QR code generation is successful.")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")

my_window = Tk()
my_window.title("QR Code Generator")
my_window.minsize(width=300, height=200)
my_window.config(background="#7f86ff")

my_icon = PhotoImage(file='qricon.png')
my_window.iconphoto(False, my_icon)

my_img = Image.open("qrimage.png")
new_width = 150
new_height = 100
my_img = my_img.resize((new_width, new_height))
tk_img = ImageTk.PhotoImage(my_img)
label = Label(my_window, image=tk_img)
label.grid(row=0, column=0, columnspan=2)

my_qr_link_label = Label(text="Enter URL to Generate QR Code:")
my_qr_link_label.grid(row=1, column=0, sticky="w")
my_qr_link_label.config(background="#7f86ff")

my_qr_link_entry = Entry(width=30)
my_qr_link_entry.grid(row=1, column=1)
my_qr_link_entry.config(background="gray")

my_qr_name_label = Label(text="QR Name:")
my_qr_name_label.grid(row=2, column=0, sticky="w")
my_qr_name_label.config(background="#7f86ff")

my_qr_name_entry = Entry(width=30)
my_qr_name_entry.grid(row=2, column=1)
my_qr_name_entry.config(background="gray")

my_qr_location_label = Label(text="Select the Location:")
my_qr_location_label.grid(row=3, column=0, sticky="w")
my_qr_location_label.config(background="#7f86ff")

my_qr_location_entry = Entry(width=30)
my_qr_location_entry.grid(row=3, column=1)
my_qr_location_entry.config(background="gray")

my_button_icon = Image.open("buttonicon.jpg")
second_width = 20
second_height = 20
my_button_icon = my_button_icon.resize((second_width, second_height))
tk_icon = ImageTk.PhotoImage(my_button_icon)

my_location_button = Button(image=tk_icon, command=put_location_qr)
my_location_button.grid(row=3, column=2)

apply_button = Button(text="Generate QR Code", command=qr_generator)
apply_button.grid(row=4, column=0, columnspan=2)
apply_button.config(background="gray")

status_label = Label(text="")
status_label.grid(row=5, column=0, columnspan=2)
status_label.config(background="#7f86ff")

my_window.mainloop()
