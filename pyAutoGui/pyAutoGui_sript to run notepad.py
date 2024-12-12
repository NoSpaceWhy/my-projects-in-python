import pyautogui
import time

# Open Notepad
pyautogui.hotkey('win', 'r')  # Open Run dialog
time.sleep(1)
pyautogui.typewrite('notepad')
pyautogui.press('enter')
time.sleep(1)

# Type in Notepad
pyautogui.typewrite('Hello, this is automated typing using PyAutoGUI!', interval=0.1)

# Save the file
pyautogui.hotkey('ctrl', 's')  # Ctrl + S for save
time.sleep(1)
pyautogui.typewrite('example.txt')
pyautogui.press('enter')

