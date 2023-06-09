import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("400x200")
app.resizable(0, 0)
app.title('Learn.py')

label1 = customtkinter.CTkLabel(app, text="Learn.py", fg_color="transparent", font=("Sans Serif", 20))
label1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
label2 = customtkinter.CTkLabel(app, text="Coming Soon", fg_color="transparent", font=("Sans Serif", 20))
label2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

app.mainloop()
