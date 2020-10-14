import time
import datetime
from pygame import mixer
a = 1200  # time is written in seconds
b = float(2700)  # time is written in seconds
c = 30  # time is written in seconds

# def gettime():
#     a =
#     print(a)

Time_for_water = time.time()
Time_for_rubbingeyes = time.time()
time_for_exercise = time.time()
while True:
    verification = input("Are u also a coder, if yes then type yes otherwise no\n")
    if verification == "yes":
        print("Then you also would be just sitting like me, so that's why I made this program to help us\n It will help you keep you fit!\n so let's begin")
        time.sleep(3)
    elif verification == "no":
        print("That's fine I made this program for both coders and other peoples.")
        time.sleep(3)
    else:
        print('Invalid input!')
        exit()
    
    i2 = input(
        "Please enter:\na to activate this program\nc to check you progress\ncl to close the program\n--> ")

    

    if i2 == "a":
        currenttime = time.strftime("%H:%M:%S")
        print("So this is the time right now: ", currenttime)
        while 1:
            if time.time() - Time_for_water > a:
                mixer.init()
                mixer.music.load("Water.mp3")
                mixer.music.play()
                i = input("If you have drunk please enter[done]\n--> ")
                if i == "done":
                    mixer.music.stop()
                    with open('Water_drinking_record.txt', 'a') as x:
                        x.write(time.strftime('%A %B %d %I:%M:%S %Y\n'))
                        time.sleep(1)
                        print('Your record has been saved successfully!')
                        x.close()
            if time.time() - Time_for_rubbingeyes  > b:
                mixer.init()
                mixer.music.load('eyes.mp3') # Here you have to enter the audio path
                mixer.music.play()
                inpu1 = input('If you have done your eyes exercise please enter[done]\n--> ')
                if inpu1 == 'done':
                    mixer.music.stop()
                    file = open('eyes_exercise_record.txt','a')
                    file.write(time.strftime('%A %B %d %I:%M:%S %Y\n'))
                    time.sleep(1)
                    print('Your record has been saved successfullly!')
                    file.close()
                    
            if time.time() - time_for_exercise > c:
                mixer.init()
                mixer.music.load('physical.mp3')
                mixer.music.play()
                inpu3 = input('If you have done your physical exercise please enter [done]\n--> ')
                if inpu3 == 'done':
                    mixer.music.stop()
                    with open('Physical_exercise_record.txt','a') as b:
                        b.write(time.strftime('%A %B %d %I:%M:%S %Y\n'))
                        time.sleep(1)
                        print('Your record has been saved successfully!')
                        b.close()
                        break
    elif i2 == "c":
        inpu = input(
            'Please tell for what you want to check the record: w for water, e for eyes and ph for physical exercise\n --> ')
        if inpu == 'w':
            with open('Water_drinking_record.txt') as y:
                print(y.read())
                y.close()
        elif inpu == 'e':
            file =  open('eyes_exercise_record.txt')
            print(file.read())
            file.close()
        elif inpu == 'ph':
            file = open('Physical_exercise_record.txt')
            print(file.read())
            file.close()
        else:
            print('Input Error!')

    elif i2 == 'cl':
        quit()


    ipm = input('Do you want to run this programm again? Enter y for yes and n for no\n--> ')
    if ipm == 'y':
        continue
    else:
        quit()
    

