#import module
import pygame 
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("TicTacToe")



#define variables
line_width = 6
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False



#define colours
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#define font
font = pygame.font.SysFont(None,40)

def reset_game():
    global markers, player, winner, game_over
    markers = [[0]*3 for _ in range(3)]
    player = 1
    winner = 0
    game_over = False



def draw_grid():
    bg = (255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(3):
        pygame.draw.line(screen, grid, (0, x*100), (SCREEN_WIDTH, x*100), 6)
        pygame.draw.line(screen, grid, (x*100,0), (x*100,SCREEN_HEIGHT), 6)



for i in range(3):
    rows = [0]*3
    markers.append(rows)

def draw_marker():
    x_pos = 0
    for i in markers:
        y_pos = 0
        for k in i:
            if k == 1:
                pygame.draw.line(screen, green, (x_pos*100 + 15, y_pos*100 + 15), (x_pos*100 + 85, y_pos*100 + 85), line_width)
                pygame.draw.line(screen, green, (x_pos*100 + 85, y_pos*100 + 15), (x_pos*100 + 15, y_pos*100 + 85), line_width)

            if k == -1:
                pygame.draw.circle(screen, red, (x_pos*100+50,y_pos*100+50), 38, line_width)
            
            y_pos += 1
        x_pos += 1
        
def check_winner():
    global winner
    global game_over
    y_pos = 0

    for i in markers:
        #check coloumns
        if sum(i) == 3:
            winner = 1
            game_over = True

        if sum(i) == -3:
            winner = 2
            game_over = True

        if (markers[0][y_pos]+ markers[1][y_pos]+ markers[2][y_pos] == 3):
            winner = 1
            game_over = True

        if (markers[0][y_pos]+ markers[1][y_pos]+ markers[2][y_pos] == -3):
            winner = 2
            game_over = True
        
        y_pos += 1

        
    #check cross
    if(markers[0][0]+markers[1][1]+markers[2][2] == 3) or (markers[0][2]+markers[1][1]+markers[2][0] == 3):
        winner = 1
        game_over = True
    

    if(markers[0][2]+markers[1][1]+markers[2][0] == -3) or (markers[0][0]+markers[1][1]+markers[2][2] == -3):
        winner = 2
        game_over = True

    
def draw_winner(winner):
    win_text = "Player  " + str(winner) + "wins!"
    win_text2 = "Press R to Restart "
    win_img2 = font.render(win_text2,True,blue)
    win_img = font.render(win_text, True, blue)
    pygame.draw.rect(screen,green,(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2-60, 200, 50))
    pygame.draw.rect(screen,green,(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 110, 250, 50))
    screen.blit(win_img,(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
    screen.blit(win_img2,(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 100))







        


run = True
while run:

    draw_grid()
    draw_marker()
    
    #add event handlers
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

            
        if i.type == pygame.KEYDOWN and i.key == pygame.K_r:
            reset_game()


        if game_over == False:

            if i.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if i.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if(markers[cell_x//100][cell_y//100] == 0):
                    markers[cell_x//100][cell_y//100] = player
                    player *= -1
                    check_winner()
                    print(markers,"\n")

    if game_over == True:
        draw_winner(winner)




    
    
    
    pygame.display.update()

    

pygame.quit()
