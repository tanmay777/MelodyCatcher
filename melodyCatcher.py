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

'''def timer_display(start_time):
	end_time=timeit.default_timer()
	os.system('clear')
	print("Time"+str(end_time-start_time))
	return'''

#Is there no compile here?
#Why is the function being called when i am try to build and run. The parameter code is below na :/ 
os.system('clear')

print("Welcome to the game")
x=input("Enter the number of players ")
playersValue=[x]

flag_music=input("Enter 1 to start the game ")

if(flag_music):
    print ("The music will be played in ")
    '''TO BE ADDED LATER
	for k in range(3,0,-1):
                sys.stdout.write("\r"+"{0}".format(k)+" seconds")
		sys.stdout.flush()
#		print("{0}".format(k)+" seconds","\r")
		sleep(1)
		#sys.stdout.write('\r' + "{}".format(k)+" seconds")
else:
	sys.exit()
'''

tune=["e","d#","e","d#","e","b","d","c","a"]
tuneNew=[]

'''TO BE ADDED LATER
pygame.mixer.init()
pygame.mixer.music.load("Resources/furliseMainTune.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
'''
print("\nNow you have to play this music using the butttons")
print("The player who completes the fastest will win the game")
print("All the best!")
#ADD THE WAIT CODE HERE ALSO AS PUT IN MUSIC TO START SNIPPET
print(x)
for i in range(0,x,1):
    flag_music=1
    k=0
    os.system('clear') #Why isn't it clearing?
    run=1

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
            sys.stdout.write('\rTimer: %.2f' %str(end_time - start_time))
            playersValue.append(str(round(end_time - start_time,2)))
            if(GPIO.input(button1)==0):
#                print ("Button 1 was pressed")
                GPIO.output(LED2,0)
                GPIO.output(LED3,0)
                GPIO.output(LED4,0)
                GPIO.output(LED5,0)
                GPIO.output(LED6,0)
                GPIO.output(LED1,1)
                k=k+1
                sleep(.25)
                pygame.mixer.init()
                pygame.mixer.music.load("Resources/ANote2(9).mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() == True:
                    continue
#		print(tuneNew)
                if(["e", "d#", "e", "d#", "e", "b", "d", "c"]==tuneNew):
                    tuneNew.append("a")
                    run=0
                    print(k)
                else:
                    run=0
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
                k=k+1
                if (["e", "d#", "e", "d#", "e"] == tuneNew):
                    tuneNew.append("b")
		else:
			run=0
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
                k=k+1
                if (["e", "d#", "e", "d#", "e", "b", "d"] == tuneNew):
                    tuneNew.append("c")
		else:
			run=0
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
                k=k+1
                if (["e", "d#", "e", "d#", "e", "b"] == tuneNew):
                    tuneNew.append("d")
		else:
			run=0
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
                k=k+1
                if(["e", "d#", "e"] == tuneNew):
                    tuneNew.append("d#")
                elif (["e"] == tuneNew):
                    tuneNew.append("d#")
                else:
                    run=0
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
                k=k+1
                if([]==tuneNew):
                    tuneNew.append("e")
                elif(["e","d#"]==tuneNew):
                    tuneNew.append("e")
                elif(["e", "d#", "e", "d#"]==tuneNew):
                    tuneNew.append("e")
                else:
                    run=0
			
        #I will have an array. And i will compare a particular element of array
    	#accodingly. If any element doesn't matches then an restart message will
    	#pop up
    		#if(completed on time logic):
    		#if(1):
    		#	print("Congratulation you completed ")
    		#	print("Your time is ")
    		#	print(time)
    	#	else:
    	#		print("BOO")
    	#		print("You failed. Please try again")

    except KeyboardInterrupt:
        GPIO.cleanup()

    #def timer_display():
    #	end_time=timeit.default_timer()
    #	os.system('clear')
    #	print ("Time"+ str(end_time-start_time))
    #	return

if(k!=9):
    print("Sorry you failed")
#	print(k)
else:
    print("Congrats you completed it")

lowest=playersValue[0]
for i in range(0,x,1):
    if(playersValue[i]<lowest):
        lowest=playersValue[i]
        bestplayer=i
print ("Player"+i+1,"Won the game!")

