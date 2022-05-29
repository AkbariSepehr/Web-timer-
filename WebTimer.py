

import webbrowser
import time 
  

link = input("what link do you want to open? ")

alarm = input("When do you want to set the time? ") 
  

Current_time = time.strftime("%H:%M:%S") 
  


while (Current_time == alarm): 
    print ("WEBSITE IS OPENING")
    Current_time = time.strftime("%H:%M:%S") 
    webbrowser.open(link)
