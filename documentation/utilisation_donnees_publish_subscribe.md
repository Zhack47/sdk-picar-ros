# ROS Topics: Utilisation des données de publish subscribe

## Speed 

La valeur speed varie entre 0 et 100 avec un pas de 10.   
La voiture en tête envoie la valeur de sa vitesse s'il y a un changement de celle-ci (déccélération ou accélération).  Les autres voitures vont receptionner la nouvelle valeur afin de se caler à la même vitesse que la première voiture.   

## Rotate

La valeur rotate est un angle qui varie entre -50 et 50 (à vérifier)
La voiture en tête envoie la valeur de l'angle de sa rotation. Les autres voitures vont receptionner les informations pour tourner à la même position que la première voiture (prévoir le calcul de distance)


## Ultrason (pas utilisé pour cette version du projet)

Les capteurs ultrasons  envoient des données en continue. Ces données sont des distances entre l'objet détecté (dans notre cas la voiture précédente) devant et la voiture.  Cela nous permettra de calibrer la trajectoire de la voiture tout en stabilisant l'écart entre les 2 voitures.  
