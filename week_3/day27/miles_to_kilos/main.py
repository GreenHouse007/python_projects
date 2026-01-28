from tkinter import *

def miles_to_kilo():
    miles = float(miles_input.get())
    kn = miles * 1.609
    kilometer_result_lable.config(text=f"{kn}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30, pady=30)

miles_input = Entry(width = 7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_lable = Label(text="0")
kilometer_result_lable.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=miles_to_kilo)
calculate_button.grid(row=2, column=1)


window.mainloop()