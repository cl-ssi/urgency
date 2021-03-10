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

start_time_total = time.time()

for nodo, idx in zip(config.nodos, config.ids):
    print(nodo, idx)

    # medimos cuanto tiempo toma el scraping
    start_time = time.time()

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(config.driver,chrome_options=options)
    #driver = webdriver.Chrome(config.driver)
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

    end_time = time.time()
    print("Tiempo de ejecucion de login: {}".format(end_time - start_time))
    ######################## FIN DE LOGIN ###########################


    ################### SE SELECCIONA EL NODO #######################
    #xpath = "/html/body/div[2]/div/div[2]/div/ng-include/div/div/fielset/ul/li[{}]/form/div[3]/input".format(sys.argv[1])
    xpath = "/html/body/div[2]/div/div[2]/div/ng-include/div/div/fielset/ul/li[{}]/form/div[3]/input".format(nodo)
    seleccion = wait.until(ec.visibility_of_element_located((By.XPATH, xpath))).click()

    end_time = time.time()
    print("Tiempo de ejecucion de seleccionar el nodo: {}".format(end_time - start_time))

    xpath = "//*[@id='container']/div/div[2]/div[2]/p/span[1]"
    pacientes_espera = wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))

    numero = re.search('\(([^)]+)', pacientes_espera.text).group(1)
    print("Pacientes en espera: "+numero)

    #xpath = "//*[@id='container']/div/div[1]/dl/dd[2]/a/tab-heading"
    #seleccion = driver.find_element(By.XPATH, xpath).click()
    #seleccion = wait.until(ec.visibility_of_element_located((By.XPATH, xpath))).click()

    #xpath = "//*[@id='container']/div/div/dl/dd[1]/a/tab-heading/span"
    #xpath = "//*[@id='container']/div/div[2]/div[2]/p/span[1]"
    #pacientes_box = driver.find_element(By.XPATH, xpath)
    #print(pacientes_box.text)

    #sys.exit()
    #numero = pacientes_box.text
    #numero = re.search('\(([^)]+)', pacientes_box.text).group(1)
    #print("Pacientes en box: "+numero)

    #driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/dl/dd[2]/a/tab-heading').click()
    #pacientes_en_box = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/p/span[1]')
    #print("En Box  "+pacientes_en_box.text)

    driver.close()

    # Enviar los datos al webservice

    #r = requests.post(config.webservice, data={'establishment_id': sys.argv[2], 'waiting': numero})
    r = requests.post(config.webservice, data={'establishment_id': idx, 'waiting': numero})
    print(r.status_code, r.reason)

# medimos cuanto finaliza el scraping
end_time = time.time()
print("Tiempo total de ejecucion del webscraping: {}".format(end_time - start_time_total))
