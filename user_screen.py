import pygame, sys
import drop_m
from button import Button
import map

clean_place = ''

pygame.init()

SCREEN = pygame.display.set_mode(consts.WINDOW_SIZE)
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/nature_backround.jpg")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def open_map():
    map.run_map()


def report():
    clock = pygame.time.Clock()
    list1 = drop_m.OptionBox(
        550, 320, 160, 40, (173,255,47), (50,205,50), pygame.font.SysFont(None, 30),
        ["option 1", "2nd option", "another option"])
    while True:
        clock.tick(60)
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill(consts.COLOR_WHITE)

        OPTIONS_TEXT = get_font(45).render("report cleaning", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        clean_button = Button(image=None, pos=(640, 460),
                              text_input="I CLEANED", font=get_font(75), base_color="Black", hovering_color="Green")

        clean_button.changeColor(OPTIONS_MOUSE_POS)
        clean_button.update(SCREEN)
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if clean_button.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()  # report add 1

        selected_option = list1.update(events)
        if selected_option >= 0:
            print(selected_option)
            #clean_place = list[selected_option]

        list1.draw(SCREEN)
        pygame.display.update()



def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("CARE FOR NATURE", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        map_button = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                            text_input="MAP", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        report_button = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                               text_input="REPORT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [map_button, report_button, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if map_button.checkForInput(MENU_MOUSE_POS):
                    open_map()
                if report_button.checkForInput(MENU_MOUSE_POS):
                    report()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
