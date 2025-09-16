import pyautogui
import time

pyautogui.PAUSE = 0.6

#Passo 1: Entrar no sistema da empresa
#abrir o google
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

time.sleep(1)

#entrar no site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(1)

#Passo 2: Fazer login
pyautogui.click(x=676, y=407)
pyautogui.write('luizsmitemiguel@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')

#Passo 3: Importar os dados

#Passo 4: Cadastrar 1ª produto
#Passo 5: Repetir para os proximos