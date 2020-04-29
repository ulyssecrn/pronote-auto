# pronote-auto
## Description
Script Python utitilisant Selenium pour automatiquement remplir un iDevoir sur Pronote, une interface web utilisée par des millions de lycées en France. Dans mon cas, il remplit un iDevoir très simple utilisé par un professeur pour faire l'appel.

*English version [here](https://github.com/ulyssecrn/pronote-auto).*
## Utilisation
1. Installer la librairie Selenium :
```
pip install selenium
```
2. Ce script utilise Safari comme navigateur par défaut. Vous pouvez utiliser n'importe quel autre navigateur en éditant la ligne `driver = webdriver.Chrome()` et en utilisant le driver approprié. Plus d'info [ici](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).
3. Ensuite, éditer `credentials.py` en y ajoutant votre identifiant et votre mot de passes aux variables respectives `user` et `pwd`.
4. Lancer `pronote-auto.py` et profiter !

## Misc
Ce script est bien évidemment plus pratique si vous le programmez pour qu'il se lance automatiquement à une certaine heure.
