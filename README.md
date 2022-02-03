# LOG635-Lab1

## But
Le laboratoire 1 a pour but de s'initier à l'utilisation du cozmo.
Nous allons créer un script Python pour aider cozmo à repérer des balises dans l'espace.
A chaque fois, il devra s'arréter et effectuer une action telle que parler, déplacer un cube, suivre un objet ou reconnaitre un visage.

## Démarrer
Pour tester le code il suffit de faire tourner main.py qui est un fichier exécutable.
Les étapes sont difficiles à faire fonctionner d'une traite. Ne pas hésiter à bouger les objets ou à exécuter le code en plusieurs fois.

## Architecture
L'architecture du code est comme suit :
- le fichier main.py est le chef d'orchestre qui exécute les différentes étapes du parcours de cozmo
- le fichier steps.py décrit les partitions de chaque étape du parcours
- les autres fichier .py tels que utils.py et formes.py sont les actions que peut réaliser cozmo
