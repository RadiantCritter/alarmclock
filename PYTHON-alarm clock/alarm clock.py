#importing all the libraaries needed to make the alarm clock in python
from tkinter import *
import datetime
import time
import winsound

#will now define a function for alarm timer
def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print(now)
        if now == set_alarm_time:
            print("Time to wake up")
            winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)
            break


#will now define a function for actual time
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock=Tk()
clock.title("Alarm Clock")
clock.geometry("400x200")
timeformat=Label(clock,text="Enter time in 24 Hour format!", fg="red", bg="black", font="Arial").place(x=60, y=150)
addTime=Label(clock,text="Hour    Min     Sec", font=60).place(x=180)
addYourAlarm=Label(clock,text="When to wake up", fg="pink",  relief="solid", font=("Arial", 15,"bold")).place(x=0, y=29)

#lets set some of the variables required
hour=StringVar()
min=StringVar()
sec=StringVar() 


#Rime required to set the alarm clock
hourTime=Entry(clock, textvariable=hour,bg="green", width=15, font="Arial").place(x=180, y=30)
minTime=Entry(clock, textvariable=min,bg="green", width=15, font="Arial").place(x=240, y=30)
hourTime=Entry(clock, textvariable=sec,bg="green", width=15, font="Arial").place(x=290, y=30)

#to make the time input by user
submit=Button(clock,text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=100)


#set the clock on main loop 
clock.mainloop()