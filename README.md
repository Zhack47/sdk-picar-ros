# Projet PiCar pour le cours de Systèmes embarqués

**Ce projet est le résultat du travail de l'équipe de Systèmes Embarqués**

Les membres de cette équipe sont :

- BALGA Khalil
- BOURDELEAU Guillaume
- DESQUENNE Bertrand
- GUERRY Émilien
- LEU Héloïse
- MESBAH Zacharia


## Objectifs du projet

Les principaux objectifs du projet sont:
- Développer un SDK permettant de contrôler la voiture (équipe Khalil / Zacharia)

- Développer une architecture permettant aux voitures de se déplacer seules ou en platoon (équipe Bertrand / Héloïse)

- Développer des outils de vision pour la JetRacer (équipe Émilien / Guillaume)

## Environnement du projet

Les voitures sont controlées par une carte Raspberry Pi 4 (ainsi qu'un hat 4WD qui contrôle les roues). Le sytème d'exploitation utilisé est ROS (Robot Operating System), version noetic.

L'objectif d'un point de vue pédagogique étant de nous apprendre à utiliser les différents concepts mis à dispositoin par ROS la communication inter-véhicules se fera via les [ROS topics](utilisation_donnees_publish_subscribe.md)


## Installation

Dans le dossier *catkin_ws/src*:

`git clone https://gitlab.insa-rouen.fr/sem/sdk-picar-ros-full.git`

`cd scripts/sdk_picar_ros`

`sudo python3 setup.py install`

Une erreur due à dpkg pet apparaître, si des installation sonnt en cours en arrière-plan. Si c'est le cas et que le script d'installation quitte avec une erreur, attendez la fin du processus qui utilise dpkg ou tuez-le. Vous devrez ensuite lancer la dernière ligne à nouveau.


#### TODO

Débugger le keyboard_publisher.launch (*compiles but dos not run*)
