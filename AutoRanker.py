import pyautogui
import time

RankButton = "C:\\Users\\shree\\OneDrive\\Desktop\\Python\\Projects\\PAL Autoranker\\RankButton.png"
VeryIntButton = "C:\\Users\\shree\\OneDrive\\Desktop\\Python\\Projects\\PAL Autoranker\\VeryInterestedButton.png"
SaveButton = "C:\\Users\\shree\\OneDrive\\Desktop\\Python\\Projects\\PAL Autoranker\\SaveButton.png"

time.sleep(1)
pyautogui.click(RankButton)

time.sleep(3)
pyautogui.press("end")

pyautogui.click(VeryIntButton)
pyautogui.click(SaveButton)

pyautogui.press("end")