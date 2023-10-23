import pyautogui
import time

while True:
    RankButton = "C:\\Users\\shree\\OneDrive\\Desktop\\Python\\Projects\\PAL Autoranker\\RankButton.png"
    VeryIntButton = "C:\\Users\\shree\\OneDrive\\Desktop\\Python\\Projects\\PAL Autoranker\\VeryInterestedButton.png"
    SaveButton = "C:\\Users\\shree\\OneDrive\\Desktop\\Python\\Projects\\PAL Autoranker\\SaveButton.png"

    time.sleep(3)
    while True:
        try:
            pyautogui.press("end")
            pyautogui.click(RankButton)
            break
        except:
            continue
    time.sleep(3)
    while True:
        try:
            pyautogui.press("end")
            break
        except:
            continue
    while True:
        try:
            pyautogui.click(VeryIntButton)
            break
        except:
            continue
    while True:
        try:
            pyautogui.click(SaveButton)
            break
        except:
            continue

    time.sleep(1)
    pyautogui.press("end")