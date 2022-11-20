import tkinter
import customtkinter
from PIL import Image, ImageTk
import tkintermapview
from culture_class import CultureClass

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CustomTkinter complex_example.py")
        self.minsize(500, 300)
        self.geometry(f"{900}x{700}")

        self.menu_bar = MenuBar()
        self.menu_bar.place(relx=0, rely=0, relwidth=1)

        self.rowconfigure(0, minsize=50)
        self.columnconfigure(0, weight=1)

        option = 1

        if option == 0:
            self.label1 = customtkinter.CTkLabel(self, text="Recommended", text_font=("Noto Sans KR", -20, "bold"))
            self.label1.grid(row=1, column=0, sticky="w", padx=10)

            self.bar1 = VerticalSlider(self)
            self.bar1.grid(row=2, column=0, sticky="ew")

            self.label2 = customtkinter.CTkLabel(self, text="New", text_font=("Noto Sans KR", -20, "bold"))
            self.label2.grid(row=3, column=0, sticky="w")

            self.bar2 = VerticalSlider(self)
            self.bar2.grid(row=4, column=0, sticky="ew")

            self.label3 = customtkinter.CTkLabel(self, text="Random", text_font=("Noto Sans KR", -20, "bold"))
            self.label3.grid(row=5, column=0, sticky="w")

            self.bar3 = VerticalSlider(self)
            self.bar3.grid(row=6, column=0, sticky="ew")

        if option == 1:
            self.rowconfigure(3, weight=1)

            self.label1 = customtkinter.CTkLabel(self, text="컬쳐맵", text_font=("Noto Sans KR", -20, "bold"))
            self.label1.grid(row=1, column=0, sticky="w")

            self.label1 = customtkinter.CTkLabel(self, text="카테고리", text_font=("Noto Sans KR", -20, "bold"))
            self.label1.grid(row=2, column=0, sticky="w")

            self.map = CultureMap(self)
            self.map.grid(row=3, column=0, sticky="nesw")


class MenuBar(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        customtkinter.CTkButton(self, text="홈", border_width=2, text_font=("Noto Sans KR", -20, "bold")).place(
            relx=0.01, y=5, relwidth=0.35)
        customtkinter.CTkButton(self, text="컬쳐맵", border_width=2, text_font=("Noto Sans KR", -16, "bold")).place(
            relx=0.46, y=7, relwidth=0.175)
        customtkinter.CTkButton(self, text="카테고리", border_width=2, text_font=("Noto Sans KR", -16, "bold")).place(
            relx=0.64, y=7, relwidth=0.175)
        customtkinter.CTkButton(self, text="컬쳐 알리기", border_width=2, text_font=("Noto Sans KR", -16, "bold")).place(
            relx=0.82, y=7, relwidth=0.175)

        for widget in self.winfo_children():
            widget.configure(corner_radius=0)
            widget.configure(fg_color="white")
            widget.configure(border_color="black")


class HomePageElement(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry = (200, 300)

        raw_image = Image.open("C:/Users/User/PycharmProjects/CultureProject/download.png")
        new_image = raw_image.resize((200, 170))
        self.my_image = ImageTk.PhotoImage(new_image)

        self.image = customtkinter.CTkLabel(self,
                                            image=self.my_image,
                                            width=200,
                                            height=170,
                                            fg_color="light blue")
        self.image.grid(row=0, column=0, padx=10, pady=2)

        self.title = customtkinter.CTkLabel(self,
                                            text="aaaa",
                                            width=200,
                                            height=40,
                                            fg_color="grey")
        self.title.grid(row=1, column=0, padx=10)

        self.date = customtkinter.CTkLabel(self,
                                           text="aaaa",
                                           width=200,
                                           height=20,
                                           fg_color="grey")
        self.date.grid(row=2, column=0, padx=10)

        self.location = customtkinter.CTkLabel(self,
                                               text="aaaa",
                                               width=200,
                                               height=20,
                                               fg_color="grey")
        self.location.grid(row=3, column=0, padx=10)

        self.location = customtkinter.CTkButton(self,
                                                text="상세히 보기",
                                                width=200,
                                                height=20,
                                                fg_color="grey")
        self.location.grid(row=3, column=0, padx=10, sticky="e")


class VerticalSlider(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = customtkinter.CTkCanvas(self)
        scrollbar = customtkinter.CTkScrollbar(self, orientation="horizontal", command=self.canvas.xview)
        self.scrollable_frame = customtkinter.CTkFrame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        for i in range(20):
            self.element = HomePageElement(self.scrollable_frame)
            self.element.grid(row=0, column=i)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(xscrollcommand=scrollbar.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        scrollbar.pack(side="bottom", fill="x")


class CultureMap(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.map_widget = tkintermapview.TkinterMapView(self, corner_radius=0)
        self.map_widget.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor="center")

        self.map_widget.set_position(37.293692, 126.974304)
        self.map_widget.set_zoom(15)

        '''
        for cu in p:
            marker = self.map_widget.set_marker(cu.longitude,
                                                cu.latitude,
                                                text=cu.eventName)
            marker.set_text(cu.eventName)
        '''


class CulturePage(customtkinter.CTkToplevel):
    def __init__(self, p):
        super().__init__()

        culture_name = customtkinter.CTkLabel(text="컬쳐페이지")
        culture_name.grid(row=0, column=0)

        culture_name = customtkinter.CTkLabel(text=p.eventName)
        culture_name.grid(row=1, column=0)

        raw_image = Image.open("C:/Users/User/PycharmProjects/CultureProject/download.png")
        new_image = raw_image.resize((200, 170))
        self.my_image = ImageTk.PhotoImage(new_image)

        self.image = customtkinter.CTkLabel(self, image=self.my_image)
        self.image.grid(row=2, column=0, rowspan=6)

        customtkinter.CTkLabel(self, text="일시").grid(row=3, column=1)
        customtkinter.CTkLabel(self, text=f"{p.eventStartDate} ~ {p.eventEndDate}").grid(row=4, column=1)
        customtkinter.CTkLabel(self, text="장소").grid(row=5, column=1)
        customtkinter.CTkLabel(self, text=f"{p.roadAddress}").grid(row=6, column=1)
        customtkinter.CTkLabel(self, text="가격").grid(row=7, column=1)
        customtkinter.CTkLabel(self, text=f"{p.price}").grid(row=8, column=1)

        self.grid_rowconfigure(8, minsize=20)

        customtkinter.CTkLabel(self, text="상세").grid(row=9, column=0)
        customtkinter.CTkLabel(self, text=f"{p.information}").grid(row=10, column=0, rowspan=3)

        customtkinter.CTkLabel(self, text="오늘 개장 시간:").grid(row=9, column=1)
        customtkinter.CTkLabel(self, text=f"{p.mondayStartTime} ~ {p.mondayEndTime}").grid(row=10, column=1)
        customtkinter.CTkLabel(self, text="사이트").grid(row=11, column=1)
        customtkinter.CTkLabel(self, text=f"{p.page}").grid(row=12, column=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
