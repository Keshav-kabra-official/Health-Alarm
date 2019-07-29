'''
 @author : Keshav Kabra
'''

import time
import os
import pygame
import datetime

def music():
    print("It's time for Walk, drinking Water and relaxation to Eyes ...",
          "press 'x' and hit 'enter' when you are done ...")

    pygame.mixer.init()
    pygame.mixer.music.load("m2.mp3")
    pygame.mixer.music.play(-1)
    while True:
        a = input("Input : ")
        if a == 'x' or a == 'X':
            pygame.mixer.music.stop()
            break
        else:
            print("Oops!! It seems not to be 'x'")

def timer():
    sec = 1800   # for 30min set it to 1800

    while sec > 0:
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)

        time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print("Time-left for taking a Health Dose : ", time_left + '\r', end="")
        time.sleep(1)
        os.system('cls')
        sec -= 1


def log():
    x = datetime.datetime.now()
    x = x.strftime("%d-%m-%Y  %I:%M:%S(%p)")
    with open("log.txt", "a") as file:
        file.write("Health-Dose taken at : " + x + "\n")


if __name__ == "__main__":
    for i in range(8):
        timer()
        music()
        pygame.mixer.music.stop()
        log()