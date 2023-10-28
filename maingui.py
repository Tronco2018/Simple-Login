import tkinter as tk

#font
title_font = ("Arial", 16, "bold")
#user names list
user_list = ["Tronco", "Komm", "James", "Carl"]
#creating fin
fin = tk.Tk()

#fin title
fin.title("Login")

#fin size
fin.geometry("400x200")

#text welcome
label = tk.Label(fin, text="Welcome!", font=title_font, fg="black")
label.pack()

#login
label2 = tk.Label(fin, text="Username")
label2.pack()

# Casella di input(userame)
username_input = tk.Entry(fin)
username_input.pack()

#pass
label3 = tk.Label(fin, text="Password")

#casella input(password)
password_input = tk.Entry(fin)
password_input.pack()

# Label4 iniziale
label4 = tk.Label(fin, text="")
label4.pack()

def get_input():
        user_username_input = username_input.get()
        user_password_input = password_input.get()
        if user_username_input in user_list and user_password_input == "1234":
            label4.config(text="You are logged in!", font=title_font, fg="black")
        else:
            label4.config(text="Invalid username/password!")

def clear():
    label4.config(text="")

# Bottone per confermare l'input
button = tk.Button(fin, text="Confirm", command=get_input)
button.pack() 

# bottone per clearare il text
button2 = tk.Button(fin, text="Try another user", command=clear)
button2.pack()

#loop        
fin.mainloop()
