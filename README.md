Fonctionnement:

	-"a" pour avancer:
		-le diriger avec la souris
	-"c" pour avancer plus fluidement
		-le diriger avec la souris
	-"w" pour se mettre en mode écrire:
		-"k" pour se baisser pour écrire
		-"k" (deuxième fois) pour remonter
	-"l" pour bouger la patte n°1
		-la diriger avec :
			-flèche haut et bas pour l'axe z
			-la souris pour les axes x et y
	-click gauche souris pour le faire dancer
	-"d" pour le remettre debout
	-"r" pour lui faire faire une rotation
		-flèche gauche et droite pour lui indiquer le sens de rotation
	-"g" pour lui faire basculer son centre de gravité; 
		-le diriger avec la souris
	-"echap" pour quitter

TODO : 
	- faire attention et comprendre le bug qu'il y a parfois dans les dxl_communication.
		De temps en temps le prog se stop car (je crois) un moteur n'a pas reçu d'info, où s'est déconnecté (A VERIFIER)

	- les limites de déplacement d'une seule patte ne sont pas gérer, elle peut aller à des position extremes

	- comprendre les bugs d'initialisations : 
		-des fois il y a un moteur qui refuse de s'initialiser à une position et des fois bug à mort
			pour le remettre normal il faut débrancher l'usb et l'alim et les remettre (ou se déco reco)