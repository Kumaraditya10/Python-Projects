# import tkinter as tk
# from PIL import Image, ImageTk
# import itertools
# import os


# root = tk.Tk()
# root.title("Image Slideshow Viewer")
# root.resizable(False, False)


# image_paths = [
#     r"C:\path\to\your\image1.jpg",
#     r"C:\path\to\your\image2.jpg",
#     r"C:\path\to\your\image3.jpg",
# ]


# IMAGE_SIZE   = (800, 600)
# photo_images = []

# for path in image_paths:
#     if not os.path.exists(path):
#         print(f"File not found, skipping: {path}")
#         continue
#     try:
#         img = Image.open(path).resize(IMAGE_SIZE, Image.Resampling.LANCZOS)
#         photo_images.append(ImageTk.PhotoImage(img))
#     except Exception as e:
#         print(f"Error loading {path}: {e}")


# if not photo_images:
#     print("No images loaded. Please update 'image_paths' with valid file paths.")
#     root.destroy()
#     raise SystemExit


# label = tk.Label(root)
# label.pack()

# slideshow    = itertools.cycle(photo_images)
# after_id     = None          
# running      = False         

# def show_next():
#     """Advance to the next image and schedule another call."""
#     img = next(slideshow)
#     label.config(image=img)

# def start_slideshow():
#     """Start (or resume) the slideshow; ignore if already running."""
#     global after_id, running
#     if running:
#         return                       
#     running = True
#     play_button.config(state=tk.DISABLED)
#     stop_button.config(state=tk.NORMAL)
#     _loop()

# def stop_slideshow():
#     """Pause the slideshow."""
#     global after_id, running
#     running = False
#     if after_id is not None:
#         root.after_cancel(after_id)  
#         after_id = None
#     play_button.config(state=tk.NORMAL)
#     stop_button.config(state=tk.DISABLED)

# def _loop():
#     """Internal: show next image, then schedule itself after 3 seconds."""
#     global after_id
#     if not running:
#         return
#     show_next()
#     after_id = root.after(3000, _loop)


# controls = tk.Frame(root)
# controls.pack(pady=6)

# play_button = tk.Button(controls, text="▶  Start", width=12, command=start_slideshow)
# play_button.grid(row=0, column=0, padx=4)

# stop_button = tk.Button(controls, text="⏹  Stop", width=12, command=stop_slideshow,
#                         state=tk.DISABLED)
# stop_button.grid(row=0, column=1, padx=4)


# show_next()

# root.mainloop()