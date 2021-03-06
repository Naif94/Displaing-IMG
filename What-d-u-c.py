import os
import glob
import pygame
import time
import speech_recognition as sr
import random  # we use this to make a random right button
import sys
from gpiozero import LED
from time import sleep

riht=LED(18)
RR=LED(17)

pygame.init()
""" loading English audio files """
right = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/right.wav")
wrong= pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/ again.wav")

Tiger = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Tiger.wav")
Monkey= pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Monkey.wav")
Panda = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Panda.wav")
Green = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Green.wav")
Red = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Red.wav")
Yellow = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Yellow.wav")
Heart = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Heart.wav")
Circle = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/Circle.wav")
Square = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/square.wav")
Triangle = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/triangle.wav")

# Spanih audio files
right_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Good_job.wav")
wrong_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Tagane_sp.wav")

Tiger_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Tiger.wav")
Monkey_e= pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Monkey_mono.wav")
Panda_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Panda_oso Panda.wav")
Green_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Green_Verde.wav")
Red_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Red_Rojo.wav")
Yellow_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Yellow_amarillo.wav")
Heart_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/HeartCorazon.wav")
Circle_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Circle_Circulo.wav")
Square_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Square_Cuadrado.wav")
Triangle_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/Triangle_Triangulo_1.wav")



display_width = 600
display_height = 480

black = (0,0,0)
alpha = (0,88,255)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
purple = (102, 0, 102)
bright_purple= (153, 0, 153)
blue = (0, 0, 255)
bright_bule = (0, 255, 0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
#, pygame.FULLSCREEN
pygame.display.set_caption(' Recognizing the Image ')

current_path = os.path.dirname(__file__) 

image_path = os.path.join('resized') 




    


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

def button(msg, x, ic, ac, action=None):
    y =250;
    w=100;
    h=50;
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
            pygame.time.wait(200)
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def load_the_image(image):
    return pygame.image.load(os.path.join(image_path,image))
images = [
    load_the_image('tiger.jpg'),
    load_the_image('monkey.jpg'),
    load_the_image('panda.jpg'),
    load_the_image('green.jpg'),
    load_the_image('red.jpg'),
    load_the_image('yellow.jpg'),
    load_the_image('circle.jpg'),
    load_the_image('square.jpg'),
    load_the_image('triangle.jpg'),
    load_the_image('heart.jpg')
]


def play_in_sp():
    
    for i in range(1,11):
       
       #
      if i== 1:
            counter = 0
            carImg = pygame.image.load(os.path.join(image_path,'tiger.jpg'))
            gameDisplay.blit(carImg,(0,0))
            pygame.display.update()
            pygame.mixer.Sound.play(Tiger_e)
            pygame.mixer.music.stop()
            time.sleep(17)
            for j in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
            
                    if text == 'tigre' or 'Tigre':
                        print('good job') 
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
            time.sleep(4)
      
       
      elif i== 2:
        counter = 0
        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Monkey_e)
        pygame.mixer.music.stop()
        time.sleep(9)
         
        for a in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
        
                    if text == 'mona' or 'Mona':
                        print('good job') 
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
      elif i== 3:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'panda.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Panda_e)
        pygame.mixer.music.stop()
        time.sleep(11)
        for b in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'panda'or'Panda':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
      elif i== 4:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Green_e)
        pygame.mixer.music.stop()
        time.sleep(9)
        for c in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'verde' or'Verde':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
      elif i== 5:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Red_e)
        pygame.mixer.music.stop()
        time.sleep(10)
        for d in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'roja' or 'roja':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
      elif i== 6:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Yellow_e)
        pygame.mixer.music.stop()
        time.sleep(12)
        for e in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'amarilla' or 'amarillo':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)   
      
      elif i== 7:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'heart.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Heart_e)
        pygame.mixer.music.stop()
        time.sleep(11)
        for f in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'corazón' or 'Corazón'or 'corazon'or' corazon':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
      
      elif i== 8:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Circle_e)
        pygame.mixer.music.stop()
        time.sleep(9)
        for f in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'circulo' or 'Circulo':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
     
      elif i== 9:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Square_e)
        pygame.mixer.music.stop
        time.sleep(11)
        for g in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'Cuadrada'or 'cuadrada'or 'Cuadrado'or 'cuadrado':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
      
      elif i== 10:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Triangle_e)
        pygame.mixer.music.stop()
        time.sleep(13)
        for h in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio, language='es-MX')
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'triángulo'or 'Triángulo':
                        print('good job')
                        pygame.mixer.Sound.play(right_e)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        

def play_in_eg():
  
          
     
   

   for i in range(1,11):
       
       
       if i== 1:
            counter = 0
            carImg = pygame.image.load(os.path.join(image_path,'tiger.jpg'))
            gameDisplay.blit(carImg,(0,0))
            pygame.display.update()
            pygame.mixer.Sound.play(Tiger)
            pygame.mixer.music.stop()
            time.sleep(8)
            for j in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
            
                    if text == 'tiger':
                        print('good job') 
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
            time.sleep(4)
      
       
       elif i== 2:
        counter = 0
        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Monkey)
        pygame.mixer.music.stop()
        time.sleep(8)
        for a in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
        
                    if text == 'monkey':
                        print('good job') 
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
       elif i== 3:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'panda.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Panda)
        pygame.mixer.music.stop()
        time.sleep(9)
        for b in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'panda':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
       elif i== 4:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Green)
        pygame.mixer.music.stop()
        time.sleep(8)
        for c in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'green':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
       elif i== 5:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Red)
        pygame.mixer.music.stop()
        time.sleep(8)
        for d in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'red':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
       elif i== 6:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Yellow)
        pygame.mixer.music.stop()
        time.sleep(7)
        for e in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'yellow':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)   
      
       elif i== 7:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'heart.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Heart)
        pygame.mixer.music.stop()
        time.sleep(7)
        for f in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'heart' or 'Heart':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
     
       elif i== 8:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Circle)
        pygame.mixer.music.stop()
        time.sleep(8)
        for f in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'circle' or 'Circle':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
       elif i== 9:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Square)
        pygame.mixer.music.stop()
        time.sleep(8)
        for g in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'square' or 'Square':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
      
       elif i== 10:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(0,0))
        pygame.display.update()
        pygame.mixer.Sound.play(Triangle)
        pygame.mixer.music.stop()
        time.sleep(9)
        for h in range(1,4):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
            
                     print ('Say Something!')
                     audio = r.listen(source)
                    try:
                        text = r.recognize_google(audio)
                        print(text)
                    except:
                        print('Did not get that try Again')
                        text=''
    
                    if text == 'triangle':
                        print('good job')
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        riht.on()
                        sleep(2)
                        riht.off()
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            RR.on()
                            sleep(2)
                            RR.off()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)


def Game1():
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
       carImg = pygame.image.load(os.path.join(image_path,'Cover.jpg'))
       gameDisplay.blit(carImg,(0,0))       
       button("English",250,green,bright_green,play_in_eg)
       button("Spanish",350,purple,bright_purple,play_in_sp)
       button("Quit",450,red,bright_red,close)
       pygame.display.update()






""" This function is to print & display good job massege in English"""  
def Check_right():
    global screen
    gameDisplay.blit(Img, (0, 0))
    message_display("good job")
    pygame.mixer.Sound.play(right)
    pygame.mixer.music.stop()
    riht.on()
    sleep(2)
    riht.off()
    print("good job")
    screen += 1


""" This function is to print & display Wrong massege"""


def Check_wrong():
    gameDisplay.blit(Img, (0, 0))
    message_display("wrong")
    pygame.mixer.Sound.play(wrong)
    pygame.mixer.music.stop()
    RR.on()
    sleep(2)
    RR.off()
    print("wrong")



""" This function is to print & display good job massege in spanish"""

def Check_right_s():
    global screen
    gameDisplay.blit(Img, (0, 0))
    message_display("Salidas")
    pygame.mixer.Sound.play(right_e)
    pygame.mixer.music.stop()
    riht.on()
    sleep(2)
    riht.off()
    print("good job")
    screen += 1
""" This function is to print & display Wrong massege"""
def Check_wrong_s():
    gameDisplay.blit(Img, (0, 0))
    message_display("Buen Trabajo")
    pygame.mixer.Sound.play(wrong_e)
    pygame.mixer.music.stop()
    RR.on()
    sleep(2)
    RR.off()
    print("wrong")



""" This fuction is to take the screeen vaule from main fuction 
and increase it by one"""
def game():
    global screen
    screen +=1
    
    
""" This fuction is to take the screeenS vaule wich is equal to 4
    from main fuction  and increase it by one"""
def gameS():
    global screen
    screen = screenS +1
    
    
"""" In The main function is to show the frist screen with 
two buttons options play or quit. if the user choes quit. the game will quit.
On the other hand, if the user choses to play button. it is going
 to take him 
to game function  """

def Game2():
    NewRightButton = random.randint(1, 2)
    Zyaid = True
    global screen
    global screenS
    global Img
    screen = 0
    screenS = 13
    while Zyaid:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if screen==0 and screenS==13 :
            
            Img =   pygame.image.load(os.path.join(image_path, "lalaa.jpg"))
            gameDisplay.blit(Img, (0, 0))
            button("Quit",450,red, bright_red, close)
            button("English",350,green, bright_green, game)
            button("Spanish",250,blue, bright_bule, gameS)
            pygame.display.update()

        elif screen==1:
            Img =   pygame.image.load(os.path.join(image_path, "tiger.jpg"))
            gameDisplay.blit(Img, (0, 0))
            
            if NewRightButton == 1:
                button("Tiger", 150,  green, bright_green, Check_right)
                button("Dog", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cat", 150,  green, bright_green, Check_wrong)
                button("Tiger", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==2:
            Img =   pygame.image.load(os.path.join(image_path, "panda.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Panda", 150,  green, bright_green, Check_right)
                button("Fish", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Fish", 150,  green, bright_green, Check_wrong)
                button("Panda", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==3:
            Img =   pygame.image.load(os.path.join(image_path, "monkey.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Monkey", 150,  green, bright_green, Check_right)
                button("Duck", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Duck", 150,  green, bright_green, Check_wrong)
                button("Monkey", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==4:
            Img =   pygame.image.load(os.path.join(image_path, "cat.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Cat", 150,  green, bright_green, Check_right)
                button("Elephant", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Elephant", 150,  green, bright_green, Check_wrong)
                button("Cat", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==5:
            Img =   pygame.image.load(os.path.join(image_path, "blue.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Blue", 150,  green, bright_green, Check_right)
                button("White", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("White", 150,  green, bright_green, Check_wrong)
                button("Blue", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
                
        elif screen==6:
            Img =   pygame.image.load(os.path.join(image_path, "yellow.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Yellow", 150,  green, bright_green, Check_right)
                button("Black", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Black", 150,  green, bright_green, Check_wrong)
                button("Yellow", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==7:
            Img =   pygame.image.load(os.path.join(image_path, "red.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("red", 150,  green, bright_green, Check_right)
                button("pink", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("pink", 150,  green, bright_green, Check_wrong)
                button("red", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==8:
            Img =   pygame.image.load(os.path.join(image_path, "green.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("green", 150,  green, bright_green, Check_right)
                button("brown", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Brown", 150,  green, bright_green, Check_wrong)
                button("green", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==9:
            Img =   pygame.image.load(os.path.join(image_path, "heart.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Heart", 150,  green, bright_green, Check_right)
                button("Triangle", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Triangle", 150,  green, bright_green, Check_wrong)
                button("Cubic", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==10:
            Img =   pygame.image.load(os.path.join(image_path, "square.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Square", 150,  green, bright_green, Check_right)
                button("Cubic", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Black", 150,  green, bright_green, Check_wrong)
                button("Square", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==11:
            Img =   pygame.image.load(os.path.join(image_path, "triangle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Triangle", 150,  green, bright_green, Check_right)
                button("Cylinder", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cylinder", 150,  green, bright_green, Check_wrong)
                button("Triangle", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==12:
            Img =   pygame.image.load(os.path.join(image_path, "circle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Circle", 150,  green, bright_green, Check_right)
                button("Cubick", 50, blue, bright_bule, Check_wrong)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cubic", 150,  green, bright_green, Check_wrong)
                button("Circle", 50, blue, bright_bule, Check_right)
                button("Quit", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==13:
            Img = pygame.image.load(os.path.join(image_path, "Lala_showerd.jpg"))
            gameDisplay.blit(Img, (0, 0))
            message_display("end of the game")
            button("Quit", 450, red, bright_red, close)
            pygame.display.update()
            print("end of the game")
            main()
            """ here is the spanish language """
        elif screen== 14:
            Img = pygame.image.load(os.path.join(image_path, "tiger.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Tigre", 150,  green, bright_green, Check_right_s)
                button("Perro", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
            else:
                button("Perro", 50, blue, bright_bule, Check_wrong_s)
                button("Tigre", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==15:
            Img =   pygame.image.load(os.path.join(image_path, "panda.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Oso", 150,  green, bright_green, Check_right_s)
                button("Pescado", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Pescado", 150,  green, bright_green, Check_wrong_s)
                button("Oso", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

        elif screen==16:
            Img =   pygame.image.load(os.path.join(image_path, "monkey.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Mono", 150,  green, bright_green, Check_right_s)
                button("Pato", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Pato", 150,  green, bright_green, Check_wrong_s)
                button("Mono", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==17:
            Img =   pygame.image.load(os.path.join(image_path, "cat.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Gato", 150,  green, bright_green, Check_right_s)
                button("Elefante", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Elefante", 150,  green, bright_green, Check_wrong_s)
                button("Gato", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==18:
            Img =   pygame.image.load(os.path.join(image_path, "blue.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Azul", 150,  green, bright_green, Check_right_s)
                button("Blanco", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Blanco", 150,  green, bright_green, Check_wrong_s)
                button("Azul", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
                
        elif screen==19:
            Img =   pygame.image.load(os.path.join(image_path, "yellow.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Amarillo", 150,  green, bright_green, Check_right_s)
                button("Negro", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Negro", 150,  green, bright_green, Check_wrong_s)
                button("Amarillo", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==20:
            Img =   pygame.image.load(os.path.join(image_path, "red.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Rojo", 150,  green, bright_green, Check_right_s)
                button("rosado", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Rosado", 150,  green, bright_green, Check_wrong_s)
                button("Rojo", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==21:
            Img =   pygame.image.load(os.path.join(image_path, "green.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Verde", 150,  green, bright_green, Check_right_s)
                button("Marron", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Marron", 150,  green, bright_green, Check_wrong_s)
                button("Verde", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==22:
            Img =   pygame.image.load(os.path.join(image_path, "heart.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Corazon", 150,  green, bright_green, Check_right_s)
                button("Triangulo", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Triangulo", 150,  green, bright_green, Check_wrong_s)
                button("Corazon", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==23:
            Img =   pygame.image.load(os.path.join(image_path, "square.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Cuadrodo", 150,  green, bright_green, Check_right_s)
                button("Cubico", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cubico", 150,  green, bright_green, Check_wrong_s)
                button("Cuadrodo", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==24:
            Img =   pygame.image.load(os.path.join(image_path, "triangle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Triangulo", 150,  green, bright_green, Check_right_s)
                button("Cilindro", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cilindro", 150,  green, bright_green, Check_wrong_s)
                button("Triangulo", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==25:
            Img =   pygame.image.load(os.path.join(image_path, "circle.jpg"))
            gameDisplay.blit(Img, (0, 0))
            if NewRightButton == 1:
                button("Circulo", 150,  green, bright_green, Check_right_s)
                button("Cubico", 50, blue, bright_bule, Check_wrong_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()

            else:
                button("Cubico", 150,  green, bright_green, Check_wrong_s)
                button("Circulo", 50, blue, bright_bule, Check_right_s)
                button("Salidas", 450,  red, bright_red, close)
                pygame.display.update()
        elif screen==26:
            Img = pygame.image.load(os.path.join(image_path, "elif.jpg"))
            gameDisplay.blit(Img, (0, 0))
            message_display("Fin del juego")
            button("Salidas", 450, red, bright_red, close)
            pygame.display.update()
            print("end of the game")
            main()

def main():
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
       carImg = pygame.image.load(os.path.join(image_path,'Cover.jpg'))
       gameDisplay.blit(carImg,(0,0))
       button("Game1",80,green,bright_green,Game1)
       button("Game2",180,purple,bright_purple,Game2)
       button("Quit",450,red,bright_red,close)
       pygame.display.update()

if __name__ == '__main__':
   main()


