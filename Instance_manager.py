from tkinter import *


class Instance_manager:

    new_sorting = False

    def __init__(self):
        self.master = Tk()
        self.master.maxsize(width=150, height=60)

        new_map_button = Button(master=self.master, text="Let's sort", command=self.set_new_sorting_true)
        new_map_button.place(x=10, y=10)
        exit_button = Button(master=self.master, text="Exit", command=self.set_new_sorting_false)
        exit_button.place(x=110, y=10)

        self.master.mainloop()

    def set_new_sorting_true(self):
        self.new_sorting = True
        self.master.destroy()

    def set_new_sorting_false(self):
        self.new_sorting = False
        self.master.destroy()