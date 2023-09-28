import tkinter

window = tkinter.Tk()
window.title("Ward's GUI oi oi")
window.minsize(400, 200)
window.config(padx=50, pady=50)

input = tkinter.Entry(width=7)
input.grid(column=1, row=0)

miles = tkinter.Label(text="Miles", font=("Arial", 12))
miles.grid(column=2, row=0)

is_equal = tkinter.Label(text="is equal to", font=("Arial", 12))
is_equal.grid(column=0, row=1)

km_label = tkinter.Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

result = tkinter.Label(text="0", font=("Arial", 12))
result.grid(column=1, row=1)


def convert_to_km():
    km = round(int(input.get()) * 1.6)
    result.config(text=km)

button = tkinter.Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)


window.mainloop()