from tkinter import *
import random


class Menu:

    unique_values = []
    sorting_algorithm = 0
    list_of_sorting_algorithms = ['bubblesort', 'quicksort', 'insertionsort', 'swapsort', 'mergesort', 'heapsort']

    def __init__(self):
        self.master = Tk()
        self.master.maxsize(width=500, height=200)

        self.list_manager = StringVar(master=self.master)
        self.list_manager.set(self.list_of_sorting_algorithms[0])

        self.option_menu = OptionMenu(self.master, self.list_manager, *self.list_of_sorting_algorithms)
        self.option_menu.place(x=20, y=20, relwidth=0.8)

        self.slider = Scale(self.master, from_=100, to=400, tickinterval=100, orient=HORIZONTAL)
        self.slider.place(x=20, y=60, relwidth=0.8)

        submit = Button(self.master, text="submit", command=self.button_click)
        submit.place(x=40, y=130, relwidth=0.60)

        self.master.mainloop()

    def button_click(self):
        for i in range(self.slider.get()):
            y = random.randint(1, 800)
            while y in self.unique_values:
                y = random.randint(1, 800)
            self.unique_values.append(y)
        self.sorting_algorithm = self.list_of_sorting_algorithms.index(self.list_manager.get())
        self.master.destroy()
