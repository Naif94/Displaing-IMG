import os
import glob
import pygame
import time
import speech_recognition as sr



pygame.init()
# English audio files
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
# right_e = pygame.mixer.Sound("/home/pi/Game/Audio_22050Fs/right_e.wav")
# wrong_e = pygame.mixer.Sound("/home/pi/Game/WAV_EN_22050Fs/wrong_e.wav")

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

display_width = 800
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
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption(' Recognizing the Image ')

current_path = os.path.dirname(__file__) 

image_path = os.path.join('MG') 




    


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
            gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
            time.sleep(4)
      
       
      elif i== 2:
        counter = 0
        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
      elif i== 3:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'panda.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
      elif i== 4:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
      elif i== 5:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
      elif i== 6:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)   
      
      elif i== 7:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'heart.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
      
      elif i== 8:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
     
      elif i== 9:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
      
      elif i== 10:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong_e)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
      


def play_in_eg():
  
          
     
   

   for i in range(1,11):
       
       
       if i== 1:
            counter = 0
            carImg = pygame.image.load(os.path.join(image_path,'tiger.jpg'))
            gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
            time.sleep(4)
      
       
       elif i== 2:
        counter = 0
        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
       elif i== 3:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'panda.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
       elif i== 4:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
       elif i== 5:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
        
       elif i== 6:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)   
      
       elif i== 7:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'heart.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
     
       elif i== 8:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
       
       elif i== 9:
        counter = 0   
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
      
       elif i== 10:
        counter = 0  
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(130,0))
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
                        break
                    else:
                        if counter <2:
                            print('wrong try again')
                            pygame.mixer.Sound.play(wrong)
                            pygame.mixer.music.stop()
                            time.sleep(3)
                            counter += 1
        time.sleep(4)
def main():
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
       button("English",150,350,100,50,green,bright_green,play_in_eg)
       button("Spanish",350,350,100,50,purple,bright_purple,play_in_sp)
       button("Quit",550,350,100,50,red,bright_red,close)
       pygame.display.update()



if __name__ == '__main__':
   main()

