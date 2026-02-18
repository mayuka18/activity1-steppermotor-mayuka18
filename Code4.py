from machine import Pin
import time
pb1 = Pin(18, Pin.IN, Pin.PULL_UP)
pb2 = Pin(22, Pin.IN, Pin.PULL_UP)
in1 = Pin(14, Pin.OUT)
in2 = Pin(25, Pin.OUT)
in3 = Pin(26, Pin.OUT)
in4 = Pin(27, Pin.OUT)
list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
sec = 0.005


while True :
    pb1v = pb1.value()
    pb2v = pb2.value()

    if pb1v ==  0 and pb2v == 1 :
        
        for r in range(0,500) :
            
                            
            for r in list :
                
                    
                in1.value(r[0])

                in2.value(r[1])

                in3.value(r[2])

                in4.value(r[3])

                time.sleep(sec)

    if pb1v ==  1 and pb2v == 0 :
        
         
        for r in range(0,500) :
            
              
            for r in reversed(list) :
                
                  
                in1.value(r[0])
                
                in2.value(r[1])
                
                in3.value(r[2])
                
                in4.value(r[3])
                
                time.sleep(sec)
              
              
              
        
        
        
        
        
        









