import tkinter as tk
from tkinter import ttk

def validate_email():
    email = email_entry.get()
    k, j, d = 0, 0, 0

    if len(email) >= 10:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        result_label.config(text="Wrong Email")
                        green_label.place_forget()
                        red_label.place(x=180, y=260)
                    else:
                        result_label.config(text="Correct Email")
                        red_label.place_forget()
                        green_label.place(x=180, y=260)
                else:
                    result_label.config(text="Wrong Email")
                    green_label.place_forget()
                    red_label.place(x=180, y=260)
            else:
                result_label.config(text="Wrong Email")
                green_label.place_forget()
                red_label.place(x=180, y=260)
        else:
            result_label.config(text="Wrong Email")
            green_label.place_forget()
            red_label.place(x=180, y=260)
    else:
        result_label.config(text="Wrong Email")
        green_label.place_forget()
        red_label.place(x=180, y=260)

window = tk.Tk()
window.title("Email Validator")

window.geometry("400x350")

email_label = ttk.Label(window, text="Enter Your E-mail:")
email_label.pack(pady=(20,0))

email_entry = ttk.Entry(window, width=30)
email_entry.pack(pady=(0,10))

button_frame = ttk.Frame(window)
button_frame.pack(pady=(0,10))

validate_button = ttk.Button(button_frame, text="Validate Email", command=validate_email, style='TButton')
validate_button.pack(ipadx=10, ipady=5)

result_label = ttk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=(10,20))

green_label = ttk.Label(window, text="✓", font=("Helvetica", 24), foreground="green")
red_label = ttk.Label(window, text="✗", font=("Helvetica", 24), foreground="red")

green_label.place(x=180, y=260)

window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

window.mainloop()
