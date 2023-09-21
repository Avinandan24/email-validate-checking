import tkinter as tk

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
                    else:
                        result_label.config(text="Correct Email")
                else:
                    result_label.config(text="Wrong Email")
            else:
                result_label.config(text="Wrong Email")
        else:
            result_label.config(text="Wrong Email")
    else:
        result_label.config(text="Wrong Email")


window = tk.Tk()
window.title("Email Validator")

window.geometry("400x200")

email_label = tk.Label(window, text="Enter Your E-mail:")
email_label.pack(pady=(20,0))

email_entry = tk.Entry(window, width=30)
email_entry.pack(pady=(0,10))

validate_button = tk.Button(window, text="Validate Email", command=validate_email)
validate_button.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 16))
result_label.pack(pady=(10,20))


window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


window.mainloop()
