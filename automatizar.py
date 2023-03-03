#passos para visualizar a página de esportes 

#1-clicar no google chrome *

#2-clicar na barra de pesquisa *

#3-digitar o site desejado*

#4-buscar*

#5-buscar dentro do site de noticias na barra de pesquisa*

#6-digitar esportes*

#7-pesquisar esportes
import pyautogui
from time import sleep

pyautogui.click(503,750,duration=3)
pyautogui.click(504,418,duration=3)
pyautogui.write('https://g1.globo.com/')
pyautogui.click(504,418,duration=3)
pyautogui.press('enter')
pyautogui.click(1221,178,duration=11)
pyautogui.write('baskete')
pyautogui.press('enter')
