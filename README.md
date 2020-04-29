# pronote-auto
## Description
Python script using Selenium to automatically file an iDevoir on Pronote, a web interface used by millions of high-schools in France. In my case, it fills a very simple iDevoir (=i-"assignement" in french) used by a teacher to take the register.

## Usage
1. You need to have the Selenium library installed :
```
pip install selenium
```
2. You need to have Google Chrome installed, and [chromedriver](https://chromedriver.chromium.org/home). You can use any other browser by editing the `driver = webdriver.Chrome()` line and using a chosen driver. More info [here](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).
3. Then, edit `credentials.py` and add your username and password to the variables `user` and `pwd`
4. Run `pronote-auto.py` and profit !

## Misc
This script becomes useful when you program it to launch automatically at a certain time so you don't have to do anything.
