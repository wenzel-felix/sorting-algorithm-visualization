import pygame
from Start_menu import Menu


class Main_window:

    def __init__(self):
        self.pre_menu = Menu()
        self.window = pygame.display.set_mode((1500, 1000))
        pygame.display.set_caption(self.pre_menu.list_of_sorting_algorithms[self.pre_menu.sorting_algorithm])
        self.run_window()

    def run_window(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw_rect()

    def draw_rect(self):
        c = 1
        for i in self.pre_menu.unique_values:
            #dynamic bars
            pygame.draw.rect(self.window, (0, 102, 255), (10+c*3, 10, 2, i))
            c += 1
        pygame.display.update()

Main_window()