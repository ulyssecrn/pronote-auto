import time
from datetime import datetime
from playsound import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from settings import *


def load_wait_by_xpath(element_xpath):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    except TimeoutException:
        print("Loading took too much time!")


if user != '' and pwd != '':
    while datetime.now().time().minute != minute or datetime.now().time().hour != hour:
        print('Waiting for the right time.', end="\r", flush=True)
        time.sleep(1)

    driver = webdriver.Chrome()
    driver.get('https://0782562l.index-education.net/pronote/eleve.html?login=true&fd=1')
    load_wait_by_xpath('//*[@title="Saisissez votre identifiant."]')
    driver.find_element_by_xpath('//*[@title="Saisissez votre identifiant."]').send_keys(user)
    driver.find_element_by_xpath('//*[@title="Saisissez votre mot de passe."]').send_keys(pwd)
    driver.find_element_by_xpath('//*[contains(text(), "Se connecter")]').click()
    load_wait_by_xpath('//*[@id="GInterface.Instances[1]_colonne_2"]')
    success = False
    attempts = 1
    while attempts < 8:
        driver.refresh()
        load_wait_by_xpath('//*[@id="GInterface.Instances[1]_colonne_2"]')
        try:
            idevoir = driver.find_element_by_xpath(
                "//*[contains(text(),'Appel')]//preceding-sibling::div[contains(text("
                "),'PHYSIQUE-CHIMIE > TP/TD')]")
        except NoSuchElementException:
            print("iDevoir not found ! Attempt number " + str(attempts) + ".")
            for i in range(0, 120):
                print("Trying again in " + str(120 - i) + " seconds...", end="\r", flush=True)
                time.sleep(1)
            attempts += 1
        else:
            print("iDevoir found !")
            attempts = 8
            idevoir.click()
            start = "//*[contains(@id, 'boutonStart')]"
            load_wait_by_xpath(start)
            driver.find_element_by_xpath(start).click()
            load_wait_by_xpath("//*[contains(text(), 'Question 1')]")
            try:
                title = driver.find_element_by_xpath("//*[contains(text(), 'Présent ?')]")
            except NoSuchElementException:
                print('iDevoir is different !!!')
            else:
                success = True
                driver.find_element_by_xpath("//*[contains(text(), 'oui')]").click()
                time.sleep(0.5)  # find an xpath to wait for instead
                driver.find_element_by_xpath("//*[contains(text(), 'Valider')]").click()
                time.sleep(0.5)  # same problem
                driver.execute_script("GInterface.Instances[1].Instances[0].Instances[0]."
                                      "objetVisuEleve.surEvenement({action: 'submit'});")  # find a button to click
                driver.close()
                print("iDevoir successfully filled !")
    while not success:
        print("ERROR")
else:
    print("Add your username and password to settings.py first !")
