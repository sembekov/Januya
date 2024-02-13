import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FeedbackWindow:
    def __init__(self, master):
        self.feedback_window = tk.Toplevel(master)
        self.feedback_window.title("Feedback and Ratings")
        self.feedback_window.geometry('400x300')
        self.feedback_window.configure(bg="#FFFFFF")

        feedback_label = ttk.Label(self.feedback_window, text="Leave your feedback and rating", font=("Arial", 16), background='#FFFFFF')
        feedback_label.pack(pady=10)

        # Rating Scale
        self.rating_var = tk.IntVar()
        rating_label = ttk.Label(self.feedback_window, text="Rating:", font=("Arial", 14), background='#FFFFFF')
        rating_label.pack()
        rating_scale = ttk.Scale(self.feedback_window, from_=1, to=5, orient=tk.HORIZONTAL, variable=self.rating_var)
        rating_scale.pack(pady=10)

        # Feedback Textbox
        self.feedback_text = tk.StringVar()
        feedback_entry = ttk.Entry(self.feedback_window, textvariable=self.feedback_text, font=("Arial", 14))
        feedback_entry.pack(pady=10)

        # Submit Button
        submit_button = ttk.Button(self.feedback_window, text="Submit", command=self.submit_feedback, style='TButton')
        submit_button.pack(pady=10)

    def submit_feedback(self):
        # Retrieve feedback and rating
        feedback = self.feedback_text.get()
        rating = self.rating_var.get()

        # Validate if both feedback and rating are provided
        if not feedback or rating == 0:
            messagebox.showwarning("Warning", "Please provide both feedback and rating.")
        else:
            # Process feedback (you can store it in a database or perform other actions)
            # For now, display a message
            messagebox.showinfo("Feedback Submitted", "Thank you for your feedback and rating!")
            # Close the feedback window
            self.feedback_window.destroy()
