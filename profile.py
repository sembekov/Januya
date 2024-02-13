import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import random
from functions.feedback_window import FeedbackWindow

class ClinicSocialApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Clinic Social App")
        self.master.geometry('2000x800')
        self.master.configure(bg="#FFFFFF")

        # Left Sidebar with Functionalities
        self.sidebar_frame = tk.Frame(self.master, width=300, bg='#FFFFFF')
        self.sidebar_frame.grid(row=0, column=0, sticky=(tk.W, tk.N, tk.S), padx=(10, 0), pady=10)

        self.functionalities_label = tk.Label(self.sidebar_frame, text="Functionalities", font=("Arial", 18), bg='#FFFFFF', fg="#3de045")
        self.functionalities_label.grid(row=0, column=0, pady=15, sticky='w')

        self.appointment_button = tk.Button(self.sidebar_frame, text="Appointment", command=self.appointment_callback, font=("Arial", 16), bg='#FFFFFF', padx=10, pady=8)
        self.appointment_button.grid(row=1, column=0, pady=10, sticky='w')

        self.queue_button = tk.Button(self.sidebar_frame, text="Queue Status", command=self.queue_callback, font=("Arial", 16), bg='#FFFFFF', padx=10, pady=8)
        self.queue_button.grid(row=2, column=0, pady=10, sticky='w')

        self.medical_cards_button = tk.Button(self.sidebar_frame, text="Medical Cards", command=self.show_medical_cards_dialog, font=("Arial", 16), bg='#FFFFFF', padx=10, pady=8)
        self.medical_cards_button.grid(row=3, column=0, pady=10, sticky='w')

        self.consultation_button = tk.Button(self.sidebar_frame, text="Online Consultations", command=self.show_online_consultations_dialog, font=("Arial", 16), bg='#FFFFFF', padx=10, pady=8)
        self.consultation_button.grid(row=4, column=0, pady=10, sticky='w')

        self.feedback_button = tk.Button(self.sidebar_frame, text="Feedback and Ratings", command=self.open_feedback_window, font=("Arial", 16), bg='#FFFFFF', padx=10, pady=8)
        self.feedback_button.grid(row=5, column=0, pady=10, sticky='w')

        self.registration_button = tk.Button(self.sidebar_frame, text="Registration through IIN", command=self.registration_callback, font=("Arial", 16), bg='#FFFFFF', padx=10, pady=8)
        self.registration_button.grid(row=6, column=0, pady=10, sticky='w')

        # Vertical Line Separator
        tk.Frame(self.master, width=10, bg='#FFFFFF').grid(row=0, column=1, sticky='ns', padx=10, pady=10)

        # Right Frame for User Profile Information
        self.profile_frame = tk.Frame(self.master, bg='#FFFFFF')
        self.profile_frame.grid(row=0, column=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10), pady=10)

        # User Registration Information
        self.registration_label = tk.Label(self.profile_frame, text="Profile Information", font=("Arial", 18), bg='#FFFFFF', fg="#3de045")
        self.registration_label.grid(row=0, column=0, columnspan=2, pady=20, sticky='w')

        self.profile_name_label = tk.Label(self.profile_frame, text="Profile Name:", font=("Arial", 16), bg='#FFFFFF')
        self.profile_name_label.grid(row=1, column=0, pady=10, sticky='w')

        self.profile_name_entry = tk.Entry(self.profile_frame, font=("Arial", 16), state='readonly', bd=2, relief='groove')
        self.profile_name_entry.grid(row=1, column=1, pady=10, sticky='w')

        self.weight_label = tk.Label(self.profile_frame, text="Weight:", font=("Arial", 16), bg='#FFFFFF')
        self.weight_label.grid(row=2, column=0, pady=10, sticky='w')

        self.weight_entry = tk.Entry(self.profile_frame, font=("Arial", 16), state='readonly', bd=2, relief='groove')
        self.weight_entry.grid(row=2, column=1, pady=10, sticky='w')

        self.height_label = tk.Label(self.profile_frame, text="Height:", font=("Arial", 16), bg='#FFFFFF')
        self.height_label.grid(row=3, column=0, pady=10, sticky='w')

        self.height_entry = tk.Entry(self.profile_frame, font=("Arial", 16), state='readonly', bd=2, relief='groove')
        self.height_entry.grid(row=3, column=1, pady=10, sticky='w')

        self.blood_type_label = tk.Label(self.profile_frame, text="Blood Type:", font=("Arial", 16), bg='#FFFFFF')
        self.blood_type_label.grid(row=4, column=0, pady=10, sticky='w')

        self.blood_type_entry = tk.Entry(self.profile_frame, font=("Arial", 16), state='readonly', bd=2, relief='groove')
        self.blood_type_entry.grid(row=4, column=1, pady=10, sticky='w')

        self.age_label = tk.Label(self.profile_frame, text="Age:", font=("Arial", 16), bg='#FFFFFF')
        self.age_label.grid(row=5, column=0, pady=10, sticky='w')

        self.age_entry = tk.Entry(self.profile_frame, font=("Arial", 16), state='readonly', bd=2, relief='groove')
        self.age_entry.grid(row=5, column=1, pady=10, sticky='w')

        # Vertical Line Separator
        tk.Frame(self.master, width=10, bg='#FFFFFF').grid(row=0, column=3, sticky='ns', padx=10, pady=10)

    def show_medical_cards_dialog(self):
        # Создаем новое окно для отображения информации о медицинских картах
        medical_cards_window = tk.Toplevel(self.master)
        medical_cards_window.title("Medical Cards")
        medical_cards_window.geometry('600x400')  # Задайте размер окна по вашему усмотрению

        # Выводим текст о медицинских картах
        medical_info_label = tk.Label(medical_cards_window, text="Information about medical records", font=("Arial", 16), bg='#FFFFFF')
        medical_info_label.pack(pady=10)

        medical_info_text = """A medical card is a medical document in which the attending physicians record the patient's medical history and the treatment prescribed to him. The medical card of an outpatient patient is the main medical document of a patient undergoing examination and treatment in outpatient polyclinic conditions. It is filled in for each patient at the first request for medical help in a health facility. The medical card of an outpatient patient for citizens entitled to receive a set of social services is marked with the letter "L"."""

        medical_info_text_widget = scrolledtext.ScrolledText(medical_cards_window, wrap=tk.WORD, width=60, height=10, font=("Arial", 12))
        medical_info_text_widget.insert(tk.END, medical_info_text)
        medical_info_text_widget.pack(pady=10)

    def show_online_consultations_dialog(self):
        # Создаем новое окно для отображения диалога в режиме "Online Consultations"
        consultations_window = tk.Toplevel(self.master)
        consultations_window.title("Online Consultations")
        consultations_window.geometry('400x400')  # Задайте размер окна по вашему усмотрению

        # Добавим виджет прокрутки для отображения сообщений бота
        chat_text_widget = scrolledtext.ScrolledText(consultations_window, wrap=tk.WORD, width=40, height=15, font=("Arial", 12))
        chat_text_widget.pack(pady=10)

        # Добавим поле для ввода сообщений
        message_entry = tk.Entry(consultations_window, width=40, font=("Arial", 12))
        message_entry.pack(pady=10)

        # Добавим кнопку для отправки сообщения
        send_button = tk.Button(consultations_window, text="Send", command=lambda: self.send_message(chat_text_widget, message_entry), font=("Arial", 14))
        send_button.pack(pady=10)

        # Начинаем диалог
        self.bot_greet(chat_text_widget)

    def send_message(self, chat_widget, message_entry):
        # Получим текст из поля ввода
        message = message_entry.get().strip()

        # Если текст не пустой, добавим его в виджет чата и очистим поле ввода
        if message:
            chat_widget.insert(tk.END, f"You: {message}\n")
            message_entry.delete(0, tk.END)

            # Отправим ответ бота
            self.bot_response(chat_widget, message)

    def bot_greet(self, chat_widget):
        # Приветствие от бота
        greet_messages = [
            "Hi! How can I help you today?",
            "Good afternoon! How can I help?",
            "Hello! I am ready to answer your questions."
        ]

        greeting = random.choice(greet_messages)
        chat_widget.insert(tk.END, f"Bot: {greeting}\n")

    def bot_response(self, chat_widget, user_message):
        # Простая логика ответа бота
        responses = {
            "hi": "Hi! How can I help you?",
            "how are you": "I'm doing great, thank you! How are you?",
            "what are you doing": "I answer questions. How can I help you?"
            # Добавьте свои вопросы и ответы по необходимости
        }

        # Переводим в нижний регистр для удобства сравнения
        user_message_lower = user_message.lower()

        # Получаем ответ бота или предупреждение, если нет соответствия
        bot_reply = responses.get(user_message_lower, "I'm sorry, I didn't understand you. Can you clarify the question?")

        # Отправляем ответ бота в чат
        chat_widget.insert(tk.END, f"Bot: {bot_reply}\n")

    def appointment_callback(self):
        # Создаем новое окно для записи на прием
        appointment_window = tk.Toplevel(self.master)
        appointment_window.title("Appointment")
        appointment_window.geometry('500x400')  # Задайте размер окна по вашему усмотрению

        # Добавляем элементы для записи на прием
        date_label = tk.Label(appointment_window, text="Date of admission:", font=("Arial", 14))
        date_label.grid(row=0, column=0, pady=10)

        date_entry = tk.Entry(appointment_window, font=("Arial", 14))
        date_entry.grid(row=0, column=1, pady=10)

        time_label = tk.Label(appointment_window, text="Reception time:", font=("Arial", 14))
        time_label.grid(row=1, column=0, pady=10)

        time_entry = tk.Entry(appointment_window, font=("Arial", 14))
        time_entry.grid(row=1, column=1, pady=10)

        doctor_label = tk.Label(appointment_window, text="Choose a doctor:", font=("Arial", 14))
        doctor_label.grid(row=2, column=0, pady=10)

        # Заменим Entry на Combobox для выбора врача
        doctors = ["Doctor A", "Doctor B", "Doctor C"]  # Замените на свой список врачей
        doctor_combobox = ttk.Combobox(appointment_window, values=doctors, font=("Arial", 14))
        doctor_combobox.grid(row=2, column=1, pady=10)

        comment_label = tk.Label(appointment_window, text="Comment:", font=("Arial", 14))
        comment_label.grid(row=3, column=0, pady=10)

        comment_entry = tk.Entry(appointment_window, font=("Arial", 14))
        comment_entry.grid(row=3, column=1, pady=10)

        # Добавим кнопку для отправки заявки на прием
        submit_button = tk.Button(appointment_window, text="Make an appointment",
                                  command=lambda: self.submit_appointment(date_entry.get(), time_entry.get(),
                                                                          doctor_combobox.get(),
                                                                          comment_entry.get()), font=("Arial", 14))
        submit_button.grid(row=4, column=1, pady=20)

    def submit_appointment(self, date, time, doctor, comment):
        # Добавьте логику обработки записи на прием
        # Здесь может быть вызов API, отправка данных в базу данных и т.д.
        # В данном случае просто выведем информацию в консоль
        print(f"Date of admission: {date}")
        print(f"Reception time: {time}")
        print(f"Doctor: {doctor}")
        print(f"Comment: {comment}")

    def queue_callback(self):
        # Создаем новое окно для отображения статуса очереди
        queue_window = tk.Toplevel(self.master)
        queue_window.title("Queue Status")
        queue_window.geometry('500x400')  # Задайте размер окна по вашему усмотрению

        # Добавим виджет прокрутки для отображения информации о очереди
        queue_status_text_widget = scrolledtext.ScrolledText(queue_window, wrap=tk.WORD, width=40, height=15,
                                                             font=("Arial", 12))
        queue_status_text_widget.pack(pady=10)

        # Заглушка - добавим случайную информацию о состоянии очереди
        queue_info = "Queue status:\n1. Patient\n2. Patient B\n3. Patient In \n..."
        queue_status_text_widget.insert(tk.END, queue_info)

    def open_feedback_window(self):
        # Создаем объект окна обратной связи и открываем его
        feedback_window = FeedbackWindow(self.master)
        feedback_window.show_window()

    def registration_callback(self):
        # Создаем новое окно для регистрации через ИИН
        registration_window = tk.Toplevel(self.master)
        registration_window.title("Registration through IIN")
        registration_window.geometry('600x400')  # Задайте размер окна по вашему усмотрению

        # Добавим элементы для ввода ИИН и кнопку регистрации
        iin_label = tk.Label(registration_window, text="Enter IIN:", font=("Arial", 14))
        iin_label.grid(row=0, column=0, pady=20)

        iin_entry = tk.Entry(registration_window, font=("Arial", 14))
        iin_entry.grid(row=0, column=1, pady=20)

        register_button = tk.Button(registration_window, text="Register",
                                    command=lambda: self.register_user(iin_entry.get()), font=("Arial", 14))
        register_button.grid(row=1, column=0, columnspan=2, pady=20)

    def register_user(self, iin):
        # Добавьте логику регистрации пользователя через ИИН
        # Здесь может быть вызов API, проверка в базе данных и т.д.
        # В данном случае просто выведем информацию в консоль
        print(f"The user with the IIN {iin} has been successfully registered.")

# Главная часть программы - создаем объект приложения
root = tk.Tk()
root.attributes("-fullscreen", True)
app = ClinicSocialApp(root)
root.mainloop()
