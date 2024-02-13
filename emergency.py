import tkinter as tk
from tkinter import ttk, messagebox

class Emergency(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg='white')

        self.iin_label = ttk.Label(self, text="IIN:")
        self.iin_label.grid(row=0, column=0, padx=10, pady=10)

        self.diagnosis_label = ttk.Label(self, text="Diagnosis:")
        self.diagnosis_label.grid(row=1, column=0, padx=10, pady=10)

        self.contacts_label = ttk.Label(self, text="Contact Info:")
        self.contacts_label.grid(row=2, column=0, padx=10, pady=10)

        self.iin_entry = ttk.Entry(self)
        self.iin_entry.grid(row=0, column=1, padx=10, pady=10)

        self.diagnosis_entry = ttk.Entry(self)
        self.diagnosis_entry.grid(row=1, column=1, padx=10, pady=10)

        self.contacts_entry = ttk.Entry(self)
        self.contacts_entry.grid(row=2, column=1, padx=10, pady=10)

        self.submit_button = ttk.Button(self, text="Submit", command=self.handle_emergency)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=20)

    def handle_emergency(self):
        iin = self.iin_entry.get()
        diagnosis = self.diagnosis_entry.get()
        contacts = self.contacts_entry.get()

        # Implement your emergency handling logic here
        messagebox.showinfo(title="Emergency", message=f"IIN: {iin}, Diagnosis: {diagnosis}, Contacts: {contacts}")
