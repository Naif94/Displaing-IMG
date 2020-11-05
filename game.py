import os
import glob
import pygame
import time
import speech_recognition as sr



pygame.init()

r= open("/Users/naifali/Desktop/test/Sound/wrong.wav",)
s= open("/Users/naifali/Desktop/test/Sound/right.wav",)

wrong = pygame.mixer.Sound(r)

right = pygame.mixer.Sound(s)

display_width = 800
display_height = 600

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

            carImg = pygame.image.load(os.path.join(image_path,'tiger.jpg'))
            gameDisplay.blit(carImg,(130,0))
            pygame.display.update()
            
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong try again')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
            time.sleep(4)
      
       
      elif i== 2:

        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
         
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong ya wad')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
       
      elif i== 3:
           
        carImg = pygame.image.load(os.path.join(image_path,'panda.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
       
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
       
      elif i== 4:
           
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
        
      elif i== 5:
           
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
        
      elif i== 6:
           
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)   
      
      elif i== 7:
           
        carImg = pygame.image.load(os.path.join(image_path,'heart.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
      
      elif i== 8:
           
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
     
      elif i== 9:
           
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
      
      elif i== 10:
           
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        pygame.mixer.Sound.play(right)
                        pygame.mixer.music.stop()
                        break
                    else:
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
      


def play_in_eg():
  
          
     
   

   for i in range(1,11):
       
       
       if i== 1:

            carImg = pygame.image.load(os.path.join(image_path,'tiger.jpg'))
            gameDisplay.blit(carImg,(130,0))
            pygame.display.update()
            
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
                        print('wrong try again')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
            time.sleep(4)
      
       
       elif i== 2:

        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
         
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
                        print('wrong ya wad')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
       
       elif i== 3:
           
        carImg = pygame.image.load(os.path.join(image_path,'panda.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
       
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
       
       elif i== 4:
           
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
        
       elif i== 5:
           
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
        
       elif i== 6:
           
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)   
      
       elif i== 7:
           
        carImg = pygame.image.load(os.path.join(image_path,'heart.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
     
       elif i== 8:
           
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
       
       elif i== 9:
           
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
        time.sleep(4)
      
       elif i== 10:
           
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
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
                        print('wrong')
                        pygame.mixer.Sound.play(wrong)
                        pygame.mixer.music.stop()
                        time.sleep(3)
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