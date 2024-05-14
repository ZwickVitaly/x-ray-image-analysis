from pathlib import Path
from multiprocessing import Process

from PIL import Image, ImageTk

from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

from funcs import (
    hist_3d,
    high_pass_filter,
    median_filter,
    pseudo_color_filter,
    sobel_filter,
)


root = tk.Tk()
root.title("Image Processing GUI")
root.geometry('600x600')
button_frame = tk.Frame(root)
button_frame.pack()
img_path = None
main_label = None


def load_image():
    global img_path, main_label
    if main_label:
        main_label.destroy()

    def resize_image(event):
        nonlocal image, photo
        new_width = event.width
        new_height = event.height
        image = copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        main_label.config(image=photo)
        main_label.image = photo  # avoid garbage collection

    file_path = filedialog.askopenfilename(filetypes=[("Pictures", ".jpg .png .jpeg")])
    if Path(file_path).is_dir() or Path(file_path).suffix not in (".jpeg", ".jpg", ".png"):
        return
    img_path = file_path

    image = Image.open(file_path)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    main_label = ttk.Label(root, image=photo)
    main_label.bind('<Configure>', resize_image)
    main_label.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, anchor=tk.W)


def median_filter_apply():
    global img_path
    if not img_path:
        return
    process = Process(target=median_filter, args=(img_path,))
    process.start()


def pseudo_colors_terrain_apply():
    global img_path
    if not img_path:
        return
    process = Process(target=pseudo_color_filter, args=(img_path,), kwargs=({"cmap": "terrain"}))
    process.start()


def pseudo_colors_plasma_apply():
    global img_path
    if not img_path:
        return
    process = Process(target=pseudo_color_filter, args=(img_path,), kwargs=({"cmap": "plasma"}))
    process.start()


def hist_3d_build():
    global img_path
    if not img_path:
        return
    hist_3d(img_path)
    # process = Process(target=hist_3d, args=(img_path,))
    # process.start()


def sobel_apply():
    global img_path
    if not img_path:
        return
    process = Process(target=sobel_filter, args=(img_path,))
    process.start()


def high_pass_apply():
    global img_path
    if not img_path:
        return
    process = Process(target=high_pass_filter, args=(img_path,))
    process.start()


load_button = tk.Button(button_frame, text="Load image", command=load_image)

median_button = tk.Button(button_frame, text="Median filter", command=median_filter_apply)

pseudo_terrain_button = tk.Button(button_frame, text="Pseudocolor (terrain)", command=pseudo_colors_terrain_apply)

pseudo_plasma_button = tk.Button(button_frame, text="Pseudocolor (plasma)", command=pseudo_colors_plasma_apply)

hist_3d_button = tk.Button(button_frame, text="3d depth model", command=hist_3d_build)

sobel_button = tk.Button(button_frame, text="Sobel filter", command=sobel_apply)

high_pass_button = tk.Button(button_frame, text="High pass filter", command=high_pass_apply)


if __name__ == "__main__":
    buttons = [
        median_button,
        pseudo_terrain_button,
        pseudo_plasma_button,
        hist_3d_button,
        sobel_button,
        high_pass_button,
    ]
    button_frame = tk.Frame(root)
    button_frame.pack()
    load_button.grid(row=1, columnspan=3)
    row = 2
    for i, button in enumerate(buttons):
        if i % 3 == 0:
            row += 1
        button.grid(row=row, column=i % 3, sticky="ew")
    root.mainloop()
