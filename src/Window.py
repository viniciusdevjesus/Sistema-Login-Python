# import tkinter

# Window = tkinter.Tk()
# Window.geometry("500x300")



# text = tkinter.Label(Window, text="Fazer Login")
# text.pack(padx=10, pady=10)
# btnLogin = tkinter.Button(Window, text="Login", command=Click)
# btnLogin.pack(padx=10, pady=10)

# Window.mainloop()

import customtkinter

Window = customtkinter.CTk()
Window.geometry("500x300")

def Click():
    print("Fazer Login")


text = customtkinter.CTkLabel(Window, text="Fazer Login")
text.pack(padx=10, pady=10)

btnLogin = customtkinter.CTkButton(Window, text="Login", command=Click)
btnLogin.pack(padx=10, pady=10)

Window.mainloop()