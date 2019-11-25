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

#medimos cuanto tiempo toma el scraping
start_time = time.time()
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(config.driver,chrome_options=options)
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

##########################SE SELECCIONA EL REYNO##############################
#reyno_seleccion = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".button"))).click()
#reyno_seleccion.click()
reyno_seleccion = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/ng-include/div/div/fielset/ul/li[1]/form/div[3]/input"))).click()


#pacientes_espera = driver.find_element_by_css_selector(".upper-right-badge")
end_time = time.time()
print("Total ejecucion de seleccionar el reyno: {}".format(end_time - start_time))

pacientes_espera_reyno = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='container']/div/div[2]/div[2]/p/span[1]")))
print("Hospital Reyno  "+pacientes_espera_reyno.text)
driver.close()
end_time = time.time()
print("Total ejecucion del scrap al Hector Reyno: {}".format(end_time - start_time))
# medimos cuanto finaliza el scraping

#print(username)
numero = int (re.search('\(([^)]+)', numero).group(1))
r = requests.post("http://35.238.154.89/api/waiting_list", data={'establishment_id': 7, 'waiting': numero})
print(r.status_code, r.reason)
