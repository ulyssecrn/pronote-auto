# pronote-auto
## Description
Script Python utitlisant Selenium pour automatiquement remplir un iDevoir sur Pronote, une interface web utilisée par des millions de lycées en France. Dans mon cas, il remplit un iDevoir très simple utilisé par un professeur pour faire l'appel.

English version [here](https://github.com/ulyssecrn/pronote-auto).
## Utilisation
1. Il vous faut la librairie Selenium d'installée :
```
pip install selenium
```
2. Il vous faut Google Chrome d'installé, et [chromedriver](https://chromedriver.chromium.org/home). Vous pouvez utiliser n'importe quel autre navigateur en éditant la ligne `driver = webdriver.Chrome()` et en utilisant le driver approprié. Plus d'info [ici](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).
3. Ensuite, éditez `credentials.py` en y ajoutant votre identifiant et votre mot de passes aux variables respectives `user` et `pwd`.
4. Lancez `pronote-auto.py` aet profitez !

## Misc
Ce script est bien évidemment plus pratique si vous le programmez pour qu'il se lance automatiquement à une certaine heure.
