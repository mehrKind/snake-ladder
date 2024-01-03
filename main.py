""""""""""""""""""""""""""""""""""""""""
Title: Snake and Ladder Game
Auther: Alireza Mehraban
Date_Start: 1401/3/1
Date_End:   1401/3/8
"""""""""""""""""""""""""""""""""""""""
import pygame
from pygame import *
import sys
import random
from time import sleep

pygame.init()

screen = display.set_mode((1380,702))
display.set_caption("snake and ladder version 3.10.8")
#icon
icon = image.load("recourses/snake01.png")
display.set_icon(icon)
# background
backGround = image.load("recourses/qxzQFv.jpg")
backGround = transform.scale(backGround,(1380,700))
# main_board
board = image.load("recourses/board.png")
board = transform.scale(board,(650,610))
logo = image.load("recourses/logo.png")
#=================================================================colors
black = (0,0,0)
yellow = (255,255,0)
blue = (0,0,255)
dark_blue = (4,0,117)
white = (255,255,255)
purple = (109,38,164)
light_pink = (250,72,132)
gray = (66,61,67)
Love_pink = (255,0,51)
red = (255,0,0)
#=================================================================fonts and texts
# q = quit(), a = alireza
font_q = pygame.font.SysFont(None,35)
font_a = pygame.font.SysFont(None,25)
exit = font_q.render("Press to exit",True,blue)
roll_text = font_q.render("Roll Me", True, dark_blue)
dice_text = font_q.render("Dice: ", True, dark_blue)
alireza = font_a.render("alireza mehraban", True, dark_blue)
#==================================================================players position
player1_x = 380
player1_y = 621
player2_x = 407
player2_y = 642
player1_score = 1
player2_score = 1
#=================================================================board_list(X,Y)
bites = [(99,6),(88,67),(71,29),(55,13),(24,1)]
ladders = [(8,31),(15,97),(42,81),(66,87)]

list_board = []
for home in range(0,10):
    row = []
    if home % 2 == 0:
        row = list(range(home*10+1,home*10+11))
    else :
        row = list(range(home*10+10,home*10,-1))
    list_board.append(row)
list_board.reverse()
#==============================================================All def(board,snake_bite,ladder_up)
def radif_sotoon(score):
    radif = 0
    for row_x in list_board:
        radif += 1
        sotoon = 0
        if score in row_x:
            for x in row_x:
                sotoon +=1
                if x == score:
                    return radif,sotoon

def x_y(score):
    row,column = radif_sotoon(score)
    x = 380 + (65*(column-1))
    y = 621 - (62*(10-row))
    return x , y
# def bite ==> related to bites_list
def bite(score):
    done = False
    for i in bites:
        x,y = i
        if score == x:
            done = True
            break
    return done

def bite_back(score):
    for i in bites:
        x,y = i
        if score == x :
            return y
# def ladder ==> related to ladders_list
def ladder(score):
    done_1 = False
    for i in ladders:
        x , y = i
        if score == x:
            done_1 = True
            break
    return done_1

def ladder_up(score):
    for i in ladders:
        x,y = i
        if score == x :
            return y

# def edit():
#     global player1_x
#     global player1_y
#     player1_x = 505
#     player1_y = 500
#==============================================================def move
turn = "black"
dice = 0
def move():
    global turn
    global winner
    if turn == "black":
        global player1_score
        global player1_x
        global player1_y
        global dice_score
        global dice
        global player1_text
        dice = random.randint(1,6)
        # player_1 waiting to win
        if dice + player1_score < 100:
            player1_score += dice
        if dice + player1_score == 100:
            import winner
            quit()
            sys.exit()
        player1_x, player1_y = x_y(player1_score)
        display.update()
        if bite(player1_score):
            player1_score = bite_back(player1_score)
            player1_x , player1_y= x_y(player1_score)
        if ladder(player1_score):
            player1_score = ladder_up(player1_score)
            player1_x , player1_y = x_y(player1_score)
        turn = "red"
    else :
        global player2_score
        global player2_x
        global player2_y
        global player2_text
        global winner
        dice = random.randint(1,6)
        # player_2 waiting to win
        if dice + player2_score < 100:
            player2_score += dice
        if dice + player2_score == 100:
            import winner
            quit()
            sys.exit()
        player2_x, player2_y = x_y(player2_score)
        display.update()
        if bite(player2_score):
            player2_score = bite_back(player2_score)
            player2_x, player2_y = x_y(player2_score)
        if ladder(player2_score):
            player2_score = ladder_up(player2_score)
            player2_x , player2_y = x_y(player2_score)
        player2_x += 27
        player2_y += 21
        turn = "black"
display.update()
#=================================================================screen keeper
while True:
    screen.blit(backGround,(0,0))
    screen.blit(board,(360,50))
    screen.blit(logo,(1020,110))
    #drawing
    draw.line(screen,black,(360,50),(1011,50),2)
    draw.line(screen,black,(360,660),(1011,660),2)
    draw.line(screen,black,(360,50),(360,660),2)
    draw.line(screen,black,(1011,50),(1011,660),2)
    # exit button
    draw.rect(screen,yellow,(1180,620,180,70))
    draw.rect(screen,black,(1180,620,180,70),2)
    #dice (X,Y, wdith, heght)
    draw.rect(screen,yellow,(80,350,100,50))
    draw.rect(screen,black,(80,350,100,50),2)
    #players
    draw.circle(screen,gray,(player1_x,player1_y),15)
    draw.circle(screen,Love_pink,(player2_x,player2_y),15)
    # edit
    # draw.rect(screen,black,(500,500,180,70),0,5)
    #players_text
    if turn == "black":
        player1_text = font_q.render("Plyer Gray:",True,red)
    else:
        player1_text = font_q.render("Plyer Gray:",True,dark_blue)
    if turn == "red":
        player2_text = font_q.render("Plyer Pink:",True,red)
    else:
        player2_text = font_q.render("Plyer Pink:",True,dark_blue)

    player1_home = font_q.render(f"{player1_score}",True,dark_blue)
    player2_home = font_q.render(f"{player2_score}",True,dark_blue)
    player_dice = font_q.render(f"{dice}", True, dark_blue)
    #events
    for i in event.get():
        if i.type == QUIT:
            quit()
            sys.exit()
        #------------exit button
        mouse1 = mouse.get_pos()
        if i.type == MOUSEBUTTONDOWN:
            if 1180 <= mouse1[0] <= 1380 and 620<= mouse1[1]<= 690:
                quit()
                sys.exit()
            elif 80 <= mouse1[0] <= 180 and 350 <= mouse1[1] <= 400:
                move()
            # elif 500 <= mouse1[0] <= 680 and 500 <= mouse1[1] <= 570:
            #     edit()
    screen.blit(exit,(1194,642))
    screen.blit(player1_text,(50,100))
    screen.blit(player2_text,(50,200))
    screen.blit(player1_home,(200,100))
    screen.blit(player2_home,(200,200))
    screen.blit(roll_text,(87,365))
    screen.blit(dice_text,(90,280))
    screen.blit(player_dice,(190,280))
    screen.blit(alireza,(1200,600))
    display.update()