from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image, ImageFont, ImageDraw              # pip install Pillow
import os

text_list = [""]

window = Tk()
window.title("Watermarker")
window.geometry("1000x1000")
window.state('zoomed')

def add_it():
    global generated_image
    window.after(2000)
    my_image = Image.open("generated_image.png")                 # Open the file in here to manipulate it
    text_font = ImageFont.truetype("arial.ttf", 60)
    text_to_add = my_entry.get()        # Retrieve the entry text
    save_name_text = save_name.get()


    edit_image = ImageDraw.Draw(my_image)               # Tells it which image we want to draw on
    edit_image.text((my_image.width/2 - 0.4 * my_image.width, my_image.height/2), text_to_add, ("white"), font=text_font)   # Adds the desired text

    my_image.save(f"{save_name_text}.jpg")             # Saves the new image with new name
    save_name.delete(0, END)
    my_entry.delete(0, END)                 # Removes text from entry box
    my_entry.insert(0, "Saving File...Finished.")    # Inserts new text into entry box
    save_name.insert(0, "Close the window.")
    os.remove("C:/Users/danie/PycharmProjects/Portfolio-Project-4_Image-watermark/generated_image.png")

def scale_by_factor(im, factor):
    return im.resize((round(im.width * factor), round(im.height * factor)))


window.filename = filedialog.askopenfilename(initialdir="C:/Users/danie/PycharmProjects/Portfolio-Project-4_Image-watermark",
                                             title="Select a File",
                                             filetypes=(("png files", "*.png*"), ("all files", "*.*"))) # Opens window to open image from
im = Image.open(window.filename)

width, height = im.size
scaled = False

if width > 1080 or height > 1920:
    im = scale_by_factor(im, 0.3)
    scaled = True


image_name = ImageTk.PhotoImage(im)


generated_image = im
if scaled:
    generated_image = scale_by_factor(generated_image, 1/0.3)
generated_image.save("generated_image.png")

window.focus_force()

my_label = Label(window, image=image_name)          # Places image inside label
my_label.grid(row=0, column=0, pady=20, rowspan=3)

window.update()

my_entry = Entry(window, font=("Helvetica", 24))    # Watermark
my_entry.insert(0, "Watermark Text")
my_entry.grid(row=0, column=1, padx=20, pady=20)

window.update()

save_name = Entry(window, font=("Helvetica", 24))    # Name of new file entry
save_name.insert(0, "New File Name")
save_name.grid(row=1, column=1, padx=20, pady=20)

window.update()

my_button = Button(window, text="Add text to image", command=add_it, font=("Helvetica", 24))    # Create new image
my_button.grid(row=2, column=1, padx=20, pady=20)

window.mainloop()

