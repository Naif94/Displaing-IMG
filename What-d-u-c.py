#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:05:33 2020

@author: naifali
"""

import glob
import pygame
import time
import speech_recognition as sr

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Recognizing pictures')



def close():
   pygame.quit()
   quit()

def message_display(text):
   largeText = pygame.font.Font('freesansbold.ttf',30)
   TextSurf, TextRect = text_objects(text, largeText)
   TextRect.center = ((display_width/2),(display_height/2))
   gameDisplay.blit(TextSurf, TextRect)

   pygame.display.update()


def text_objects(text, font):
   textSurface = font.render(text, True, alpha)
   return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
   mouse = pygame.mouse.get_pos()
   click = pygame.mouse.get_pressed()
   if x+w > mouse[0] > x and y+h > mouse[1] > y:
       pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

       if click[0] == 1 and action != None:
           action()         
   else:
       pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

   smallText = pygame.font.SysFont("comicsansms",20)
   textSurf, textRect = text_objects(msg, smallText)
   textRect.center = ( (x+(w/2)), (y+(h/2)) )
   gameDisplay.blit(textSurf, textRect)

def s2t():
   
   r = sr.Recognizer()

   with sr.Microphone() as source:
       print ('Say Something!')
       audio = r.listen(source)
       print ('Done!')

   image_list = []

   for filename in glob.glob('IMG/*.jpg'):
    
    image_list.append(pygame.image.load(filename))
    
    name_list = ['monkey', 'cat', 'dog'] 
    text = r.recognize_google(audio)
   
   try:
    index = name_list.index(text)
   except ValueError:
    index = -1

    gameDisplay.fill(white)
    if 0 <= index <= len(image_list): 
        gameDisplay.blit(image_list[index], (130,0))
    pygame.display.update()

    if index > 0:
        message_display('good job')
    else:
        message_display('wrong')


def main():
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
       button("ans!",150,450,100,50,green,bright_green,s2t)
       button("Quit",550,450,100,50,red,bright_red,close)
       pygame.display.update()

if __name__ == '__main__':
   main()
