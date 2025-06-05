# limite de caracteres minimos e maximos na senha
import tkinter as tk, string, random

copy_button_created = False
copy_button = None

def copy_password():
    password = label2["text"]
    main.clipboard_clear()
    main.clipboard_append(password)
    main.update()

def create_copy_button(action):
    global copy_button_created, copy_button
    
    if action == "delete":
        if copy_button is not None:
            copy_button.destroy()
            copy_button = None
            copy_button_created = False

    elif action == "create":
        if not copy_button_created:
            copy_button = tk.Button(main, text="Copy", command=copy_password)
            copy_button.pack(pady=10)
            copy_button_created = True

def generate_password():
    global copy_button_created
    try:
        quantity = int(user_input.get())
        if quantity < 6 or quantity > 12:
            label2["text"] = "Minimum characters: 6\nMaximum characters: 12"
            create_copy_button("delete")
        else:
            caracteres = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(caracteres) for _ in range (quantity))
            label2["text"] = password
            create_copy_button("create")

    except ValueError:
        if not user_input.get():
            label2["text"] = "Empty input"
        else:
            label2["text"] = "Only integer numbers"
            if copy_button_created == True:
                copy_button_created == False
                create_copy_button("delete")
            
main = tk.Tk()
main.title("Password generator")
main.geometry("400x300")

label = tk.Label(main, text="Number of characters in the password")
label.pack(pady=10)

user_input = tk.Entry(main)
user_input.pack(pady=10)

button_generate_password = tk.Button(main, text="Generate password", command=generate_password)
button_generate_password.pack(pady=10)

label2 = tk.Label(main, text="")
label2.pack(pady=10)

main.mainloop()
