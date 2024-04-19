import tkinter as tk

def change_text():
    label.config(text="Button clicked!")

root = tk.Tk()
root.title("Basic GUI App")
root.geometry("300x100")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

button = tk.Button(root, text="Click me!", command=change_text)
button.pack()

root.mainloop()