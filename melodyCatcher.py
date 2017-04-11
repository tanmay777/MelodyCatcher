from time import time,sleep
import RPi.GPIO as GPIO
import timeit
import os

GPIO.setmode(GPIO.BOARD)
button1=11
button2=12
button3=13
button4=15
button5=16
LED1=31
LED2=32
LED3=33
LED4=35
LED5=36
time=0

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button5,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(LED1,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(LED5,GPIO.OUT)

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

print("Welcome to the Game")
flag_music=input("Enter 1 to start the Game ")
k=0
try: 
	while(1):
		if(flag_music==1):
			#play music code
			print("In this game, you will have to press the exact buttons to produce the tone which was played")
			flag_music=0
			sleep(1)
			start_time=timeit.default_timer()
		
#		timer_display(start_time)
		
		end_time=timeit.default_timer()
		os.system('clear')
		print("Time"+str(end_time-start_time))
	
		if(GPIO.input(button1)==0):
			print ("Button 1 was pressed")
			GPIO.output(LED2,0)
			GPIO.output(LED3,0)
			GPIO.output(LED4,0)
			GPIO.output(LED5,0)
			GPIO.output(LED1,1)
			sleep(.25)
			k=k+1
		if(GPIO.input(button2)==0):
			print ("Button 2 was pressed")
			GPIO.output(LED1,0)
			GPIO.output(LED3,0)
			GPIO.output(LED4,0)
			GPIO.output(LED5,0)
			GPIO.output(LED2,1)
			sleep(.25)
			k=k+1
		if(GPIO.input(button3)==0):
			print ("Button 3 was pressed")
			GPIO.output(LED1,0)
			GPIO.output(LED2,0)
			GPIO.output(LED4,0)
			GPIO.output(LED5,0)
			GPIO.output(LED3,1)
			sleep(.25)
			k=k+1
		if(GPIO.input(button4)==0):
			GPIO.output(LED1,0)
			GPIO.output(LED2,0)
			GPIO.output(LED3,0)
			GPIO.output(LED5,0)
			GPIO.output(LED4,1)
			print ("Button 4 was pressed")
			sleep(.25)
			k=k+1
		if(GPIO.input(button5)==0):
			GPIO.output(LED1,0)
			GPIO.output(LED2,0)
			GPIO.output(LED3,0)
			GPIO.output(LED4,0)
			GPIO.output(LED5,1);
			print ("Button 5 was pressed")
			sleep(.25)
			k=k+1
		if(k==5):
			break
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
	
	
