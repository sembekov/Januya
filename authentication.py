import tkinter as tk
from tkinter import ttk, messagebox
from emergency import Emergency
import subprocess  # Import subprocess module

def login():
    call(["python", "authentication.py"])

def register():
    # Add your registration logic here
    subprocess.run(["python", "registration_info.py"])



def emergency():
    # Remove widgets managed by grid in the register_frame
    for widget in register_frame.winfo_children():
        widget.grid_remove()

    # Create and raise the Emergency frame in the same container (register_tab)
    emergency_frame = Emergency(register_tab)
    emergency_frame.grid(row=0, column=0, sticky="nsew")
    emergency_frame.tkraise()



window = tk.Tk()
window.attributes("-fullscreen", True)
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#FFFFFF')
style = ttk.Style()
style.configure('TButton', background='#FFFFFF')
# Create a Notebook (tabbed layout)
notebook_style = ttk.Style()
notebook_style.configure('My.TNotebook', background='#FFFFFF')

notebook = ttk.Notebook(window, style='My.TNotebook')

# Create tabs
login_tab = ttk.Frame(notebook, style='My.TFrame')
register_tab = ttk.Frame(notebook, style='My.TFrame')

notebook.add(login_tab, text="Login")
notebook.add(register_tab, text="Registration")

notebook.pack(pady=10)

# Style for the tabs
style = ttk.Style()
style.configure('My.TFrame', background='#FFFFFF')

# Login Tab
login_frame = ttk.Frame(login_tab, padding="10", style='My.TFrame')
login_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

login_label = ttk.Label(login_frame, text="Login", font=("Arial", 20), background='#FFFFFF', foreground="#3de045")
login_label.grid(row=0, column=0, columnspan=2, pady=20)

iin_label = ttk.Label(login_frame, text="IIN", background='#FFFFFF', foreground="#000000")
iin_entry = ttk.Entry(login_frame, font=("Arial", 16))
password_label = ttk.Label(login_frame, text="Password ", background='#FFFFFF', foreground="#000000")
password_entry = ttk.Entry(login_frame, show="*", font=("Arial", 16))

login_button = ttk.Button(login_frame, text="Login", command=login)

iin_label.grid(row=1, column=0)
iin_entry.grid(row=1, column=1, pady=10)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=10)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

# Register Tab
register_frame = ttk.Frame(register_tab, padding="10", style='My.TFrame')
register_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

register_label = ttk.Label(register_frame, text="Registration", font=("Arial", 20), background='#FFFFFF', foreground="#3de045")
register_label.grid(row=0, column=0, columnspan=2, pady=20)

new_iin_label = ttk.Label(register_frame, text="IIN", background='#FFFFFF', foreground="#000000")
new_iin_entry = ttk.Entry(register_frame, font=("Arial", 16))
new_password_label = ttk.Label(register_frame, text="New Password ", background='#FFFFFF', foreground="#000000")
new_password_entry = ttk.Entry(register_frame, show="*", font=("Arial", 16))

register_button = ttk.Button(register_frame, text="Register", command=register)
emergency_button = tk.Button(register_frame, text='Emergency', bg='red', command=emergency)

new_iin_label.grid(row=2, column=0)
new_iin_entry.grid(row=2, column=1, pady=10)
new_password_label.grid(row=3, column=0)
new_password_entry.grid(row=3, column=1, pady=10)


# Place buttons in the grid
register_button.grid(row=4, column=1, pady=20, sticky='ew')
emergency_button.grid(row=4, column=0, pady=20, sticky='ew')

window.mainloop()
