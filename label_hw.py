from tkinter import *

root = Tk()
root.title("Driving license")
root.geometry("500x400")

root.configure(bg="white")
canvas = Canvas(root, width=500, height=400)
canvas.create_rectangle(0, 0, 500, 80, fill="#bf2626")


label_heading = canvas.create_text(250, 50, font=("Times", "24", "bold italic"), fill="white", text="Driving license")
label_id_tag = canvas.create_text(40, 100, font=("Times", "18", "bold"), text="ID: ")
label_name_tag = canvas.create_text(40, 165, font=("Times", "16", "bold"), text="Name: ")
label_dob_tag = canvas.create_text(40, 205, font=("Times", "16", "bold"), text="DOB: ")
label_pin_tag = canvas.create_text(40, 250, font=("Times", "16", "bold"), text="Pin: ")

label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)

def myCardDetails():
    id = 1113331
    print(type(id))
    name = "Mrityunjay"
    print(type(name))
    dob = "5th August"
    print(type(dob))
    pin = "300110"
    print(type(pin))

    label_id['text'] = id
    label_name['text'] = name
    label_dob['text'] = dob
    label_pin['text'] = pin


button_1 = Button(root, command=myCardDetails, bg="yellow", text="Show license details")
button_1.configure(width=20, activebackground="#bf2626", relief=FLAT)

button_1_window = canvas.create_window(150, 330, anchor=CENTER, window=button_1)
label_id_window = canvas.create_window(100, 100, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(120, 205, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(110, 255, anchor=CENTER, window=label_pin)
canvas.pack()

root.mainloop()
