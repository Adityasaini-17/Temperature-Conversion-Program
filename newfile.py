from tkinter import * 

def convert_temperature():
    try:
        temp_value = float(entry.get())
        
        if selected_conversion.get() == 1:  
            fahrenheit = (temp_value * 9/5) + 32
            kelvin = temp_value + 273.15
            result.set(f"{temp_value}°C => {fahrenheit:.2f}°F => {kelvin:.2f}K")
            
        elif selected_conversion.get() == 2:  
            celsius = (temp_value - 32) * 5/9
            kelvin = (temp_value - 32) * 5/9 + 273.15
            result.set(f"{temp_value}°F => {celsius:.2f}°C => {kelvin:.2f}K")
        elif selected_conversion.get() == 3: 
            celsius = temp_value - 273.15
            fahrenheit = (temp_value - 273.15) * 9/5 + 32
            result.set(f"{temp_value}K => {celsius:.2f}°C => {fahrenheit:.2f}°F")
    except ValueError:
        result.set("Please enter a valid number.")

root = Tk()
root.title("Temperature Converter")
root.geometry("390x400")
root.resizable(False, False)

result = StringVar()
selected_conversion = IntVar()

# Entry temperature value
entry_label = Label(root, text="Enter Temperature:", font="lucida 12")
entry_label.pack(pady=10)

entry = Entry(root, font="lucida 14")
entry.pack(pady=5)

# Radiobuttons conversion options
conversion_frame = Frame(root)
conversion_frame.pack(pady=10)

celsius_radio = Radiobutton(conversion_frame, text="Celsius", variable=selected_conversion, value=1, font="lucida 12")
celsius_radio.grid(row=0, column=0, padx=10, pady=5, sticky=W) 

fahrenheit_radio = Radiobutton(conversion_frame, text="Fahrenheit", variable=selected_conversion, value=2, font="lucida 12")
fahrenheit_radio.grid(row=1, column=0, padx=10, pady=5, sticky=W)

kelvin_radio = Radiobutton(conversion_frame, text="Kelvin", variable=selected_conversion, value=3, font="lucida 12")
kelvin_radio.grid(row=2, column=0, padx=10, pady=5, sticky=W)

# perform conversion
convert_button = Button(root, text="Convert", command=convert_temperature, font="lucida 12")
convert_button.pack(pady=10)

# display results
result_label = Label(root, textvariable=result, font="lucida 12 bold")
result_label.pack(pady=10)

# main loop
root.mainloop()
