import customtkinter as ctk
from my_tab_view import MyTabView


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("640x360")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.title("PowerShell History Manager")

        self.tab_view = MyTabView(self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky=ctk.NSEW)


if __name__ == "__main__":
    app = App()
    app.mainloop()
