# Présentation du dépôt

Ce dossier contient le diaporama de la présenation du groupe effectuée
lors de l'AG de l'IREM d'Aix-Marseille qui a eu lieu le mercredi 6 juin 2018.

# Format du diaporama

Le diaporama a été écrit en markdown et est compilé avec pandoc.
Le fichier généré est une page HTML.

# Comment compiler

Il faut installer pandoc (d'une façon ou d'une autre…)

puis lancer la commande :

pandoc -S -s --mathjax -i -t revealjs ./bro_moodle.md -o ./bro_moodle.md.html -V revealjs-url=./../reveal.js -V theme=moon

(oui oui, ça fonctionne chez moi aujourd'hui (28/5/2018))