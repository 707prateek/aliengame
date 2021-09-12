import pygame
#This line is important to run our window
screen=pygame.display.set_mode((1200,600))
running=True
while running:
    ask=input("if you want to quit type q and enter")
    if ask=='q':
        running=False