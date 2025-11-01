from customtkinter import *


class MainWindow(CTk):

    def __init__(self):
        super().__init__()


        self.top_frame = CTkFrame(self)
        self.top_frame.pack(fill = "both", expand = True)


        self.content_frame = CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True)


        self.input_frame = CTkFrame(self.content_frame)
        self.input_frame.pack(fill="x", expand=True, side="bottom")


        self.text_box = CTkTextbox(self.content_frame)
        self.text_box.pack(padx = 20, pady=20, fill="both", expand=True)
        self.text_box.configure(state = "disable")


        self.is_menu_open = False
        self.menu_width = 0
        self.menu_frame = CTkFrame(self, width=0, height = 400)
        self.menu_frame.place(x = 0, y = 50)
        self.menu_frame.pack_propagate(False)


        self.menu_input = CTkEntry(self.menu_frame, placeholder_text="Введіть ваше ім'я...")
        self.menu_input.pack(pady = 20)


        self.connect_button = CTkButton(self.menu_frame, text="Підключитись")
        self.connect_button.pack(pady = 10)


        self.menu_btn = CTkButton(self.top_frame, text="Меню", command=self.toggle_menu)
        self.menu_btn.pack(side = "left", padx = 20)


        self.input_box = CTkEntry(self.input_frame)
        self.input_box.pack(fill="x", padx= 20, pady=20, side = "left", expand=True)


        self.btn = CTkButton(self.input_frame, text="Надіслати")
        self.btn.pack(side="right")


        self.title("LogiTalk")
        self.geometry("650x400")


    def toggle_menu(self):
        if self.is_menu_open:
            self.close_menu()
        else:
            self.open_menu()


    def open_menu(self):
        
        if self.menu_width < 200:
            self.menu_width += 20
            self.menu_frame.configure(width=self.menu_width)
            self.content_frame.pack_configure(padx=(self.menu_width + 20, 0))
            self.after(10, self.open_menu)
        else:
            self.is_menu_open = True

    def close_menu(self):
        if self.menu_width > 0:
            self.menu_width -= 20
            self.menu_frame.configure(width=self.menu_width)
            self.content_frame.pack_configure(padx=(self.menu_width, 0))
            self.after(10, self.close_menu)
        else:
            self.is_menu_open = False


main_window = MainWindow()
main_window.mainloop()