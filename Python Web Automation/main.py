import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Function to search on YouTube
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# Function to search on Google
def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Function to search on Instagram
def search_instagram():
    query = entry.get()
    # Cleaning the username for Instagram URL
    username = query.replace("@", "")
    url = f"https://www.instagram.com/{username}"
    webbrowser.open(url)

# Initializing the main window
root = tk.Tk()
root.title("Your AI Assistant")
root.configure(bg="steel blue")  # Setting background color 

# Creating Input Label
label = Label(root, text="Enter Your Command", bg="steel blue", fg="white", font=("Arial", 12, "bold"))
label.pack(pady=10)

# Creating Input Entry Field
entry = Entry(root, width=50)
entry.pack(pady=10)

# Creating Buttons with associated functions
# YouTube Button 
btn_youtube = Button(root, text="Search on YouTube", command=search_youtube)
btn_youtube.pack(pady=5)

# Google Button 
btn_google = Button(root, text="Search on Google", command=search_google)
btn_google.pack(pady=5)

# Instagram Button 
btn_instagram = Button(root, text="View Instagram Profile", command=search_instagram)
btn_instagram.pack(pady=5)

# Running the application 
root.mainloop()