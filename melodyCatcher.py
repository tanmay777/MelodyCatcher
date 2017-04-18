from __future__ import print_function
import pygame
import os
import timeit
from time import sleep
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

button1=38
button2=11
button3=12
button4=13
button5=15
button6=16

LED1=31
LED2=32
LED3=33
LED4=35
LED5=36
LED6=37
time=0

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button6,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)
GPIO.setup(LED6,GPIO.OUT)

flagMusic=0
second=0
minutes=0
start_time=0
end_time=0

os.system('clear')

print("Welcome to the game")
x=input("Enter the number of players ")
playersValue=[x]

flag_music=input("Enter 1 to start the game ")

if(flag_music):
    print ("The music will be played in ")
    for k in range(3,0,-1):
        sys.stdout.write("\r"+"{0}".format(k)+" seconds")
	sys.stdout.flush()
	sleep(1)
else:
    sys.exit()


tune=["e","d#","e","d#","e","b","d","c","a"]
completed=[]

pygame.mixer.init()
pygame.mixer.music.load("Resources/furliseMainTune.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

print("\nNow you have to play this music using the butttons")
print("The player who completes the fastest will win the game")
print("If you do a mistake then you would have to start again")
print("All the best!\n")

flag_music=input("Enter 1 to start the competition ")

#rectify k error

print(x)
for i in range(0,x,1):
    flag_music=1
    k=0
    os.system('clear') #Why isn't it clearing?
    run=1
    chance=0
    tuneNew=[]
    try:
        while(run):
            if(flag_music==1):
                #play music code
                print("\nAll the best Player {}".format(i+1))
                flag_music=0
                sleep(1)
                start_time=timeit.default_timer()
                #timer_display(start_time)

            end_time=timeit.default_timer()
            sys.stdout.write('\rTimer: %.2f' %(end_time - start_time))

            if(GPIO.input(button1)==0):
#                print ("Button 1 was pressed")
                GPIO.output(LED2,0)
                GPIO.output(LED3,0)
                GPIO.output(LED4,0)
                GPIO.output(LED5,0)
                GPIO.output(LED6,0)
                GPIO.output(LED1,1)
                sleep(.25)
                pygame.mixer.init()
                pygame.mixer.music.load("Resources/ANote2(9).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
#		print(tuneNew)
                if(["e", "d#", "e", "d#", "e", "b", "d", "c"]==tuneNew):
                    k=k+1
                    tuneNew.append("a")
                    run=0
                    completed.append(1)
                    playersValue.append(end_time - start_time)
                else:
                    print("\nWrong button pressed. Start Again")
                    chance=chance+1
                    tuneNew=[]
            if(GPIO.input(button2)==0):
#               print ("Button 2 was pressed")
                GPIO.output(LED1,0)
                GPIO.output(LED3,0)
                GPIO.output(LED4,0)
                GPIO.output(LED5,0)
                GPIO.output(LED6,0)
                GPIO.output(LED2,1)
                sleep(.25)
                pygame.mixer.init()
                pygame.mixer.music.load("Resources/BNote2(6).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                if (["e", "d#", "e", "d#", "e"] == tuneNew):
                    k=k+1
                    tuneNew.append("b")
		else:
                    print("\nWrong button pressed. Start Again")
                    chance=chance+1
                    tuneNew=[]
            if(GPIO.input(button3)==0):
#                print ("Button 3 was pressed")
                GPIO.output(LED1,0)
                GPIO.output(LED2,0)
                GPIO.output(LED4,0)
                GPIO.output(LED5,0)
                GPIO.output(LED6,0)
                GPIO.output(LED3,1)
                sleep(.25)
                pygame.mixer.init()
                pygame.mixer.music.load("Resources/CNote(8).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                if (["e", "d#", "e", "d#", "e", "b", "d"] == tuneNew):
                    k=k+1
                    tuneNew.append("c")
		else:
                    print("\nWrong button pressed. Start Again")
                    tuneNew=[]
                    chance=chance+1
            if(GPIO.input(button4)==0):
                GPIO.output(LED1,0)
                GPIO.output(LED2,0)
                GPIO.output(LED3,0)
                GPIO.output(LED5,0)
                GPIO.output(LED6,0)
                GPIO.output(LED4,1)
#                print ("Button 4 was pressed")
                sleep(.25)
                pygame.mixer.init()
                pygame.mixer.music.load("Resources/Dnote(7).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                if (["e", "d#", "e", "d#", "e", "b"] == tuneNew):
                    k=k+1
                    tuneNew.append("d")
		else:
                    print("\nWrong button pressed. Start Again")
                    tuneNew=[]
                    chance=chance+1
            if(GPIO.input(button5)==0):
                GPIO.output(LED1,0)
                GPIO.output(LED2,0)
                GPIO.output(LED3,0)
                GPIO.output(LED4,0)
                GPIO.output(LED6,0)
                GPIO.output(LED5,1)
#                print ("Button 5 was pressed")
                sleep(.25)
                pygame.mixer.init()
                pygame.mixer.music.load("Resources/DSharpNote(2,4).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                if(["e", "d#", "e"] == tuneNew):
                    k=k+1
                    tuneNew.append("d#")
                elif (["e"] == tuneNew):
                    k=k+1
                    tuneNew.append("d#")
                else:
                    print("\nWrong button pressed. Start Again")
	            tuneNew=[]
                    chance=chance+1
            if (GPIO.input(button6) == 0):
#                print("Button 6 was pressed")
                GPIO.output(LED1, 0)
                GPIO.output(LED2, 0)
                GPIO.output(LED3, 0)
                GPIO.output(LED4, 0)
                GPIO.output(LED5, 0)
                GPIO.output(LED6, 1)
                sleep(.25)
                pygame.mixer.init()
                pygame.mixer.music.load("Resources/ENote(1,3,5).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
                if([]==tuneNew):
                    tuneNew.append("e")
                    k=k+1
                elif(["e","d#"]==tuneNew):
                    tuneNew.append("e")
                    k=k+1
                elif(["e", "d#", "e", "d#"]==tuneNew):
                    k=k+1
                    tuneNew.append("e")
                else:
                    print("\nWrong button pressed. Start Again")
                    chance=chance+1
                    tuneNew=[]

            if(chance==3):
		print("You have taken all your chances")
                completed.append(0)
                playersValue.append(end_time - start_time)
                run=0

    except KeyboardInterrupt:
        GPIO.cleanup()

lowest=round(playersValue[0],0)
bestplayer=0

os.system('clear')

print("\n")
for i in range(0,x,1):
    if(completed[i]==1):
        print("Player "+str(i+1)+" Timing: "+str(playersValue[i]))	
    else:
        print("Player "+str(i+1)+" Timing: Does not qualifies")
        
    if((round(playersValue[i],0)<lowest)and(completed[i]==1)):
        lowest=playersValue[i]
        bestplayer=i

no_of_players_completed=x

for i in range(0,x,1):
    if(completed[i]==0):
        no_of_players_completed=no_of_players_completed-1

if(no_of_players_completed!=0):
    print ("\nPlayer "+str(bestplayer+1),"Won the game!")
else:
    print ("\nEverybody lost. Nobody is winner")

