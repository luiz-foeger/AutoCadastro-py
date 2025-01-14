import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(0.5)

pyautogui.click(x=850, y=550)
pyautogui.write("meuemail")
pyautogui.press("tab")
pyautogui.write("KMKO23MO3MEM2KOMDI2I3JDOI2DO32DI2MI")
pyautogui.press("enter")

pyautogui.hotkey("fn", "f11")

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(0.5)
pyautogui.PAUSE = 0.1

for linha in tabela.index:
    
    pyautogui.click(x=930, y=280)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
            
    pyautogui.press("enter")
    pyautogui.scroll(10000)