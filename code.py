import pyautogui
pyautogui.FAILSAFE = False   #to use the mouse to close the program when the cursor at any corner of screen but you make it false as you need to move the cursor
while True:
  time.sleep(15)    #after seconds it will move from the right corner up to down
  for i in range(0 , 100):
    pyautogui.moveTo(0, i*5)     #move per pixels
  for i in range(0,3):
    pyautogui.press('shift')  #after it finishes the movement the computer will press shift 3 times to still active

