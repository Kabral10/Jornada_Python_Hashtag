import pyautogui
import time

pyautogui.PAUSE = 0.3

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
import pandas

tabela = pandas.read_csv('produtos.csv')
print(tabela)

#Passo 4: Cadastrar 1ª produto
#    pyautogui.click(x=678, y=290)
#
#    codigo = 'MOLO000251'
#    pyautogui.write(codigo)
#    time.sleep(0.3)
#    pyautogui.press('tab')
#
#    marca = 'Logitech'
#    pyautogui.write(marca)
#   time.sleep(0.3)
#    pyautogui.press('tab')
#
#
#    tipo = 'Mouse'
#    pyautogui.write(tipo)
#   time.sleep(0.3)
#    pyautogui.press('tab')
#
#
#    categoria = '1'
#    pyautogui.write(categoria)
#    time.sleep(0.3)
#    pyautogui.press('tab')
#
#
#    preco_unitario = '25.95'
#    pyautogui.write(preco_unitario)
#    time.sleep(0.3)
#    pyautogui.press('tab')
#
#
#    custo = '6.50'
#    pyautogui.write(custo)
#    time.sleep(0.3)
#    pyautogui.press('tab')
#
#
#    obs = ''
#    pyautogui.write(obs)
#    time.sleep(0.3)
#
#    pyautogui.press('tab')
#    pyautogui.press('enter')
#    pyautogui.scroll(10000)
#
#Passo 5: Repetir para os proximos
for linha in tabela.index:
    pyautogui.click(x=678, y=290)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    pyautogui.write(obs)
    time.sleep(0.1)



    pyautogui.press('enter')
    pyautogui.scroll(10000)