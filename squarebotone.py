import gpiozero  # GPIO Zero library
import time  # Time library

robot = gpiozero.Robot(left=(22,27), right=(17,18))
 
# Repeat this loop three times.
# Robot will make three boxes.
for i in range(3):
  robot.forward() # Move forward for
  time.sleep(1.0) # 1 second
  robot.right()   # Move right for 
  time.sleep(0.4) # 0.4 second
  robot.forward() # Move forward for
  time.sleep(1.0) # 1 second
  robot.right()   # Move right for
  time.sleep(0.4) # 0.4 second
  print("Box completed") # Box completed
  print("Created by Robotic Insomnia Co.")