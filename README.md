# pronote-auto
## Description
Python script using Selenium to automatically file an iDevoir on Pronote, a web interface used by millions of high-schools in France. In my case, it fills a very simple iDevoir (=i-"assignement" in french) used by a teacher to take the register.

*Version française [ici](https://github.com/ulyssecrn/pronote-auto/blob/master/README_FR.md).*
## Usage
1. You need to have the Selenium and Playsound libraries installed :
```
pip install selenium playsound
```
2. This script uses Safari as a browser by default. You can use any other browser by editing the `driver = webdriver.Safari()` line and using a chosen driver. More info [here](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).
3. Then, edit `credentials.py` and add your username and password to the variables `user` and `pwd`.
4. Run `pronote-auto.py` and profit !

## Misc
`alarm.mp3` credit of Daniel Simion under Attribution 3.0 license.
