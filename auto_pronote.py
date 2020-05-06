import time
from playsound import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from credentials import *


def load_wait_by_xpath(element_xpath):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    except TimeoutException:
        print("Loading took too much time!")


if user != '' and pwd != '':
    # launch browser
    driver = webdriver.Chrome()
    driver.get('https://0782562l.index-education.net/pronote/eleve.html?login=true&fd=1')
    load_wait_by_xpath('//*[@title="Saisissez votre identifiant."]')

    driver.find_element_by_xpath('//*[@title="Saisissez votre identifiant."]').send_keys(user)
    driver.find_element_by_xpath('//*[@title="Saisissez votre mot de passe."]').send_keys(pwd)
    driver.find_element_by_xpath('//*[contains(text(), "Se connecter")]').click()
    load_wait_by_xpath('//*[@id="GInterface.Instances[1]_colonne_2"]')
    success = False
    attempts = 0
    while attempts < 7:
        try:
            idevoir = driver.find_element_by_xpath(
                "//*[contains(text(),'Appel')]//preceding-sibling::div[contains(text("
                "),'PHYSIQUE-CHIMIE > TP/TD')]")
        except NoSuchElementException:
            print("iDevoir not found !")
            attempts += 1
            time.sleep(120)
        else:
            print("iDevoir found !")
            attempts = 8
            idevoir.click()
            start = "//*[contains(@id, 'boutonStart')]"
            load_wait_by_xpath(start)
            driver.find_element_by_xpath(start).click()
            # add a wait by xpath idevoir window
            try:
                title = driver.find_element_by_xpath("//*[contains(text(), 'Présent ?')]")
            except NoSuchElementException:
                print('iDevoir is different !!!')
            else:
                success = True
                driver.find_element_by_xpath("//*[contains(text(), 'oui')]").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[contains(text(), 'Valider')]").click()
                driver.close()
                print("iDevoir successfully filled !")
    while not success:
        playsound('alarm.mp3')
else:
    print("Add your username and password to credentials.py first !")
