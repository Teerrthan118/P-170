from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Project 170")
root.geometry("500x500")
root.configure(background="lightblue")

percentage_grade_3_label = Label(root, text="")
percentage_grade_5_label = Label(root, text="")
percentage_grade_10_label = Label(root, text="")

class grade3:
    def __init__(self,language_arts,mathematics):
        self.language_arts = language_arts
        self.mathematics = mathematics
        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks_with_100 / 200
        percentage_grade_3_label["text"] = grade_3_percentage
        
class grade5:
    def __init__(self,language_arts,mathematics,social_studies):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies

        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies
        total_marks_with_100 = total_marks * 100
        grade_5_percentage = total_marks_with_100 / 300
        percentage_grade_5_label["text"] = grade_5_percentage
        
class grade10:
    def __init__(self,language_arts,mathematics,social_studies,foreign_language):
        self.language_arts = language_arts
        self.mathematics = mathematics
        self.social_studies = social_studies
        self.foreign_language = foreign_language

        
    def percentage(self):
        total_marks = self.language_arts + self.mathematics + self.social_studies + self.foreign_language
        total_marks_with_100 = total_marks * 100
        grade_10_percentage = total_marks_with_100 / 400
        percentage_grade_10_label["text"] = grade_10_percentage

object_grade_3 = grade3(40,50)

button1 = Button(root, text="Grade 3", command = object_grade_3.percentage)
button1.pack()
percentage_grade_3_label.pack()

object_grade_5 = grade5(40,50,90)

button2 = Button(root, text="Grade 5", command = object_grade_5.percentage)
button2.pack()
percentage_grade_5_label.pack()

object_grade_10 = grade10(40,50,90,80)

button3 = Button(root, text="Grade 10", command = object_grade_10.percentage)
button3.pack()
percentage_grade_10_label.pack()

root.mainloop()