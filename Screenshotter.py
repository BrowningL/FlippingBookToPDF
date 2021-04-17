import pyautogui
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
pageNumber = 1

#time to set up browser
time.sleep(15)

#right key function
def press():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

#take screenshot
def screenshot(pageNumber):
    #FirstPage
    myScreenshot = pyautogui.screenshot(region=(315,158, 1303, 1843))
    myScreenshot.save(r'C:\Users\Lukem\Documents\AutomaticTextbook\PageNumber%s.png' % pageNumber)
    #SecondPage
    pageNumber += 1
    myScreenshot = pyautogui.screenshot(region=(1618,158, 1303, 1843))
    myScreenshot.save(r'C:\Users\Lukem\Documents\AutomaticTextbook\PageNumber%s.png' % pageNumber)


#MainLoop
for c in range(155):
    #Take two screenshots of each page
    screenshot(pageNumber)
    pageNumber += 2
    #Change page
    press()
    #wait 1 second
    time.sleep(2)
