import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter 

class DashboardApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('700x600')
        self.master.configure(bg="#FFFFFF")

        style = ttk.Style()
        style.configure('TButton', background='#FFFFFF')

        self.full_name_label = ttk.Label(master, background="#FFFFFF", text="Full Name")
        self.full_name_label.pack()

        self.name_entry = ttk.Entry(master)
        self.name_entry.pack()

        self.gender_label = ttk.Label(master, background="#FFFFFF", text="Sex")
        self.gender_label.pack()
        gender_options = ["Male", "Female"]
        self.gender_var = tk.StringVar(master)
        self.gender_var.set(gender_options[0])
        self.gender_menu = tk.OptionMenu(master, self.gender_var, *gender_options)
        self.gender_menu.config(bg='#FFFFFF')
        self.gender_menu.pack()

        self.contacts_label = ttk.Label(master, background="#FFFFFF", text="Contacts")
        self.contacts_label.pack()

        self.contacts_entry = ttk.Entry(master)
        self.contacts_entry.pack()

        self.height_label = ttk.Label(master, background="#FFFFFF", text="Height(cm)")
        self.height_label.pack()

        self.height_entry = ttk.Entry(master)
        self.height_entry.pack()

        self.weight_label = ttk.Label(master, background="#FFFFFF", text="Weight(kg)")
        self.weight_label.pack()

        self.weight_entry = ttk.Entry(master)
        self.weight_entry.pack()

        self.diagnosis_label = ttk.Label(master, background="#FFFFFF", text="Diagnosis")
        self.diagnosis_label.pack()

        self.diagnosis_entry = ttk.Entry(master)
        self.diagnosis_entry.pack()

        self.blood_type_label = ttk.Label(master, background="#FFFFFF", text="Blood Type")
        self.blood_type_label.pack()

        blood_type_options = ["A", "B", "AB", "O"]
        self.blood_type_var = tk.StringVar(master)
        self.blood_type_var.set(blood_type_options[0])
        self.blood_type_menu = tk.OptionMenu(master, self.blood_type_var, *blood_type_options)
        self.blood_type_menu.config(bg='#FFFFFF')
        self.blood_type_menu.pack()

        self.submit_button = ttk.Button(master, text="Submit", style='TButton')
        self.submit_button.pack()

        # Keep a reference to tk_image at the class level
        self.tk_image = self.add_image_top_center()
    def add_image_top_center(self):
        # Load your image using Pillow
        image_path = "/home/akira/Downloads/preview.png"
        pil_image = Image.open(image_path)

        # Add transparent padding to the image
        padding = 10  # Adjust the padding as needed
        padded_image = Image.new("RGBA", (pil_image.width + 2 * padding, pil_image.height + 2 * padding), (0, 0, 0, 0))
        padded_image.paste(pil_image, (padding, padding))

        # Resize the image to the desired dimensions using a different resampling method
        resized_width = 150  # Adjust the width as needed
        resized_height = 150  # Adjust the height as needed
        pil_image = padded_image.resize((resized_width, resized_height), Image.BICUBIC)

        # Create a new image with a white background
        new_image = Image.new("RGBA", (resized_width, resized_height), "#FFFFFF")

        # Paste the resized image onto the new image
        new_image.paste(pil_image, (0, 0), pil_image)

        # Convert the new image to Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(new_image)

        # Create a Canvas
        canvas = tk.Canvas(self.master, width=resized_width, height=resized_height)
        canvas.pack()

        # Draw the image on the Canvas at the top center
        canvas.create_image(resized_width // 2, 0, anchor=tk.N, image=tk_image)

        # Return the reference to tk_image
        return tk_image

if __name__ == "__main__":
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    app = DashboardApp(root)
    root.mainloop()
