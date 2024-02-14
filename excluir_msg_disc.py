import pyautogui
from time import sleep

x = int(input('Digite o numero de mensagens para apagar: '))
for i in range(0, x):
    pyautogui.click(x=1335, y=847)
    sleep(0.8)
    pyautogui.click(x=1335, y=847)
    pyautogui.click(x=1100, y=965)
    sleep(0.6)
    pyautogui.click(x=1171, y=703)
    sleep(0.5)
