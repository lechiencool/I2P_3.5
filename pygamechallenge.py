import pygame
import os

pygame.init()

bass = pygame.mixer.Sound(os.path.join('data', '/Users/s170142/PycharmProjects/I2P_3.5/basssynth.wav'))
crash = pygame.mixer.Sound(os.path.join('data', '/Users/s170142/PycharmProjects/I2P_3.5/crash.wav'))
dancefloor = pygame.mixer.Sound(os.path.join('data', '/Users/s170142/PycharmProjects/I2P_3.5/dancefloorpattern.wav'))
popsynth = pygame.mixer.Sound(os.path.join('data', '/Users/s170142/PycharmProjects/I2P_3.5/popsynth.wav'))
drum = pygame.mixer.Sound(os.path.join('data', '/Users/s170142/PycharmProjects/I2P_3.5/drumbeat.wav'))
techno = pygame.mixer.Sound(os.path.join('data', '/Users/s170142/PycharmProjects/I2P_3.5/technosynth.wav'))
screen = pygame.display.set_mode((500,500))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                bass.play()
            if event.key == pygame.K_a:
                crash.play()
            if event.key == pygame.K_s:
                dancefloor.play()
            if event.key == pygame.K_d:
                popsynth.play()
            if event.key == pygame.K_f:
                drum.play()
            if event.key == pygame.K_g:
                techno.play()
            if event.key == pygame.K_q:
                done = True

pygame.quit()
