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

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('GUI Speech Recognition')

current_path = os.path.dirname(__file__) 
#resource_path = os.path.join(current_path, 'test') 
image_path = os.path.join('MG') 

#sound_path = os.path.join('Sound') 


    


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
    load_the_image('dog.jpg'),
    load_the_image('green.jpg'),
    load_the_image('red.jpg'),
    load_the_image('yellow.jpg'),
    load_the_image('circle.jpg'),
    load_the_image('square.jpg'),
    load_the_image('triangle.jpg')
]


def plays():
    
    for i in range(1,7):
       
       
     
      if i== 1:

        carImg = pygame.image.load(os.path.join(image_path,'cat.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
        
    
        if text == 'cat':
            print(text)
            print('good job') 
        else:
            print(text)
            print('wrong')
        time.sleep(7)
      
       
      elif i== 2:

        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'monkey':
            print(text)
            print('good job') 
        else:
            print(text)
            print('wrong')
        time.sleep(7)
       
      elif i== 3:
           
        carImg = pygame.image.load(os.path.join(image_path,'dog.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
            if text == 'dog':
                print('good job') 
        else:
            print('wrong')
        time.sleep(7)
       
      elif i== 4:
           
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
            if text == 'green':
                print('good job') 
        else:
            print('wrong')
            time.sleep(7)
        
      elif i== 5:
           
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
            if text == 'red':
                print('good job')
        else:
            print('wrong')
            time.sleep(7)
        
      elif i== 6:
           
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
            if text == 'yellow':
                print('good job')
        else:
            print('wrong')
            time.sleep(7)   
      
      elif i== 7:
           
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
            if text == 'circle':
                print('good job')
        else:
            print('wrong')
            time.sleep(7)
     
      elif i== 8:
           
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
            if text == 'square':
                print('good job')
        else:
            print('wrong')
            time.sleep(7)
      
      elif i== 9:
          
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
            if text == 'triangle':
                print('good job')
        else:
            print('wrong')
            time.sleep(7)


def s2te():
  
          
     
   

   for i in range(1,10):
       
       
       if i== 1:

        carImg = pygame.image.load(os.path.join(image_path,'cat.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'cat':
            print('good job') 
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
        time.sleep(7)
      
       
       elif i== 2:

        carImg = pygame.image.load(os.path.join(image_path,'monkey.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'monkey':
            print('good job') 
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
        time.sleep(7)
       
       elif i== 3:
           
        carImg = pygame.image.load(os.path.join(image_path,'dog.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'dog':
            print('good job')
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
        time.sleep(7)
       
       elif i== 4:
           
        carImg = pygame.image.load(os.path.join(image_path,'green.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'green':
            print('good job')
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
            time.sleep(7)
        
       elif i== 5:
           
        carImg = pygame.image.load(os.path.join(image_path,'red.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'red':
            print('good job')
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
            time.sleep(7)
        
       elif i== 6:
           
        carImg = pygame.image.load(os.path.join(image_path,'yellow.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'yellow':
            print('good job')
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
            time.sleep(7)   
      
       elif i== 7:
           
        carImg = pygame.image.load(os.path.join(image_path,'circle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'circle':
            print('good job')
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
            time.sleep(7)
     
       elif i== 8:
           
        carImg = pygame.image.load(os.path.join(image_path,'square.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'square':
            print('good job')
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
            time.sleep(7)
      
       elif i== 9:
           
        carImg = pygame.image.load(os.path.join(image_path,'triangle.jpg'))
        gameDisplay.blit(carImg,(130,0))
        pygame.display.update()
        r = sr.Recognizer()
        with sr.Microphone() as source:
    
            print ('Say Something!')
            audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
        except:
            print('Did not get that')
            text=''
    
        if text == 'triangle':
            print('good job')
            pygame.mixer.Sound.play(right)
            pygame.mixer.music.stop()
        else:
            print('wrong')
            pygame.mixer.Sound.play(wrong)
            pygame.mixer.music.stop()
            time.sleep(7)
def main():
   while True:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
       button("Play! in English",150,450,100,50,green,bright_green,s2te)
       button("Play! in Spanish",350,450,100,50,green,bright_green,plays)
       button("Quit",550,450,100,50,red,bright_red,close)
       pygame.display.update()

if __name__ == '__main__':
   main()
