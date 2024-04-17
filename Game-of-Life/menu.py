import pygame
import negat1
import negat0
import si00
import si01
import si10
import si11
import sau00
import sau01
import sau10
import sau11


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "NOT GATE"
        self.notgatex, self.notgatey = self.mid_w, self.mid_h + 30
        self.orgatex, self.orgatey = self.mid_w, self.mid_h + 60
        self.andgatex, self.andgatey = self.mid_w, self.mid_h + 90
        self.infox, self.infoy = self.mid_w, self.mid_h + 120
        self.expx, self.expy = self.mid_w, self.mid_h + 150
        self.cursor_rect.midtop = (self.notgatex + self.offset, self.notgatey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('MENU', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("NOT GATE", 20, self.notgatex, self.notgatey)
            self.game.draw_text("OR GATE", 20, self.orgatex, self.orgatey)
            self.game.draw_text("AND GATE", 20, self.andgatex, self.andgatey)
            self.game.draw_text("EXPLANATIONS", 20, self.infox, self.infoy)
            self.game.draw_text("HOW TO PLAY", 20, self.expx, self.expy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'NOT GATE':
                self.cursor_rect.midtop = (self.orgatex + self.offset + 30, self.orgatey)
                self.state = 'OR GATE'
            elif self.state == 'OR GATE':
                self.cursor_rect.midtop = (self.andgatex + self.offset + 20, self.andgatey)
                self.state = 'AND GATE'
            elif self.state == 'AND GATE':
                self.cursor_rect.midtop = (self.infox + self.offset - 15, self.infoy)
                self.state = 'INSTRUCTIONS'
            elif self.state == 'INSTRUCTIONS':
                self.cursor_rect.midtop = (self.expx + self.offset - 10, self.expy)
                self.state = 'HOW TO PLAY'
            elif self.state == 'HOW TO PLAY':
                self.cursor_rect.midtop = (self.notgatex + self.offset + 20, self.notgatey)
                self.state = 'NOT GATE'
        elif self.game.UP_KEY:
            if self.state == 'NOT GATE':
                self.cursor_rect.midtop = (self.expx + self.offset - 10, self.expy)
                self.state = 'HOW TO PLAY'
            elif self.state == 'OR GATE':
                self.cursor_rect.midtop = (self.notgatex + self.offset + 20, self.notgatey)
                self.state = 'NOT GATE'
            elif self.state == 'AND GATE':
                self.cursor_rect.midtop = (self.orgatex + self.offset + 30, self.orgatey)
                self.state = 'OR GATE'
            elif self.state == 'INSTRUCTIONS':
                self.cursor_rect.midtop = (self.andgatex + self.offset + 20, self.andgatey)
                self.state = 'AND GATE'
            elif self.state == 'HOW TO PLAY':
                self.cursor_rect.midtop = (self.infox + self.offset - 20, self.infoy)
                self.state = 'INSTRUCTIONS'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'NOT GATE':
                self.game.curr_menu = self.game.options
            elif self.state == 'OR GATE':
                self.game.curr_menu = self.game.menu_Or
            elif self.state == 'AND GATE':
                self.game.curr_menu = self.game.credits
            elif self.state == 'INSTRUCTIONS':
                self.game.curr_menu = self.game.instruction
            elif self.state == 'HOW TO PLAY':
                self.game.curr_menu = self.game.howtoplay
            self.run_display = False


class NotMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'NOT 0'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        self.volume_menu_active = False
        self.controls_menu_active = False

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('NOT GATE', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("NOT 0", 15, self.volx, self.voly)
            self.game.draw_text("NOT 1", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'NOT 0':
                self.state = 'NOT 1'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'NOT 1':
                self.state = 'NOT 0'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            if self.state == 'NOT 0':
                self.volume_menu_active = True
                negat1.main(120, 90, 6)
            elif self.state == 'NOT 1':
                self.controls_menu_active = True
                negat0.main(120, 90, 6)


class AndMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = '0 negat'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.options1x, self.options1y = self.mid_w, self.mid_h + 60
        self.options2x, self.options2y = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        self.volume_menu_active = False
        self.controls_menu_active = False

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('AND GATE', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("0 AND 0", 15, self.volx, self.voly)
            self.game.draw_text("0 AND 1", 15, self.volx, self.voly + 20)
            self.game.draw_text("1 AND 0", 15, self.volx, self.voly + 40)
            self.game.draw_text("1 AND 1", 15, self.volx, self.voly + 60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == '0 negat':
                self.state = '1 negat'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == '1 negat':
                self.state = '2 negat'
                self.cursor_rect.midtop = (self.options1x + self.offset, self.options1y)
            elif self.state == '2 negat':
                self.state = '3 negat'
                self.cursor_rect.midtop = (self.options2x + self.offset, self.options2y)
            elif self.state == '3 negat':
                self.state = '0 negat'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            if self.state == '0 negat':
                self.volume_menu_active = True
                si00.main(120, 90, 6)
            elif self.state == '1 negat':
                self.controls_menu_active = True
                si01.main(120, 90, 6)
            elif self.state == '2 negat':
                self.controls_menu_active = True
                si10.main(120, 90, 6)
            elif self.state == '3 negat':
                self.controls_menu_active = True
                si11.main(120, 90, 6)


class OrMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = '0 negat'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.options1x, self.options1y = self.mid_w, self.mid_h + 60
        self.options2x, self.options2y = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        self.volume_menu_active = False
        self.controls_menu_active = False

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('OR GATE', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("0 OR 0", 15, self.volx, self.voly)
            self.game.draw_text("0 OR 1", 15, self.volx, self.voly + 20)
            self.game.draw_text("1 OR 0", 15, self.volx, self.voly + 40)
            self.game.draw_text("1 OR 1", 15, self.volx, self.voly + 60)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == '0 negat':
                self.state = '1 negat'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == '1 negat':
                self.state = '2 negat'
                self.cursor_rect.midtop = (self.options1x + self.offset, self.options1y)
            elif self.state == '2 negat':
                self.state = '3 negat'
                self.cursor_rect.midtop = (self.options2x + self.offset, self.options2y)
            elif self.state == '3 negat':
                self.state = '0 negat'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            if self.state == '0 negat':
                self.volume_menu_active = True
                sau00.main(120, 90, 6)
            elif self.state == '1 negat':
                self.controls_menu_active = True
                sau01.main(120, 90, 6)
            elif self.state == '2 negat':
                self.controls_menu_active = True
                sau10.main(120, 90, 6)
            elif self.state == '3 negat':
                self.controls_menu_active = True
                sau11.main(120, 90, 6)


class ScrollableTextMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.text = "     Conway's Game of Life is a cellular automaton devised in 1970 by the british mathematician John Horton Conway.\n" \
                    "     The game is composed of an infinte, two-dimensional grid of squares called cells.\n" \
                    "     A cell can have one of two states: alive or dead. Each cell interacts with its eight neighbours.\n" \
                    "There are three rules that dictate what happens to the cell over the course of the next generation:\n" \
                    "  1. Any live cell with two or three live neighbours survives.\n" \
                    "  2. Any dead cell with three live neighbours becomes a live cell.\n" \
                    "  3. All other live cells die in the next generation. Similarly, all other dead cells stay dead\n" \
                    "     Given this set of rules there are many interesting patterns that arises.\n" \
                    "For implementing the game of life the following patterns will be used:\n" \
                    "1. Glider\n" \
                    "     A glider is a spaceship type of structure. A spaceship has the property that it returns to its original state after a number of generations but in a different position. The glider, also known as the featherweight spaceship, is the smallest, most common and first-discovered spaceship in Game of Life." \
                    "A property of the gliders is that if they collide at a certain angle they anhilate each other." \
                    "In this simulation the glider will represent the logic one. When it arrives to a certain point at a given interval it means that the value of the gate is logic one. If it doesn't arrive at that specific point the gate has a zero value." \
                    "\n2. Gosper Glider Gun\n" \
                    "     The Gosper gun is the first discovered gun. A gun is a stationary pattern that repeatedly emits spaceships forever." \
                    "In the context of emulating Logic Gates, this structure is used both as a way to generate input and as a way to block a stream a gliders, by poisitioning a glider at a certain angle." \
                    "\n3. Eater\n" \
                    "     The eater is a stationary structure that annhiliate a glider."
        self.font = pygame.font.Font(None, 27)
        self.text_rect = pygame.Rect(50, 50, 600, 900)
        self.scroll_speed = 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('EXPLANATIONS', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 200 + self.text_rect.y)
            self.draw_text()
            self.blit_screen()

    def draw_text(self):
        lines = self.text.splitlines()
        rendered_lines = []
        for line in lines:
            words = line.split(" ")
            rendered_words = []
            current_line = ""
            for word in words:
                rendered_word = self.font.render(word + " ", True, (255, 255, 255))
                if self.font.size(current_line + word)[0] > self.text_rect.width:
                    rendered_lines.append(self.font.render(current_line, True, (255, 255, 255)))
                    current_line = word + " "
                else:
                    current_line += word + " "
            rendered_lines.append(self.font.render(current_line, True, (255, 255, 255)))

        max_lines = int(self.text_rect.height / self.font.get_height())
        start_line = max(0, len(rendered_lines) - max_lines)
        text_y = self.game.DISPLAY_H // 2 - 200 + self.text_rect.y + 50  # Adjust the y-coordinate here
        for i in range(start_line, len(rendered_lines)):
            self.game.display.blit(rendered_lines[i],
                                   (self.text_rect.x, text_y + (i - start_line) * self.font.get_height()))

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY:
            self.text_rect.y -= self.scroll_speed
        elif self.game.DOWN_KEY:
            self.text_rect.y += self.scroll_speed


class HowToPlay(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.text = "   Press UP and DOWN in order to navigate in the menu.\n" \
                    "   If you want to select an option from the menu point the arrow to the option and press ENTER.\n" \
                    "   If you want to learn how to play this game select the HOW TO PLAY section.\n" \
                    "   If you want to learn about Conway's Game of Life and the patterns used in this game select EXPLANATION.\n" \
                    "   In order to select a value from the table of truth point the cursor to the option and press ENTER.\n" \
                    "   In order to go back to the menu from the logic gates simulation press SPACE.\n"
        self.font = pygame.font.Font(None, 27)
        self.text_rect = pygame.Rect(50, 50, 600, 900)
        self.scroll_speed = 20

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('HOW TO PLAY', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 200 + self.text_rect.y)
            self.draw_text()
            self.blit_screen()

    def draw_text(self):
        lines = self.text.splitlines()
        rendered_lines = []
        for line in lines:
            words = line.split(" ")
            rendered_words = []
            current_line = ""
            for word in words:
                rendered_word = self.font.render(word + " ", True, (255, 255, 255))
                if self.font.size(current_line + word)[0] > self.text_rect.width:
                    rendered_lines.append(self.font.render(current_line, True, (255, 255, 255)))
                    current_line = word + " "
                else:
                    current_line += word + " "
            rendered_lines.append(self.font.render(current_line, True, (255, 255, 255)))

        max_lines = int(self.text_rect.height / self.font.get_height())
        start_line = max(0, len(rendered_lines) - max_lines)
        text_y = self.game.DISPLAY_H // 2 - 200 + self.text_rect.y + 50  # Adjust the y-coordinate here
        for i in range(start_line, len(rendered_lines)):
            self.game.display.blit(rendered_lines[i],
                                   (self.text_rect.x, text_y + (i - start_line) * self.font.get_height()))

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY:
            self.text_rect.y -= self.scroll_speed
        elif self.game.DOWN_KEY:
            self.text_rect.y += self.scroll_speed
