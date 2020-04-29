import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from credentials import *


# wait for page to load function
def load_wait(element_id):
    try:
        myelem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, element_id)))
    except TimeoutException:
        print("Loading took too much time!")


# check whether credentials are filled
if user != '' and pwd != '':
    # launch browser
    driver = webdriver.Safari()
    driver.get('https://0782562l.index-education.net/pronote/eleve.html?login=true&fd=1')
    time.sleep(2)

    # login
    driver.find_element_by_xpath('//*[@title="Saisissez votre identifiant."]').send_keys(user)
    driver.find_element_by_xpath('//*[@title="Saisissez votre mot de passe."]').send_keys(pwd)
    driver.find_element_by_id('id_43').click()
    load_wait("GInterface.Instances[1]_colonne_2")

    # open iDevoir
    driver.execute_script("GInterface.Instances[1].surExecutionQCM (event, 0)")
    load_wait("GInterface.Instances[1].Instances[0].Instances[0].objetVisuEleve")

    # fill iDevoir
    idevoir = "GInterface.Instances[1].Instances[0].Instances[0].objetVisuEleve"
    driver.execute_script(idevoir + ".surEvenement({action: 'start'});")
    time.sleep(2)
    driver.find_element_by_id(idevoir + "_q0_div_r0").click()
    time.sleep(2)
    driver.execute_script(idevoir + ".surEvenement({action: 'submit'});")
    time.sleep(2)
    driver.execute_script(idevoir + ".surEvenement({action: 'submit'});")
else:
    print("Add your username and password to credentials.py first !")
