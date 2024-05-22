import time
import pyautogui as pg
import cv2
import mss
import mss.tools
from multiprocessing import Process, Queue, Value

def open_webpage():
    # This code is used to open URL in firefox 
    # browser
      
    import webbrowser
      
    # To take the URL as input from the user.
    link = "https://elgoog.im/t-rex/"
      
    # Passing firefox executable path to the
    # Mozilla class.
    firefox = webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
      
    # Using open() function to display the URL.
    firefox.open(link)
    
def find_trex():
    tries = 0
    while tries < 3:
        trex_center = pg.locateCenterOnScreen('trex2.png',grayscale = True, confidence=0.4)  # returns center x and y
        if trex_center is None:
            tries += 1
            time.sleep(3)
        else:
            return trex_center
    
    return None

def get_pixels(queue: Queue, stop: bool) -> None:
    rect = {"left": 500, "top": 400, "width": 150, "height": 150}
    with mss.mss() as sct:
        while True:
            queue.put(sct.grab(rect))
            
            if stop.value == 1:
                break

    queue.put(None)

def check_pixels(queue: Queue, jump: bool) -> None:
    while True:
        img = queue.get()
        if img is None:
            break
            
        if img.pixel(25, 10)[0] < 100:
            jump.value = 1
            
if __name__ == "__main__":
    open_webpage()
    time.sleep(5)   #wait for webpage to load
    
    trex_center = find_trex()
    
    if trex_center is None:
        print("dinosaur not found")
        quit()

    # Start game
    pg.press('space')    
    
    queue: Queue = Queue()
    
    stop = Value('i', 0)
    jump = Value('i', 0)
    
    p1 = Process(target=get_pixels,   args=(queue, stop))
    p2 = Process(target=check_pixels, args=(queue, jump))
    
    p1.start()
    p2.start()
            
    while True:
        with mss.mss() as sct:
            # Take a screenshot of a region out of monitor bounds
            rect2 = {"left": 675, "top": 350, "width": 50, "height": 50}
            try:
                pix = sct.grab(rect2)
            except ScreenShotError:
                details = sct.get_error_details()
                
            if pix.pixel(17, 16)[0] < 100:
                stop.value = 1
                queue.put(None)
                break

            if jump.value == 1:
                jump.value = 0
                pg.press('space')
    
    p1.terminate()
    p2.terminate()