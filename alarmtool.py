from tkinter import *
from time import strftime
from tkinter.filedialog import askopenfilename
from pygame import mixer
from datetime import datetime

mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
mixer.init()

root=Tk()
root.title("Alarm Tool")
root.geometry("400x400")



##background image
canvas = Canvas(root,width=400,height=400)
canvas.grid()

my_image=PhotoImage(file='C:\\Users\\santhu chintu\\Downloads\\bg.png')
canvas.create_image(0,0,anchor=NW,image=my_image)

##home functions


def snoozing_time():
  global s
  root=Tk()
  root.title("Set snooze time")
  root.geometry("300x200")
  root.configure(background='AntiqueWhite1')
  entry=IntVar()
  def sleep():
    global s
    s=entry.get()
    s=int(s)*1000*60
    
    print(s)
    setup()
    root.destroy()
    

  label=Label(root,text="Set Snooze Time:",font=("calibri 20 bold"))
  label.place(relx=0.7,rely=0.2,anchor=NE)
  entry=Spinbox(root, from_ = 00, to = 60,width=6)
  entry.place(relx=0.65,rely=0.45,anchor=NE)
  label2=Label(root,text="minutes",font=("times 15 bold"))
  label2.place(relx=0.9,rely=0.42,anchor=NE)
  button=Button(root,text="Set",font=("calibri 20 bold"),command=sleep)
  button.place(relx=0.6,rely=0.62,anchor=NE)
  
  
  


 
def setup():

  root=Tk()
  root.title("Set Alarm")                                                                                                                                                                     
  root.geometry("1600x1200")
  root.configure(background = 'AntiqueWhite1')
  
  def time():
    
    string = strftime('%I:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time)
    
  upload=''
  
  def browse():
    global upload
    upload = askopenfilename(initialdir="C:/Users/santhu chintu/",filetypes =(("Wav File", "*.wav"),("All Files","*.*")),title = "Choose ringtone.")

  h=IntVar()
  m=IntVar()
  time_zone=IntVar()
  def set_alarm():
      global s
    
      
      global upload
      import time
      
      
      alarm1=h.get()
      alarm2=m.get()
      alarm3=variable.get()
      AlarmTime=str(alarm1)+":"+str(alarm2)+":"+str(0)+str(0)+" "+str(alarm3)
    
      current_time = time.strftime("%I:%M:%S %p")
      print(s)
      print(AlarmTime)
    

      while current_time != AlarmTime:
          
          print("The time is"+current_time)
          current_time=time.strftime("%I:%M:%S %p")
          time.sleep(1)
      if current_time==AlarmTime:
          print("time to wakeup")
          ring()

  def ring():
      
      global upload
      global set_alarm
      root=Tk()
      root.title("Alarm")                                                                                                                                                                     
      root.geometry("400x400")
      root.configure(background = 'AntiqueWhite1')
      if upload:
          
          print("now Alarm Musing Playing")
          noise=mixer.Sound(upload)
          noise.play()
      def stop():
        noise.stop()
        root.destroy()

      def snooze():
        import time
        noise.stop()
        print(s)
        
        if s!=0:
          print(s)
         
          set_alarm.after(s,ring)
          root.destroy()
        if s==0:   
          set_alarm.after(5000,ring)
          root.destroy()
        
        
          
      stop=Button(root,text="stop",font='times 30',command=stop)
      stop.place(relx = 0.75, rely = 0.3, anchor = NE)

      snooze=Button(root,text="snooze",font='times 30',command=snooze)
      snooze.place(relx = 0.77, rely = 0.58, anchor = NE)
  
  
  
        
  lbl = Label(root, font = ('calibri', 40, 'bold'), background = 'black',foreground = 'white')           
  lbl.place(relx=1,rely=0,anchor=NE)
  time()
  alarm=Label(root,text='Set Alarm:',font=('calibri',30,'bold'),foreground='black')
  alarm.place(relx = 0.2, rely = 0.15, anchor = NE)
  
  time1=Label(root,text='Time:',font=('times', 20,'bold'))
  time1.place(relx=0.25,rely=0.25,anchor = NE)

  h = Spinbox(root, from_ = 00, to = 12,width=5) 
  h.place(relx=0.34,rely=0.263,anchor = NE)

  hour=Label(root,text='hr:',font=('times', 20,'bold'))
  hour.place(relx=0.37,rely=0.25,anchor=NE)

  m = Spinbox(root, from_ = 00, to = 60,width=5) 
  m.place(relx=0.456,rely=0.263,anchor = NE)

  minute=Label(root,text='min',font=('times', 20,'bold'))
  minute.place(relx=0.49,rely=0.25,anchor=NE)

  time_period=["AM","PM"]
  variable = StringVar(root)
  variable.set(time_period[0])
  time_zone=OptionMenu(root,variable,*time_period)
  time_zone.place(relx=0.534,rely=0.252,anchor=NE)

  ringtone=Label(root,text='Set Ringtone:',font=('times', 20,'bold'))
  ringtone.place(relx=0.25,rely=0.33,anchor = NE)

  
      


  browsing=Button(root,text='Browse Mp3 file',command=browse)
  browsing.place(relx=0.33,rely=0.336,anchor=NE)
 
  switch=Button(root,text='Set Alarm',bg='white',font='times 25',command=set_alarm)
  switch.place(relx = 0.4, rely = 0.4, anchor = NE) 

s=0
##buttons in the homepage
set_alarm=Button(command=setup,text='Set Alarm',bg='white',activebackground='black',font='times 30')
set_alarm.place(relx = 0.75, rely = 0.3, anchor = NE) 

set_snoozetime=Button(text='Set Snooze',bg='white',activebackground='black',font='times 30',command=snoozing_time)
set_snoozetime.place(relx = 0.77, rely = 0.58, anchor = NE) 

root.mainloop()
