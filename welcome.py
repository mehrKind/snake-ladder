import pygame
from pygame import *
import sys
pygame.init()

table = display.set_mode((1380, 702))
display.set_caption("snake and ladder version 3.10.8")
icon_2 = image.load("recourses/snake01.png")
display.set_icon(icon_2)
bg = image.load("recourses/qxzQFv.jpg")
bg = transform.scale(bg, (1380, 700))
logo_0 = image.load("recourses/logo2.png")
# colors
yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
Love_pink = (255, 0, 51)
# text
# g: game, e: exit, n: name
font_g = pygame.font.SysFont(None, 70)
font_e = pygame.font.SysFont(None, 40)
font_n = pygame.font.SysFont(None, 25)
start = font_g.render("Start", True, black)
exit = font_g.render("Exit", True, black)
name = font_n.render("Alireza mehraban", True, black)

while True:
    table.blit(bg, (0, 0))
    table.blit(logo_0, (387, 90))
    # start
    draw.rect(table, green, (570, 290, 200, 75), 0, 50)
    draw.rect(table, black, (570, 290, 200, 75), 2, 50)
    # exit
    draw.rect(table, red, (570, 400, 200, 75), 0, 50)
    draw.rect(table, black, (570, 400, 200, 75), 2, 50)
    # start and exit text
    table.blit(start, (611, 305))
    table.blit(exit, (620, 414))
    # name
    table.blit(name, (397, 180))
    for o in event.get():
        if o.type == QUIT:
            quit()
            sys.exit()
        mouse1 = mouse.get_pos()
        if o.type == MOUSEBUTTONDOWN:
            # start Button
            if 570 <= mouse1[0] <= 770 and 290 <= mouse1[1] <= 360:
                import main
                quit()
                sys.exit()
            # exit Button
            # sure = font_e.render("Are you sure?",True,black)
            # if 570 <= mouse1[0] <= 770 and 400 <= mouse1[1] <= 475:
            #     quit()
            #     sys.exit()
                # table.blit(sure,(600,500))
                # display.update()

    display.update()
