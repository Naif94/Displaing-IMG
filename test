import os
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
pygame.display.set_caption('GUI Speech Recognition')

current_path = os.path.dirname(__file__) 
resource_path = os.path.join(current_path, 'test') 
image_path = os.path.join(resource_path, 'MG') 

#image_list = []
#for filename in glob.glob('MG/*.jpg'):
    #image_list.append(filename)
    


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

def load_the_image(image):
    return pygame.image.load(os.path.join(image_path,image))

images = [
    load_the_image('cat.jpg'),
    load_the_image('monkey.jpg'),
    load_the_image('dog.jpg')
]

WINDOW = pygame.display.set_mode((800,800))


def s2t():
  # gameDisplay.blit(carImg,(0,0))
   r = sr.Recognizer()

   with sr.Microphone() as source:
       print ('Say Something!')
       audio = r.listen(source)
       print ('Done!')

   text = r.recognize_google(audio)
   print(text)
   
   


   for i in range(len(images)):
       WINDOW.blit(i)
       if i == 1:
           index=0
           gameDisplay.fill(white)
           carImg = pygame.image.load(images[index])
           pygame.display.update()
           gameDisplay.blit(carImg,(130,0))
           
           if text == 'cat':
               message_display('good job')
           else:
               message_display('wrong')
               
       elif i== 2:
           index=1
           gameDisplay.fill(white)
           carImg = pygame.image.load(images[index])
           pygame.display.update()
           gameDisplay.blit(carImg,(130,0))
           
           if text == 'monkey':
               message_display('good job')
           else:
               message_display('wrong')
       elif i== 3:
           index=2
           gameDisplay.fill(white)
           carImg = pygame.image.load(images[index])
           pygame.display.update()
           gameDisplay.blit(carImg,(130,0))
           
           if text == 'dog':
               message_display('good job')
           else:
               message_display('wrong')
               

def main():
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
       button("Speak!",150,450,100,50,green,bright_green,s2t)
       button("Quit",550,450,100,50,red,bright_red,close)
       pygame.display.update()

if __name__ == '__main__':
   main()
