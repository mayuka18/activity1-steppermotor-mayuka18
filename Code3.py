from machine import Pin
import time
in1 = Pin(14, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(27, Pin.OUT)
list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
sec = 0.005


while True :
    
    for r in range(0,500) :
      for r in list :
          in1.value(r[0])
          
          in2.value(r[1])
          
          in3.value(r[2])
          
          in4.value(r[3])
          
          time.sleep(sec)
        
      

    for r in range(0,500) :
      for r in reversed(list) :
          in1.value(r[0])
          
          in2.value(r[1])
          
          in3.value(r[2])
          
          in4.value(r[3])
          
          time.sleep(sec)
        
      
      
        
        
        
        
        
        







