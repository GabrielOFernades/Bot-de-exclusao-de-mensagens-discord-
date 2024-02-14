import pyautogui
from time import sleep

# position
i = 0
x = int(input('Digite o numero de mensagens para apagar: '))
while i <= x :
    pyautogui.click(x=1335, y=847)
    sleep(0.6)
    pyautogui.click(x=1335, y=847)
    pyautogui.click(x=1100, y=965)
    sleep(0.6)
    pyautogui.click(x=1171, y=703)
    i = i+1