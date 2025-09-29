import tkinter



window = tkinter.Tk()
window.title("Miles to km converter")
window.config(padx=20, pady=20)


miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1 ,row=0 )

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2 ,row=0 )

is_equal_lable = tkinter.Label(text="is equal to")
is_equal_lable.grid(column=0 ,row=1 )

kilometer_result_label = tkinter.Label(text="Km")
kilometer_result_label.grid(column=1 ,row=1)

def convert():
    km = float(miles_input.get()) * 1.60934
    kilometer_result_label.config(text=f"{km} km")

calculate_button = tkinter.Button(text="Calculate", command=convert)
calculate_button.grid(column=1 ,row=2 )




window.mainloop()
