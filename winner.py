import pygame
from pygame import *
import sys
from main import *
pygame.init()

screen = display.set_mode((1380,702))
display.set_caption("snake and ladder version 3.10.8")
#icon
icon = image.load("recourses/snake01.png")
display.set_icon(icon)
player1_win = image.load("recourses/you win5.png")
player1_win = transform.scale(player1_win, (1300,700))
#color
dark_blue = (4,0,117)
black = (0,0,0)
Love_pink = (255,0,51)
# font and texts
font_w = pygame.font.SysFont(None,170)
font_q = pygame.font.SysFont(None,30)
p1win = font_w.render("Player Gray Wins",True,dark_blue)
p2win = font_w.render("Player Pink Wins",True,dark_blue)
quitt = font_q.render("Press to exit",True,dark_blue)
# winner song
mixer.music.load("recourses/mixkit-video-game-win-2016.wav")
mixer.music.play()
display.update()
#screen_keeper
while True:
    screen.fill("white")
    screen.blit(player1_win,(30,-50))
    draw.rect(screen,Love_pink,(1210,635,145,50),2)
    screen.blit(quitt,(1220,650))
    if dice + player1_score == 100:
        screen.blit(p1win,(200,450))
    if dice + player2_score == 100:
        screen.blit(p2win,(200,450))
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
        mouse2 = mouse.get_pos()
        if e.type == MOUSEBUTTONDOWN:
            if 1210 <= mouse2[0] <= 1355 and 635 <= mouse2[1] <= 685:
                quit()
                sys.exit()
    
    display.update()