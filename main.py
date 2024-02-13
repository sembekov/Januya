import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import subprocess 

def login():
    subprocess.run(["python", "authentication.py"])

window = tk.Tk()
window.attributes("-fullscreen", True)
window.title("Start Page")
window.geometry('1420x800')

window.configure(bg="white")

text_label = tk.Label(window, text="Let's take care of your health together! \n At 'Zhanya' we are\n committed to providing outstanding \nhealthcare services in a comfortable\n and supportive environment. \n Our mission is to help patients achieve\n optimal health and well-being.",bg="white",fg="#3de045")


text_label.config(font=("Courier", 22))


text_label.pack(pady=10, padx=10, side="left")

text_label.place(x=100,y=250)
window.configure(bg="white")


image_path = "preview.jpg"
pil_image = Image.open(image_path)


tk_image = ImageTk.PhotoImage(pil_image)

label = tk.Label(window, image=tk_image,bd=0)
label.pack(padx=10, pady=10)
label.place(x=800,y=100)
label.config(width=500, height=500)

canvas = tk.Canvas(window, width=1400, height=100)
canvas.pack()

canvas.create_line(150, 50, 150, 150, fill='#00c741', width=3300)
canvas.place(x=0,y=-50)

btn = tk.Button(window, text="Login", bg="white", fg="#00c741", command=login)
btn.pack()
btn.place(x=1315, y=5)
btn.config(width=5, height=2)

btn3 = tk.Button(window, text="Contact us", bg="white", fg="#00c741")
btn3.pack()
btn3.place(x=250,y=500)
btn3.config(width=50, height=5)

root = tk.Toplevel(window)
root.geometry('1420x800')
root.withdraw()

root.mainloop()
