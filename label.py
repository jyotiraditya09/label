from tkinter import *

root = Tk()
root.title("Identity Card")
root.geometry("300x400")

root.configure(bg="yellow")
canvas = Canvas(root, width=300, height=400)
canvas.create_rectangle(0, 0, 300, 55, fill="#bf2626")
canvas.create_rectangle(0, 345, 300, 400, fill="#bf2626")

label_heading = canvas.create_text(150, 90, font=("Times", "24", "bold italic"), text="Identity card")
label_name_tag = canvas.create_text(40, 165, font=("Times", "16", "bold"), text="Name: ")
label_grade_tag = canvas.create_text(40, 205, font=("Times", "16", "bold"), text="Grade: ")
label_subjects_tag = canvas.create_text(40, 250, font=("Times", "16", "bold"), text="Subjects: ")

label_name = Label(root)
label_grade = Label(root)
label_subjects = Label(root)


def myCardDetails():
    name = "Mrityunjay"
    print(type(name))
    grade = 7
    print(type(grade))
    subjects = ["Math", "Programming"]
    print(type(subjects))

    label_name['text'] = name
    label_grade['text'] = grade
    label_subjects['text'] = subjects


button_1 = Button(root, command=myCardDetails, bg="yellow", text="Show my id card")
button_1.configure(width=20, activebackground="#bf2626", relief=FLAT)

button_1_window = canvas.create_window(150, 330, anchor=CENTER, window=button_1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(155, 255, anchor=CENTER, window=label_subjects)
canvas.pack()

root.mainloop()
