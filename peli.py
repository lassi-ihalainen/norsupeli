# Credits:
# Lassi Ihalainen

import pygame
import time
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

display_width = 800
display_height = 600

black = (0,0,0) #defines colors
white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode ((display_width,display_height))
pygame.display.set_caption("Norsupeli") #top bar name
clock = pygame.time.Clock()

char_height=155 #hitbox size
char_width=200

x = display_width * 0.2 #place of the character on screen
y = display_height * 0.3

projectile = False

eye_x = x+170
eye_y = y+37

scoreAlreadyGiven = 0
scorenumber = 0

y_change = 5 #speed of character dropping

charImg = pygame.image.load('C:/Users/lassi/Documents/Python/Norsu3.png') #file of character image
explosionImg = pygame.image.load('C:/Users/lassi/Documents/Python/jajahdys.png')
backgroundImg = pygame.image.load("C:/Users/lassi/Documents/Python/Tausta3.png")
backgroundImg2 = pygame.image.load("C:/Users/lassi/Documents/Python/Tausta-aurinko2.png")

JumpSFX=pygame.mixer.Sound("hyppy.wav")
ShotSFX=pygame.mixer.Sound("laser.wav")
ExplosionSFX=pygame.mixer.Sound("rajahdys.wav")

def start_screen():
    gameDisplay.fill(white)
    startTextFont= pygame.font.SysFont("comicsansms",60)
    TextSurf, TextRect = text_objects("PRESS SPACE TO START", startTextFont)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                game_loop()

def avoid(avoidx, avoidy, avoidw, avoidh, color):
    pygame.draw.rect(gameDisplay, color, [avoidx, avoidy, avoidw, avoidh]) #function drawing the flying boxes

def char (x,y):
    gameDisplay.blit(charImg,(x,y)) #inserts the char image

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text, scorenumber, highscore):
    largeText = pygame.font.SysFont("comicsansms",120) #defines font and size
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/3)) #defines location of text
    gameDisplay.blit(TextSurf, TextRect) #adds the text rectangle to screen
    pygame.display.update() #updates the screen with the text
    score_display("YOUR SCORE: " + str(scorenumber) + "       HIGHSCORE: " + str(highscore))
    
    time.sleep(1.5) #text appears for 0,5 seconds

    game_loop() #starts the game over

def text_objects_score(HS_text, font):
    scoresurface = font.render(HS_text, True, red)
    return scoresurface, scoresurface.get_rect()

def score_display(HS_text):
    textfont = pygame.font.SysFont("comicsansms",40) #textfont is variable containing font and font size
    scoresurface, scorerectangle = text_objects_score(HS_text, textfont)
    scorerectangle.center = ((display_width/2), ((display_height/3)*2))
    gameDisplay.blit(scoresurface, scorerectangle)
    pygame.display.update()
    
def text_objects2(scorenumber, scorefont):
    textSurface = scorefont.render(str(scorenumber), True, red)
    return textSurface, textSurface.get_rect()
 
def score(scorenumber):
    scorefont = pygame.font.SysFont ("comicsansms", 100)
    ScoreSurf, ScoreRect = text_objects2(scorenumber, scorefont)
    ScoreRect.topleft = (20, 20)
    gameDisplay.blit (ScoreSurf, ScoreRect)
    pygame.display.update()

def hit(scorenumber):
    fileObject = open("highscore.txt", "r")
    highscore = fileObject.read()
    if int(scorenumber) >= int(highscore):
        update_highscore(scorenumber)
    message_display("U R DED", scorenumber, highscore)

def update_highscore(scorenumber):
    fileObject = open("highscore.txt", "w")
    fileObject.write(str(scorenumber))
        
def shoot(shootx, shooty, shootw, shooth, color, shots_fired):
    pygame.draw.rect(gameDisplay, color, [shootx, shooty, shootw, shooth])

    
def game_loop():
    scorenumber = 0 #resets the score
    scrolling_x = 0
    x = display_width * 0.2 #place of the character on screen
    y = display_height * 0.3

    heightLaunch = 0
    projectile = False
    
    avoid_speed = -5 #speed of the boxes
    avoid_width = 100 #size of boxes

    avoid_height = 100
    avoid_starty = random.randrange(0, display_height - avoid_height) #randomizes the starting height of the boxes
    avoid_startx = display_width # spawns the boxes at the edge of the screen
    shoot_width = 70
    shoot_height = 7
    eye_x = x+170
    eye_y = y+37
    shots_fired = 0
    y_change = 5
    scoreAlreadyGiven = 0
    gameExit = False
    
    while not gameExit:
        gameDisplay.blit(backgroundImg2, (0, 0))
        scrolling_x -= 3
        gameDisplay.blit(backgroundImg, (scrolling_x, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -10
                    JumpSFX.play()
                if event.key == pygame.K_DOWN:
                    y_change = 10
                    JumpSFX.play()
                if event.key == pygame.K_SPACE and eye_x > x+170:
                   () 
                    
                elif event.key == pygame.K_SPACE:
                    shots_fired += 1
                    heightLaunch = y + 37
                    eye_x = x+170
                    projectile = True
                    ShotSFX.play()
                    
                if event.key == pygame.K_ESCAPE:
                    quit()   
                    
            else:
                    y_change = 5
                     
        y += y_change

        if projectile == True:
            shoot(eye_x, heightLaunch, shoot_width, shoot_height, blue, shots_fired)
            
        avoid(avoid_startx, avoid_starty, avoid_width, avoid_height, black)
             
        char(x,y)

        if scrolling_x  <= -1054: #right side of equation is the subtraction of two identical points' x-coordinates (palm trees)
            scrolling_x = 0

        if eye_x >= display_width:
            eye_x = -100
            projectile = False
        elif projectile == True:
            eye_x += 10
            
        if (heightLaunch <= avoid_starty +avoid_height and heightLaunch + shoot_height >= avoid_starty) and (eye_x + shoot_width >= avoid_startx and x <= avoid_startx + avoid_width) :
            eye_x = -100
            projectile = False
            gameDisplay.blit(explosionImg,(avoid_startx, avoid_starty))
            avoid_startx = display_width
            avoid_starty = random.randrange(0, display_height - avoid_height)
            scorenumber += 1
            avoid_speed -= 1
            ExplosionSFX.play()
            
            
        if y > display_height - char_height or y<0:
            hit(scorenumber)

        if avoid_startx < 0:
            avoid_startx = display_width
            avoid_starty = random.randrange(0, display_height-avoid_height)
            scoreAlreadyGiven = 0

        if (y <= avoid_starty +avoid_height and y + char_height >= avoid_starty) and (x + char_width >= avoid_startx and x <= avoid_startx + avoid_width): 
            hit(scorenumber)

        if x - avoid_width >= avoid_startx and scoreAlreadyGiven == 0:
            scoreAlreadyGiven += 1
            avoid_speed -= 1
            scorenumber += 1
            
        
        avoid_startx += avoid_speed
        score(scorenumber)
        pygame.display.update()
        clock.tick(60)
        
start_screen()
pygame.quit()
quit()
