import pygame
#This line is important to run our window
screen=pygame.display.set_mode((1200,600))

#FOR WINDOW NOT DISAPPERING WE MADE A LOOP
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running==False