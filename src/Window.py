# import tkinter

# Window = tkinter.Tk()
# Window.geometry("500x300")



# text = tkinter.Label(Window, text="Fazer Login")
# text.pack(padx=10, pady=10)
# btnLogin = tkinter.Button(Window, text="Login", command=Click)
# btnLogin.pack(padx=10, pady=10)

# Window.mainloop()
import main
import customtkinter
from winotify import Notification
# Window Config
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

Window = customtkinter.CTk()
Window.title("Login")
Window.geometry("500x300")
# def's
def Login():
    Email_name = Email.get()
    Password_name = Password.get()
def ForgotWindow():
    try:
        NewWindow_fr.janela
    except NameError:
        NewWindow_fr = customtkinter.CTkToplevel()
        NewWindow_fr.janela = True
        NewWindow_fr.title("Esqueci a Senha")
        text_fr = customtkinter.CTkLabel(NewWindow_fr, text="Esqueci a Senha")
        text_fr.pack(padx=10, pady=10) 
        Email_fr = customtkinter.CTkEntry(NewWindow_fr, placeholder_text="Digite seu Email")
        Email_fr.pack(padx = 10, pady = 10)
        NewWindow_fr.attributes("-topmost", True)
    else:
        notification = Notification(app_id="Erro", title="Janela já aberta")
        notification.show()


text = customtkinter.CTkLabel(Window, text="Fazer Login")
text.pack(padx=10, pady=10)
# Entry's
Email = customtkinter.CTkEntry(Window, placeholder_text="Digite seu Email")
Email.pack(padx = 10, pady = 10)

Password = customtkinter.CTkEntry(Window, placeholder_text="Digite seu Senha", show ="*")
Password.pack(padx = 10, pady = 10)


ForgotPass = customtkinter.CTkButton(Window, text="Esqueceu a Senha?", command=ForgotWindow, border_color=None, fg_color="transparent", text_color="blue", hover=None)
ForgotPass.pack(padx = 10, pady = 10)

# ForgotPass.bind("<Button-1>", lambda e: Click())
# ForgotPass.pack(padx = 10, pady = 10)
# Button's
btnLogin = customtkinter.CTkButton(Window, text="Login", command=Click)
btnLogin.pack(padx=10, pady=10)

Window.mainloop()