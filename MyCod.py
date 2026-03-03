import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

# 1 abrir o navegador

pyautogui.press('win')
pyautogui.write("edge")
pyautogui.press("enter")

time.sleep(2)

# 2 acessar a pagina
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)
# 3 fazer o login

pyautogui.click(x=598, y=542)
pyautogui.write("Login@user.com.br")
pyautogui.press("tab")
pyautogui.write("SuperSecret123")
pyautogui.press("enter")
# 4 cadstrar o produto
time.sleep(3)

table = pd.read_csv("produtos.csv")
print(table)


for linha in table.index:
    pyautogui.click(x=579, y=361)

    pyautogui.write(str(table.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write("marca")
    pyautogui.press("tab")

    pyautogui.write("tipo")
    pyautogui.press("tab")

    pyautogui.write("Categoria")
    pyautogui.press("tab")

    pyautogui.write("preco")
    pyautogui.press("tab")

    pyautogui.write("Custo")
    pyautogui.press("tab")

    pyautogui.write("obs")
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(+5000)




