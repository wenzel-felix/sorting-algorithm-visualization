import pygame
from Start_menu import Menu


class Main_window:
    pygame.init()

    def __init__(self):
        self.run = True
        self.pre_menu = Menu()
        self.window = pygame.display.set_mode((1500, 1000))
        pygame.display.set_caption(self.pre_menu.list_of_sorting_algorithms[self.pre_menu.sorting_algorithm])
        self.run_window()

    def run_window(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.draw_bars()
            self.draw_gui()

    def draw_bars(self):
        c = 1
        for i in self.pre_menu.unique_values:
            # dynamic bars
            pygame.draw.rect(self.window, (0, 102, 255), (10 + c * 3, 20, 2, i))
            c += 1

        pygame.display.update()

    def draw_gui(self):
        #start button
        self.button("start", 1300, 30, 100, 30, (0, 0, 0), (0, 102, 255), (0, 150, 200), action=None)

        #quit button
        self.button("quit", 1300, 70, 100, 30, (0, 0, 0), (0, 102, 255), (0, 150, 200), self.quit_window)

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

Main_window()