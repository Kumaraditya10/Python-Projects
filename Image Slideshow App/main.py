import tkinter as tk
from PIL import Image, ImageTk
import itertools
import time

# 1. Setup the main window
root = tk.Tk()
root.title("Image Slideshow Viewer")

# 2. Define the list of image file paths
# Replace the paths below with the actual paths of images on your computer
image_paths = [
    r"C:\path\to\your\image1.jpg",
    r"C:\path\to\your\image2.jpg",
    r"C:\path\to\your\image3.jpg",
    r"C:\path\to\your\image4.jpg",
    r"C:\path\to\your\image5.jpg"
]

# 3. Resize and convert images for Tkinter
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(img) for img in images]

# 4. Create a label to display images
label = tk.Label(root)
label.pack()

# 5. Define functions for the slideshow
def update_image(image):
    label.config(image=image)
    root.update()
    time.sleep(3) # Display each image for 3 seconds

# Create an infinite cycle of images
slideshow = itertools.cycle(photo_images)

def start_slideshow():
    # Loop through the images and update the display
    for _ in range(len(image_paths)):
        img = next(slideshow)
        update_image(img)

# 6. Add a Play Button
play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

# 7. Start the Tkinter event loop
root.mainloop()