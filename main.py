# imports
import pyautogui
from tkinter import *
import pyttsx3
import datetime
import time
import subprocess
import webbrowser
import random
import os
import winsound
import psutil


# battery info
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
plugged = "Plugged In" if plugged else "Not Plugged In"



# variables
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


# speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# wish when started
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!")
    else:
        speak("GOod Evening Sir!")


# runnnig commands
def submission():
    com = c.get('1.0', 'end-1c')
    y = ['Starting', 'Firing Up', 'Launching', 'Opening']
    z = random.choice(y)

    command_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'shutdown now', 'shutdown', 'restart', 'logout', 'log out', 'sleep', 'start spotify', 'start edge', 'start edge last tabs', 'start edge taskman', 'start chrome', 'start firefox', 'start chrome last tabs', 'start chrome taskman', 'start firefox taskman', 'start firefox last tabs', 'start calculator', 'start winsearch', 'start winactioncenter', 'start settings', 'start cortana', 'start AI', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    x = 10
    print(com)
    if com == 'shutdown':
        speak("Laptop will shutdown in some time")
        subprocess.run(['shutdown', '-s'], shell=True)
    elif com == 'shutdown now':
        speak("Shutting down")
        subprocess.run(['shutdown', '-s', '-t', '00'], shell=True)
    elif com == 'sleep':
        print("Going to sleep")
        subprocess.run(['rundll32.exe', 'powrprof.dll,', 'SetSuspendState', 'Sleep'], shell=True)
    elif com == 'restart':
        speak("Restart initiated")
        subprocess.run(['shutdown', '-r'])
    elif com == 'logout':
        speak("Logging outtt.....")
        subprocess.run(['shutdown', '-l'], shell=True)
    elif com == 'start spotify':
        speak(z + 'Spotify')
         
        os.system('start spotify')
    elif com == 'start edge':
        speak(z + 'Microsoft Edge') 
         
        subprocess.run(['start', 'msedge'], shell=True)
    elif com == 'battery':
        speak("The battery is " + str(percent) + "%")
        if percent == 30 or percent != 30:
            speak("I suggest to charge the device")
    elif com == 'start edge taskman':
        speak(z + "Microsoft Edge with Browser Task Manager")
        subprocess.run(['start', 'msedge'], shell=True)
        time.sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.press('esc')
        pyautogui.keyUp('shift')
    elif com == 'start chrome':
        speak(z + "Google Chrome")
        
        subprocess.run(['chrome'], shell=True)
    elif com == 'start chrome taskman':
        speak(z + "Google Chrome with Task Manager")
        subprocess.run(['chrome'], shell=True)
        time.sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.press('esc')
        pyautogui.keyUp('shift')
    elif com == 'start firefox':
        speak(z + " Firefox")
        
        subprocess.run(['start', 'firefox'], shell=True)
    elif com == 'start firefox taskman':
        speak(z + "Fire fox with task manager")
        subprocess.run(['start', 'firefox'])
        time.sleep(5)
        pyautogui.keyDown('shift')
        pyautogui.press('esc')
        pyautogui.keyUp('shift')
    elif com == 'start edge last tabs':
        speak(z + 'Last tab in Edge')
         
        subprocess.run(['start', 'msedge'], shell=True)
        time.sleep(3)
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('shift')
        pyautogui.typewrite('t')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
    elif com == 'start calc' or com == 'start calculator':
        speak(z + 'Calculator')

        subprocess.run(['start', 'calc'], shell=True)
    elif com == 'start winsearch':
        speak(z + 'Windows Search')
        
        pyautogui.keyDown('win')
        pyautogui.typewrite('s')
        pyautogui.keyUp('win')
    elif com == 'start winactioncenter':
        pyautogui.keyDown('win')
        pyautogui.typewrite('a')
        pyautogui.keyUp('win')
    elif com  == 'settings':
        pyautogui.keyDown('win')
        pyautogui.typewrite('i')
        pyautogui.keyUp('win')
    elif com == 'what time':
        t1 = datetime.datetime.now().hour
        t2 = datetime.datetime.now().minute
        if t1 > 12:
            t1 -= 12
        engine.say('The time is '+ str(t1))
        engine.say(str(t2))
     
    elif com == 'what date':
        global d
        d = datetime.datetime.now().day
        m =datetime.datetime.now().month
        y = datetime.datetime.now().year
        engine.say('Today is ' + str(d))
        engine.say(str(m))
        engine.say(str(y))
        
    elif com == 'what day':
        d = datetime.datetime.now().strftime('%A')
        engine.say("Today is " + str(d))
         
    elif com == "start AI" or com == 'start cortana':
        engine.say(z + 'cortana')
        
        pyautogui.keyDown('win')
        pyautogui.typewrite('c')
        pyautogui.keyUp('win')
    elif com == 'exit()':
        exiting()
    elif com[0] == 'n' and com[1] == 'o':
        engine.say('Command Not Allowed')
    elif "https://" in com or "http://" in com or "www" in com or ".com" in com:
        speak("Redirecting to URL in browser")
         
        webbrowser.open_new_tab(com)
    elif com not in command_list:
        os.system('start msedge')
        time.sleep(3)
        pyautogui.typewrite(str(com))
        pyautogui.press('enter')

    if percent == 30 or percent <= 30:
        speak("Battery low")
        speak("Charge the device to get non-stop expirience now")
        

# exit application
def exiting():
    speak("Bye Sir, Have a good day")
    root.destroy()


# root and attributes
root = Tk()
root.title("Commanding Center for Windows 10")
root.iconbitmap('./terminal.ico')


# show list of commands that user can use in future
def show_list():
    speak("As you wish sir, Opening list of commands")
    subprocess.run(['open', 'notepad', 'list of commands.txt'])


# tkinter layout
l = Label(root, text="This is a command center for Windows 10 \n operating system, Click on 'Run Command' to execute your command")
l.grid(column=0, row=0)
c = Text(root)
c.grid(column=0, row=1)
b = Button(root, text="Click to get a \n of Commands", padx=90, command=show_list)
b.grid(column=0, row=2)
b1 = Button(root, text="Run Commands", bg="green", command=submission, padx=75)
b1.grid(column=0, row=3)
b2 = Button(root, text="Exit Command Center", padx=40, bg='red', command=exiting)
b2.grid(column=0, row=4)


if __name__ == '__main__':
    wish()
    root.mainloop()
