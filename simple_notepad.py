import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        with open(file_path, 'r') as file:
            text.delete("1.0", tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get("1.0", tk.END))

def about():
    messagebox.showinfo("About", "Simple Notepad\nCreated with Python and Tkinter")

root = tk.Tk()
root.title("Simple Notepad")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

root.mainloop()
