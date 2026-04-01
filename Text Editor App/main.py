import tkinter as tk
from tkinter import filedialog, messagebox

# Function to create a new file (clears the text area)
def new_file():
    text_area.delete(1.0, tk.END) 

# Function to open an existing text file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text_area.insert(tk.INSERT, file.read()) 

# Function to save the current text to a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
            messagebox.showinfo("Success", "File saved successfully!") 

# Main Root Window Setup
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600") 

# Creating the Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Adding File Menu and its options
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit) 

# Creating the Text Widget (Blue text with Helvetica font)
text_area = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue")
text_area.pack(expand=True, fill='both') 

# Running the application
root.mainloop() 