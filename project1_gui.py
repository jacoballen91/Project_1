from tkinter import *
from project1_student import *


class Gui:
    def __init__(self, window):
        self.window = window
        self.blank_attempt1 = StringVar()
        self.blank_attempt1.set('0')
        self.blank_attempt2 = StringVar()
        self.blank_attempt2.set('0')
        self.blank_attempt3 = StringVar()
        self.blank_attempt3.set('0')
        self.blank_attempt4 = StringVar()
        self.blank_attempt4.set('0')
        self.attempts_collected = False
        self.student = ''

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Student Name:\t\t')
        self.entry_name = Entry(self.frame_name, width=40)
        self.label_name.pack(padx=20, side='left')
        self.entry_name.pack(padx=20, side='left')
        self.entry_name.focus()
        self.frame_name.pack(anchor='w', pady=10)

        self.frame_attempts = Frame(self.window)
        self.label_attempts = Label(self.frame_attempts, text='Number of Attempts:\t')
        self.entry_attempts = Entry(self.frame_attempts, width=40)
        self.label_attempts.pack(padx=20, side='left')
        self.entry_attempts.pack(padx=20, side='left')
        self.frame_attempts.pack(anchor='w', pady=10)

        self.frame_attempt1 = Frame(self.window)
        self.label_attempt1 = Label(self.frame_attempt1, text='Attempt 1:\t\t')
        self.entry_attempt1 = Entry(self.frame_attempt1, textvariable=self.blank_attempt1, width=40)
        self.label_attempt1.pack(padx=20, side='left')
        self.entry_attempt1.pack(padx=20, side='left')
        self.frame_attempt1.pack(anchor='w', pady=10)
        self.frame_attempt1.pack_forget()

        self.frame_attempt2 = Frame(self.window)
        self.label_attempt2 = Label(self.frame_attempt2, text='Attempt 2:\t\t')
        self.entry_attempt2 = Entry(self.frame_attempt2, textvariable=self.blank_attempt2, width=40)
        self.label_attempt2.pack(padx=20, side='left')
        self.entry_attempt2.pack(padx=20, side='left')
        self.frame_attempt2.pack(anchor='w', pady=10)
        self.frame_attempt2.pack_forget()

        self.frame_attempt3 = Frame(self.window)
        self.label_attempt3 = Label(self.frame_attempt3, text='Attempt 3:\t\t')
        self.entry_attempt3 = Entry(self.frame_attempt3, textvariable=self.blank_attempt3, width=40)
        self.label_attempt3.pack(padx=20, side='left')
        self.entry_attempt3.pack(padx=20, side='left')
        self.frame_attempt3.pack(anchor='w', pady=10)
        self.frame_attempt3.pack_forget()

        self.frame_attempt4 = Frame(self.window)
        self.label_attempt4 = Label(self.frame_attempt4, text='Attempt 4:\t\t')
        self.entry_attempt4 = Entry(self.frame_attempt4, textvariable=self.blank_attempt4, width=40)
        self.label_attempt4.pack(padx=20, side='left')
        self.entry_attempt4.pack(padx=20, side='left')
        self.frame_attempt4.pack(anchor='w', pady=10)
        self.frame_attempt4.pack_forget()

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='SUBMIT', command=self.submit)
        self.button_submit.pack(pady=10)
        self.frame_submit.pack()

        self.frame_scores = Frame(self.window)
        self.label_scores_message = Label(self.frame_scores)
        self.label_scores_message.pack(pady=10)
        self.frame_scores.pack_forget()

        self.frame_new_student = Frame(self.window)
        self.button_new_student = Button(self.frame_new_student, text='NEW STUDENT', command=self.new_student)
        self.button_new_student.pack(pady=10)
        self.frame_new_student.pack_forget()

    def submit(self):
        self.label_result.config(text='')
        if not self.attempts_collected:
            try:
                self.student = Student(self.entry_name.get())
                num_attempts = self.student.check_attempts(self.entry_attempts.get())
                self.frame_result.pack_forget()
                self.label_result.config(fg='green', text=f'Enter {self.student.student_name}\'s scores for each attempt')
                self.frame_result.pack()
                self.entry_attempt1.focus()
                if num_attempts >= 1:
                    self.frame_attempt1.pack()
                    if num_attempts >= 2:
                        self.frame_attempt2.pack()
                        if num_attempts >= 3:
                            self.frame_attempt3.pack()
                            if num_attempts == 4:
                                self.frame_attempt4.pack()
                self.frame_submit.pack_forget()
                self.frame_submit.pack()
                self.attempts_collected = True
            except NameError:
                self.entry_name.focus()
                self.label_result.config(fg='red', text='Student name cannot be blank')
            except TypeError:
                self.entry_attempts.focus()
                self.label_result.config(fg='red', text='Enter number of attempts between 1 and 4')
            except ValueError:
                self.entry_attempts.focus()
                self.label_result.config(fg='red', text='Enter a number for number of attempts')
        else:
            try:
                self.label_scores_message.config(fg='green', text=f'{self.student.student_name}\'s final score is '
                                                                  f'{self.student.get_grade(self.entry_attempt1.get(), self.entry_attempt2.get(), self.entry_attempt3.get(), self.entry_attempt4.get())}')
                self.frame_scores.pack()
                self.frame_result.pack_forget()
                self.frame_submit.pack_forget()
                self.frame_new_student.pack()
            except TypeError:
                self.entry_attempt1.focus()
                self.label_scores_message.config(fg='red', text='Enter a score 0-100')
                self.frame_scores.pack()
            except ValueError:
                self.entry_attempt1.focus()
                self.label_scores_message.config(fg='red', text='Scores must be numeric')
                self.frame_scores.pack()

    def new_student(self):
        self.entry_name.delete(0, END)
        self.entry_attempts.delete(0, END)
        self.blank_attempt1 = StringVar()
        self.blank_attempt1.set('0')
        self.blank_attempt2 = StringVar()
        self.blank_attempt2.set('0')
        self.blank_attempt3 = StringVar()
        self.blank_attempt3.set('0')
        self.blank_attempt4 = StringVar()
        self.blank_attempt4.set('0')
        self.entry_attempt1.config(textvariable=self.blank_attempt1)
        self.entry_attempt2.config(textvariable=self.blank_attempt2)
        self.entry_attempt3.config(textvariable=self.blank_attempt3)
        self.entry_attempt4.config(textvariable=self.blank_attempt4)
        self.frame_attempt1.pack_forget()
        self.frame_attempt2.pack_forget()
        self.frame_attempt3.pack_forget()
        self.frame_attempt4.pack_forget()
        self.frame_scores.pack_forget()
        self.frame_new_student.pack_forget()
        self.attempts_collected = False
        self.frame_name.pack()
        self.frame_attempts.pack()
        self.frame_submit.pack()
        self.entry_name.focus()
        self.frame_result.pack()
