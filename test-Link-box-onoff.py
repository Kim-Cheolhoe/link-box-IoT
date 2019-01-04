import RPi.GPIO as GPIO
import time

# Link Box 3 Axis robot test servo motor
# 23, 24, 25 PIN TEST
# ONOFFPIN TEST  5, 6, 12, 13

# servoPIN = 24
# servoPIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(int(5),GPIO.OUT)# GPIO Assign mode
GPIO.setup(int(6),GPIO.OUT)# GPIO Assign mode
GPIO.setup(int(12),GPIO.OUT)# GPIO Assign mode
GPIO.setup(int(13),GPIO.OUT)# GPIO Assign mode


while 1:
  ipt=input(" Input port : 5,6,12,13 : ")
  act=input(" on->1 /off->0 : ")
  result=ipt+act
  print(int(result))
  if int(result)==51:
      GPIO.output(5, GPIO.HIGH) # out  
  elif int(result)==50:
      GPIO.output(5, GPIO.LOW) # out
  elif int(result)==61:
      GPIO.output(6, GPIO.HIGH) # out      
  elif int(result)==60:
      GPIO.output(6, GPIO.LOW) # out             
  elif int(result)==121:
      GPIO.output(12, GPIO.HIGH) # out      
  elif int(result)==120:
      GPIO.output(12, GPIO.LOW) # out            
  elif int(result)==131:
      GPIO.output(13, GPIO.HIGH) # out      
  elif int(result)==130:
      GPIO.output(13, GPIO.LOW) # out           
        
  else :
     GPIO.cleanup()
