from tkinter import *
from tkinter import messagebox
import random
import pyperclip  
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def genterate_passward():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    passward_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    passward_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letter+passward_symbols+passward_numbers

    random.shuffle(password_list)

    password ="".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    passward_entry.insert(0,password )
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website=website_entry.get()
    email=email_entry.get()
    passward=passward_entry.get()

    if len(website)==0 or len(passward)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:

        is_ok= messagebox.askokcancel(title="website",message=f"These are the details entered:\n Email: {email}\n passward: {passward}\n is it ok to save.")
        # messagebox.showinfo(title="Title",message="Message")
        
        if is_ok:
            
            with open("C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/passward_manager_GUI/data.txt","a") as data_file:
                f=data_file.write(f"{website} | {email} | {passward}\n")
                website_entry.delete(0,END)
                passward_entry.delete(0,END)

    
# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Passward Manager")
window.minsize(width=300,height=300)
window.config(padx=50,pady=50)

web_name=Label(text="Website:")
web_name.grid(row=1,column=0)
web_name.focus()

website_entry=Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)

Email_Username=Label(text="Email/Username:")
Email_Username.grid(row=2,column=0)


email_entry=Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"anujgutpa0333@gmail.com")


button=Button(text="Generate Passward",command=genterate_passward)
button.grid(row=3,column=2)

passward_label=Label(text="Passward:")
passward_label.grid(row=3,column=0)


passward_entry=Entry(width=32)
passward_entry.grid(row=3,column=1)


add_button=Button(text="Add",width=43,command=save)
add_button.grid(row=4,column=1,columnspan=2)


canvas=Canvas(width=200,height=200)
lock_img=PhotoImage(file="C:/Users/ASUS/OneDrive/Documents/anuj_work/python_mini_projects/passward_manager_GUI/password-manager-start/logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)


window.mainloop()