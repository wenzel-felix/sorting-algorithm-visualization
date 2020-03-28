import pygame
from Start_menu import Menu
import time


class Main_window:
    pygame.init()

    def __init__(self):
        self.run = True
        self.window_height = 1000
        self.window_width = 1500
        self.pre_menu = Menu()
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption(self.pre_menu.list_of_sorting_algorithms[self.pre_menu.sorting_algorithm])
        self.run_window()

    def run_window(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.draw_bars(self.pre_menu.unique_values)
            self.draw_gui()

    def draw_bars(self, array):
        c = 1
        pygame.draw.rect(self.window, (0, 0, 0), (0, 0, self.window_width - 250, self.window_height))
        for i in array:
            # dynamic bars
            pygame.draw.rect(self.window, (0, 102, 255), (10 + c * 3, 20, 2, i))
            c += 1

        pygame.display.update()

    def draw_gui(self):
        #start button
        self.button("start", self.window_width-200, 30, 100, 30, (0, 0, 0), (0, 102, 255), (0, 150, 200), self.do_sorting)

        #quit button
        self.button("quit", self.window_width-200, 70, 100, 30, (0, 0, 0), (0, 102, 255), (0, 150, 200), self.quit_window)

        pygame.display.update()

    def button(self, msg,  x, y, w, h, bc, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.window, ac, (x-2, y-2, w+4, h+4))
            pygame.draw.rect(self.window, bc, (x+3, y+3, w-6, h-6))
            font = pygame.font.SysFont('Arial', 22)
            self.window.blit(font.render(msg, True, ac), (x+10, y+1))

            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.window, (0, 0, 0), (x - 2, y - 2, w + 4, h + 4))
            pygame.draw.rect(self.window, ic, (x, y, w, h))
            pygame.draw.rect(self.window, bc, (x + 3, y + 3, w - 6, h - 6))
            font = pygame.font.SysFont('Arial', 20)
            self.window.blit(font.render(msg, True, ic), (x + 10, y + 3))

    def quit_window(self):
        self.run = False

    def do_sorting(self):
        if self.pre_menu.sorting_algorithm == 0:
            self.do_bubblesort(self.pre_menu.unique_values)
        elif self.pre_menu.sorting_algorithm == 1:
            self.do_quicksort(self.pre_menu.unique_values)
        elif self.pre_menu.sorting_algorithm == 2:
            self.do_insertionsort(self.pre_menu.unique_values)
        elif self.pre_menu.sorting_algorithm == 3:
            self.do_swapsort(self.pre_menu.unique_values)
        elif self.pre_menu.sorting_algorithm == 4:
            self.do_mergesort(self.pre_menu.unique_values)
        '''elif self.pre_menu.sorting_algorithm == 5:
            self.do_heapsort()'''

    def do_bubblesort(self, array):
        for i in range(len(array)):
            for j in range(0, len(array)-1, 1):
                if array[j] > array[j+1]:
                    array[j+1], array[j] = array[j], array[j+1]
                self.draw_bars(array)

    def partition(self, array, begin, end):
        pivot = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
                self.draw_bars(array)
                pygame.display.update()
                time.sleep(0.03)
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot

    def do_quicksort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        def _quicksort(array, begin, end):
            if begin >= end:
                return
            pivot = self.partition(array, begin, end)
            _quicksort(array, begin, pivot - 1)
            _quicksort(array, pivot + 1, end)

        return _quicksort(array, begin, end)

    def do_insertionsort(self, array):
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                for j in range(i, 0, -1):
                    if array[j] < array[j-1]:
                        array[j], array[j-1] = array[j-1], array[j]
                        self.draw_bars(array)
                        pygame.display.update()

    def do_swapsort(self, array):
        is_sorted = False
        c = 0
        while not is_sorted:
            index = sum(j <= array[c] for j in array)-1
            if c == index:
                c += 1
                if c == len(array):
                    is_sorted = True
            elif array[index] == array[c]:
                array[index-1], array[c] = array[c], array[index-1]
                if c == index - 1:
                    c += 1
            else:
                array[index], array[c] = array[c], array[index]

            time.sleep(0.05)
            self.draw_bars(array)
            pygame.display.update()

    def do_mergesort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            L = array[:mid]
            R = array[mid:]
            start_index = self.pre_menu.unique_values.index(array[0])-1
            end_index = self.pre_menu.unique_values.index(array[len(array)-1])

            self.do_mergesort(L)
            self.do_mergesort(R)

            self.draw_bars(self.pre_menu.unique_values[:start_index]+array+self.pre_menu.unique_values[end_index:])
            pygame.display.update()
            time.sleep(0.05)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1


Main_window()
