import math as m
import time
import winsound
import pyttsx3
import pygame
def show_image(img):
    img = pygame.image.load(img)
    size = img.get_rect().size
    pygame.display.set_caption('The Promodoro by Jalis Tarif')
    screen = pygame.display.set_mode(size)
    screen.blit(img, (0, 0))
    pygame.display.flip()
def close_image():
    pygame.display.quit()

def voice_message(msg):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 120)
    engine.say(msg)
    engine.runAndWait()
    engine.stop()

def promodoro():
    show_image('start.jpg')
    for _ in range(5):
        winsound.PlaySound('beep-24.wav', winsound.SND_FILENAME)
    voice_message("Please start working for next twenty five minutes")
    close_image()
    time.sleep(1500)

    show_image('rest.jpg')
    for _ in range(5):
         winsound.PlaySound('beep-30b.wav', winsound.SND_FILENAME)
    voice_message("Please take three minutes rest")
    close_image()
    time.sleep(170)
    

def main():
    total_working_time=float(input("Enter total working hour:"))
    total_interval=m.ceil((total_working_time*60)/25)
    for _ in range(total_interval):
        promodoro()
    

main()