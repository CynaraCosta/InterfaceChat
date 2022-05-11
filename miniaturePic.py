from tkinter import *
from PIL import Image, ImageTk
from matplotlib.pyplot import text

class MiniaturePic:
    def __init__(self, text_area):
        self.text_area = text_area

    def add_image(self, type_of_file, name_of_file):
        all_files = [name_of_file, "files_for_test/ursinho-polar.jpeg", "files_for_test/urso-polar-grande.png"]
        file = all_files[type_of_file]
        image = Image(file)

        miniature = image.resize((100, (100 * image.height) // image.width), Image.ANTIALIAS)
        the_img = ImageTk.PhotoImage(miniature)
        the_img.image = the_img

        self.text_area.image_create(END, image = the_img)
        self.text_area.insert(END, f'\n')