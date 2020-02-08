try:
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    from pyfirmata import Arduino, util
import time

board = Arduino('COM3')

while True:
    Led_1 = board.digital[13].write(1)
    time.sleep(1.0)
    Led_2 = board.digital[13].write(0)
    time.sleep(1.0)
    
 
   
