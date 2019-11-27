import config
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time
import requests
import re
import sys

#if len(sys.argv) < 3:
#    print("argumentos arg1 = posicion en la lista de nodos, arg2 = id en base de datos")
#    sys.exit()

start_time = time.time()

for nodo, idx in zip(config.nodos, config.ids):
    print(nodo, idx)
    #medimos cuanto tiempo toma el scraping
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    #driver = webdriver.Chrome(config.driver,chrome_options=options)
    driver = webdriver.Chrome(config.driver)
    driver.get(config.url)

    ######################### INICIO DE LOGIN #########################
    # esperamos al elemento
    wait = WebDriverWait(driver, 90)
    username = wait.until(ec.visibility_of_element_located((By.NAME, "username")))
    # con esto ya cargo el elemento
    username.send_keys(config.user)

    #encontramos el elemento password y enviamos la clave
    password_box = driver.find_element_by_id('password')
    password_box.send_keys(config.password)

    #apretamos en el css
    driver.find_element_by_css_selector(".button").click()
    ############################ FIN DE LOGIN #########################
    end_time = time.time()
    print("Total ejecucion de login: {}".format(end_time - start_time))

    ################ SE SELECCIONA EL NODO ##############################
    #xpath = "/html/body/div[2]/div/div[2]/div/ng-include/div/div/fielset/ul/li[{}]/form/div[3]/input".format(sys.argv[1])
    xpath = "/html/body/div[2]/div/div[2]/div/ng-include/div/div/fielset/ul/li[{}]/form/div[3]/input".format(nodo)
    seleccion = wait.until(ec.visibility_of_element_located((By.XPATH, xpath))).click()

    end_time = time.time()
    print("Total ejecucion de seleccionar el nodo: {}".format(end_time - start_time))

    xpath = "//*[@id='container']/div/div[2]/div[2]/p/span[1]"
    pacientes_espera = wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))

    numero = re.search('\(([^)]+)', pacientes_espera.text).group(1)
    print("Pacientes en espera: "+numero)
    driver.close()

    #r = requests.post(config.webservice, data={'establishment_id': sys.argv[2], 'waiting': numero})
    r = requests.post(config.webservice, data={'establishment_id': idx, 'waiting': numero})
    print(r.status_code, r.reason)

# medimos cuanto finaliza el scraping
end_time = time.time()
print("Total ejecucion del webscraping: {}".format(end_time - start_time))
