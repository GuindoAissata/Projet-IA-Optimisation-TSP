# Projet-IA

RAPPORT INTELLIGENCE ARTIFICIELLE :

Traveling Salesman Problem Project

Nous présenterons dans ce rapport le problème du voyageur de commerce. L’objectif de ce projet est de trouver le plus court chemin permettant au voyageur de visiter un ensemble de N villes, en passant une seule fois par chacune d’elles. 

Ainsi, nous allons utiliser l’algorithme génétique afin de résoudre au mieux ce problème. Pour cela, nous allons : 

●	Générer un ensemble de villes placées aléatoirement sur une carte.

●	Utiliser un algorithme génétique pour améliorer progressivement les trajets.

●	Concevoir une interface graphique permettant d’afficher les villes et les solutions générées.

●	Évaluer la qualité des résultats et discuter des performances obtenues.

En effet, l’algorithme génétique s’inspire du processus d’évolution naturelle décrit par Charles Darwin : 

●	Sélection naturelle : on choisira les itinéraires les plus courts 
●	Le croisement : on mélangera 2 itinéraires parents pour créer une nouvelle génération.
●	La mutation : on modifiera légèrement des itinéraires afin d’éviter de rester bloqué sur une solution non optimale.
●	L'évaluation (fitness) : on évaluera la qualité d’un itinéraire en fonction de sa longueur totale.

I.	CRÉATION DE LA POPULATION INITIALE (avec creer_population (villes, taille_population))

La première étape de notre algorithme est la création de la population initiale de solutions aléatoires. Cette population est une liste d’itinéraires (individus), où chaque itinéraire représente une solution possible au problème.

Nous pouvons donc nous demander “ Pourquoi des chemins aléatoires ?”

L’objectif de cette fonction est de trouver le meilleur ordre qui minimise la distance totale parcourue. 
Au début, comme nous ne savons pas quel est le meilleur chemin, on génère plusieurs chemins de façon aléatoire.
Ces chemins sont appelés “individus” et l’ensemble de ces chemins forme “la population”. 
Ainsi, la fonction creer_population prend en entrée la liste des villes et la taille de la population souhaitée. 
Rappelons que plus la taille de la population est grande, plus l’algorithme a de chances de trouver la bonne solution. 
Dans cette fonction, nous remarquons l’utilisation de la fonction random.sample (villes, len(villes)) qui permet de faire une permutation aléatoire sans répétition. 

Cette fonction retourne la liste d’itinéraires aléatoires, ou chaque chemin passe une seule fois par ville, dans un ordre différent. 

Résultat :


II.	EVALUATION DE LA QUALITÉ D’UNE SOLUTION (avec fitness(itinéraire))
Dans un algorithme génétique, la fonction de fitness sert à mesurer la qualité de chaque solution (individu) dans la population.
Pour le problème du voyageur de commerce :
●	Une solution est un chemin qui passe par toutes les villes.

●	Plus le chemin est court, meilleure est la solution.

●	Donc, plus la distance totale est petite, plus la valeur de la fitness doit être grande (car l’algorithme cherche à maximiser la fitness).

Dans le cadre du problème du voyageur de commerce, un bon itinéraire est celui qui minimise la distance totale du trajet. Ainsi, pour transformer cette logique en une valeur à maximiser, on calcule l’inverse de la distance totale parcourue. Plus le trajet est court, plus cette valeur est grande.
L’algorithme utilise cette valeur pour favoriser les meilleurs itinéraires lors de la reproduction des générations futures. Cette stratégie s’inspire de la sélection naturelle : seuls les plus performants ont plus de chances de transmettre leurs caractéristiques.
Ainsi, pour pouvoir créer cette fonction nous allons créer la fonction distance (ville1, ville2) au préalable.
La fonction fitness prendra en entrée l’itinéraire et retournera le rapport 1/ distance_totale de l’itinéraire. 


Résultat :





III.	CRÉATION DE LA FONCTION SÉLECTION (avec selection(population, k) )

Après avoir créé la fonction créer_population et fitness, nous pouvons maintenant créer la fonction sélection qui nous permettra de choisir deux parents pour les faire se reproduire et générer de nouveaux individus (solutions). 
L’objectif de cette fonction est de favoriser les meilleures solutions, c'est-à-dire les chemins qui ont un meilleur fitness, tout en maintenant une diversité génétique dans la population. 

Choix de la méthode de sélection : 

Deux méthodes très utilisées en algorithme génétique ont attiré notre attention : 

●	La sélection par roulette : Il s’agit de sélectionner des individus avec une probabilité proportionnelle à leur fitness. Cela signifie que les individus ayant une faible distance totale auront plus de chances d’être choisis. 
L’avantage de cette méthode est que les meilleures solutions seront choisies mais l'inconvénient est que nous aurons un risque que les mêmes individus soient toujours choisis. 

●	La sélection par tournoi : on choisit au hasard k individus d’une population et nous sélectionnons les meilleures parmi eux. 
L’avantage est que nous aurons des solutions diverses, même les individus moyens     peuvent être choisis. 

Nous avons préféré la deuxième méthode (la sélection par tournoi), car elle élargit le champ des solutions possibles. Cela permet d'éviter de rester bloqué sur les mêmes individus et augmente les chances de se rapprocher d'une solution optimale.

Explication du fonctionnement du code : 

1.	On sélectionne aléatoirement k individus d’une population donnée. 
2.	On applique la fonction de fitness à chacun de ces k individus. 
3.	On retient celui qui a la distance la plus faible. 
4.	On répète deux fois ce processus car nous voulons deux parents. 

Résultat :






IV.	CRÉATION DE LA FONCTION CROISEMENT (avec crossover(parent1, parent2))

La fonction crossover consiste à une création de nouveaux individus à partir des deux parents générés par la fonction sélection en combinant leurs itinéraires. On appelle cela un croisement. 
Ici, nous utiliserons le croisement par ordre (Order Crossover, OX) une méthode très populaire dans l’algorithme génétique. 

Étapes du crossover : 
1.	Création d’une liste vide pour l’enfant.
2.	Choix de deux indices aléatoires pour le croisement (deb et fin).
3.	Copie d’une partie de parent1 dans l’enfant.
4.	Compléter le reste de l’enfant avec les villes de parent2.

Résultat :
 

V.	CRÉATION DE LA FONCTION MUTATION (avec mutation(enfant)) : 
La fonction mutation permet d’introduire une petite modification dans un itinéraire afin de garder une diversité génétique dans la population. Cela évite que l’algorithme stagne sur une même solution mais permet aussi d’explorer de nouveaux chemins et de se rapprocher de la solution optimale. 
Etape de la fonction : 
1.	Copie de l’enfant.
2.	Définir une probabilité de mutation : 
Nous avons vu en cours que chaque élément (ville) d’un individu (itinéraire) peut changer aléatoirement avec une probabilité de mutation, généralement faible (P < 0.05). 
Pour intégrer cette contrainte dans notre algorithme, nous avons utilisé la ligne suivante :  if random.random() < proba_mutation 
Cette instruction pose en réalité la question suivante :
“Est-ce que le tirage aléatoire est inférieur au taux de mutation ?” 
●	Si oui, alors on applique la mutation (par exemple, en échangeant deux villes).
●	Sinon, l’individu reste inchangé.
Cela permet de conserver une diversité génétique minimale dans la population tout en limitant les changements inutiles, ce qui est essentiel pour que l’algorithme progresse de manière efficace.
3.	Vérifier si nous pouvons appliquer la mutation.
4.	Choisir deux villes au hasard. 
5.	Échanger les villes. 
6.	Retour du nouvel individu. 
Résultat :
 
	
VI.	CRÉATION DE LA FONCTION FORMATION (avec formation(population,enfant)) 

Après avoir généré un nouvel individu (enfant) via crossover et éventuellement mutation, il est nécessaire de l’intégrer dans la population. Pour cela, nous avons défini une fonction formation.

Étapes de la fonction : 

●	Ajout de l’enfant :
●	Tri par performance : Nous plaçons les meilleures chemins (les plus courts) en tête de liste.
●	Maintien de la taille constante : pour éviter une croissance indésirable de la population, le dernier individu (le plus long chemin) est retiré. 

Cette fonction permet de faire évoluer la population tout en sélectionnant les chemins les plus intéressants pour le voyageur de commerce. 

Résultat :

 

VII.	CRÉATION DE L’ALGORITHME GÉNÉTIQUE (avec genetique(villes,taille_pop))

La fonction génétique, étant le cœur de l’algorithme, utilise toute les fonctions vues plus haut:
1.	Initialisation : on génère des populations initiales et on identifie le meilleur individu.
2.	Sélection des parents
3.	Crossover
4.	Mutation 
5.	Formation de la nouvelle population 
6.	Vérification d’amélioration

Résultat :


ANNEXE 1:
Code source Python de l'algorithme génétique

from fonctions import creer_population,fitness,selection,crossover,mutation,formation

def genetique(villes,taille_pop):
#principe : on repète tant qu'on améliore , donc si first_best n'a pas pas changé au cours de l'algo on s'arrête sinon tant que ça change on continue
    population = creer_population(villes,taille_pop)
    first_best = max(population, key=fitness)
    while(True):
        #selection des parents 
        parent1,parent2 = selection(population,k=3)

        #recombinaison des parents
        enfant = crossover(parent1,parent2)

        #Mutation de l'enfant
        enfant = mutation(enfant)

        #Formation : ajouter l'enfant à la popultion en mettenant la taille de la population
        population = formation(population,enfant)
        
        #find of the best way
        best = max(population,key = fitness)

        #si la fitness optimal augmente(c-a-d la distance diminue) alors on continu sinon on s'arrête
        if fitness(best) > fitness(first_best) :  
            first_best = best
        else : break #si l'ancine optimal est inférieure au nouveau alors pas d'amélioration on arrête
    return first_best , 1/fitness(first_best)




ANNEXE 2 :
Code source Python des fonctions 

import random
import math


                ############# CREER_POPULATION ##############               
def creer_population(villes, taille_population): #on veut une population initiale d'itinéraires
    population = []
    n = len(villes)  # Nombre total de villes

    for _ in range(taille_population):
        individu = random.sample(villes, n)  # Mélange aléatoire des villes #ransom.sample() assure qu'on ne repète pas de villes 
        population.append(individu)

    return population
  
                #################### FITNESS #############################
def distance (ville1,ville2):
    x1,y1= ville1[:2]
    x2,y2= ville2[:2]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def fitness (itinéraire): #évaluer la qualité de l'itinéraire, plus la distance est grande + fitness petite
                        #itinéraire = individu = un chemin pour lequel on calcule la fitness
    distance_totale = 0 

    for i in range(len(itinéraire)-1):
        distance_totale = distance_totale + distance(itinéraire[i],itinéraire[i+1])

    print(f"distance totale pour {itinéraire} = {distance_totale}")
    return 1/ distance_totale 

                #################### SELECTION ###################
def selection(population,k) :#on lui donnera la population générée en paramètre 
#cette fonction a pour but de séléctionner et retourner 2 meilleurs parents 

#pour la sélection nous avions le choix entre la selction en roulette qui se base sur la probabilité proportionelle à la fitness
#et la seléction en tounoi qui fais un duel entre   k candidats  choisis aléatoirement
#mais la selection par roulette a des riques de stagnation(trop d'élitisme) au cas où 
#on doit faire la selection pour  une population énorme 
#dans notre cas il serait donc optimal d'utiliser la sélection par tournoi , en plus 
#cet algo donne la chance à tout le monde d'être pris parce qu'on choisit aléatoirement k individus et parmis ces k individus on prend le meilleur
#ce meilleur n'est donc pas forcement le meilleur de la population mais le meilleur des k ind , or ces k individus peuvent être les 3 moins bons , on ne sait jamais 

# A noter : une forte fitness = un bon chemin car si fitness forte alors distance petite
#           une faible fitness = un mauvais chemin 

#prinicpe de l'algo : 
#                     1. on choisit aléatoirement  k individus
#                     2. on compare leur fitness
#                     3. on sélectionne le meilleur parmis ce petit groupe
#                     4. on repète ça deux pour obtenir 2 parents 

    #Tirer k individus aléatoiremnent
    c1 = random.sample(population,k)
    c2 = random.sample(population,k) #sample permet de ne pas choisir les mêmes

    #Sélectionner le meilleur parmi les k (c-a-d celui avec la plus petite fitness)
    parent1 = max(c1,key=fitness) # c1 est une liste de k individus , python va appliquer la fonction fitness à chaque individu ensuite choisira celui qui la fitness min 
    parent2=max(c2,key=fitness)

    return parent1,parent2
  
                ############ RECOMBINAISON ###################
def crossover(parent1,parent2):
    #cette fonction nous servira à utiliser les 2 parents retourner par selction
    #pour créer un enfant  , on va utiliser le Cross OX qui est très celèbre
    #pour cela je vais dois couper une partie de parent 1 le placer dans enfant(un new tab vide de taille égale à celle des parents)et 
    #completer le reste de enfant par ce qu'i,l reste dans parent 2 et qu'on a pas utilisé encore dans enfant 
    # exemple : parent1=[1,2,3,4,5] ; parent2=[2,4,3,5,1] => 
    #                                                   1) enfant =[_,2,3,4,_] : on a copié deb=parent1[1] à fin=parent[3] dans enfant exactement dans le même ordre
    #                                                   2) enfant =[1,2,3,4,5] : on a complété l'enfznt avec les éléments de parent2 qui ne sont pas djà dans l'enfant

#on crée un tableau de même taille que parent1

    enfant = [None]*len(parent1)

#choisir deux indices de coupure (comme deb , fin dans l'exemple prece)

    #j'avais pensé à prendre deb=0 et fin=len(parent1)/2 mais cela donnera à chaque appel à la fonction une coupure à la même place 
    #alors que l'optimisation dans les algorithmes génétiques repose sur la diversité des solutions donc si on fixe toujoiurs les indices
    #de coupure de cette manière , cela peut avoir certianes limites
    #donc je vais prendre des deb et fin aléatoires entre len(parent1), ça aurait pu être len(parent2) aussi parce que de toute façon ils ont le même len

    deb =random.randint(0,len(parent1)-1)
    fin = random.randint(0,len(parent1)-1)
    if deb!= fin: #au cas où par exemple deb =4 et fin =2 alors on donnera à deb le plas petite valeur c-a-d deb=2 et à fin la plus grande c-a-d fin =4
        deb=min(deb,fin)
        fin=max(deb,fin)

#Copier dans enfant la sous-séquence de parent1 entre deb et fin 

    enfant[deb:fin+1] = parent1[deb: fin+1]

# Compléter l'enfant que les élements de parent2 qui ne sont pas déjà dans enfant

    current_ind =fin + 1
    
    for ville in parent2:
        if ville not in enfant:
            if current_ind == len(parent1): #si on dépasse la fin, on recommence au début
                current_ind = 0
            enfant[current_ind] = ville 
            current_ind +=1

    return enfant
  
                ############# MUTATION ###################
def mutation(enfant) :
    #il s'agit d'échanger  la postion des villes  pour obtenir un nouveau chemin
    # exemple = [1,2,3,4,5] -> [1,3,2,4,5] => on a échangé les places de 2 et 3 pour obtenir un new individu
    #On a vu dans le cours que chaque élement(chaque ville) des individus(d'un chemin) peut  changer aléatoirement 
    #avec une probabilité P(P<0.005) 
    #On va donc définir une proba_mutaion = 0.05 avec laquelle on ferra le test pour savoir si deux villes pourront chnager d'emplacement
    enfant_mute = enfant[:]
    proba_mutation = 0.5 # j'avais utilisé une proba de 0.05 mais je ne voyais pas de mutaion lors du test donc j'ai mis comme proba 0.1
    if random.random() < proba_mutation :#si une valeur aléatoire choisi entre [0,1] avec 0 et 1 exclu est inferieur à proba_mutation 
#on chsoit 2 indices aléatoirement entre 0 à len(enfant)
        i1 , i2 = random.sample(range(len(enfant)),2) 

#On échnage les villes qui sont à ces deux indices là
        #enfant[i1] , enfant[i2] = enfant[i2], enfant[i1]
        tmp = enfant_mute[i1]
        enfant_mute[i1] = enfant_mute[i2]
        enfant_mute[i2] = tmp
    return enfant_mute

              ############ FORMATION #################
def formation(population,enfant) :
    #Ajout de l'enfant : L'enfant est ajouté à la population.
    #Tri par fitness : On trie la population en fonction de la fitness des individus,
    #  mais en ordre décroissant (reverse=True), c'est-à-dire du meilleur au moins bon.
    #Maintien de la taille de la population : On enlève le moins bon individu (dernière position après tri),
    #  de façon à ce que la taille de la population reste constante.

    # Ajouter l'enfant à la population
    population.append(enfant)

    #Trier la population par fitness décroissante (le meilleur en premier)
    population.sort(key=fitness, reverse=True)

    #Garder la taille de la population constante en enlevant le pire individu
    population = population[:len(population)-1]#conserver la populationn de taille initiale

    return population

















ANNEXE 3 :
Code source Python Main 


import tkinter as tk
from tkinter import ttk
import random
from fonctions import creer_population,fitness,selection,crossover,mutation,formation
from genetique_algo import genetique

villes= []

def generer_villes():
    canvas.delete("all") #reinitialisé la fenetre 
    global villes
    villes= []
    n = int(entry.get())
    for _ in range (n) :
        x,y = random.randint(10,490), random.randint(10,190)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill= "red",tags="ville")

        villes.append((x,y))

    for i in range (len(villes)-1):
        x1,y1 = villes[i]
        x2,y2 = villes [i+1]
        canvas.create_line(x1,y1,x2,y2, fill ="black",width=2,tags="ligne")#liaison entre les villes

def dessiner_villes(villes):#cette fonction sera utilisée dans run_algo pour dessiner les villes et chemins 
    canvas_resultat.delete("all") #reinitialisé la fenetre 
    for i in range (len(villes)-1):
        x1,y1 = villes[i]
        x2,y2 = villes [i+1]
        canvas_resultat.create_oval(x1-5, y1-5, x1+5, y1+5, fill= "red",tags="ligne")
        canvas_resultat.create_line(x1,y1,x2,y2, fill ="black",width=2, tags = "ligne",)#liaison entre les villes
    

    x1, y1 = villes[-1]
    x2, y2 = villes[0]
    canvas_resultat.create_line(x1, y1, x2, y2, fill="red", width=2, tags="ligne")
    canvas_resultat.create_oval(x1-5, y1-5, x1+5, y1+5, fill= "red",tags="ligne")

def run_algo():
    taille_pop = 100
    
    best_way ,best_fit = genetique(villes,taille_pop)
    print(f"le meilleur chemin trouvé est : {best_way} ")
    print(f"la meilleure distance trouvée est : {best_fit} ")
    
    return best_way, best_fit ,dessiner_villes(best_way), label_distance.config(text=f"BEST DIST : {best_fit :.2f}")

# fenetre 
fenetre = tk.Tk()
fenetre.title("Travelling Salesman Problem")
fenetre.geometry("600x700") #largeur x Hauteur

###############"generer les villes"##################
frame_genere_ville = tk.Frame(fenetre , bg ="white" )
frame_genere_ville.pack(side=tk.TOP, fill = tk.BOTH , expand= True)

label1 = tk.Label(frame_genere_ville, text="CITY GENERATION", bg="white", font=("Arial", 14))
label1.pack(pady=10)

#Canva pour afficher les villes générées 
canvas = tk.Canvas(frame_genere_ville,width=500,height=200,bg="white")
canvas.pack()

#################Résultat de l'algorithme###########""
frame_genetic = tk.Frame(fenetre,bg = "white")
frame_genetic.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

label2 = tk.Label(frame_genetic, text="OUTPUT OF THE ALGORITHME", bg="white", font=("Arial", 14))
label2.pack(pady=10)

#Canvas pour afficher le résultat de l'algorithme
canvas_resultat = tk.Canvas(frame_genetic, width=500, height=200, bg="white")
canvas_resultat.pack()

####################les boutons##################""
#frame_boutton = tk.Frame(fenetre,bg="white")
#frame_boutton.pack(side=tk.RIGHT, fill = tk.Y)

#label3 = tk.Label(frame_boutton, text="Contrôles", bg="#f0f0f0", font=("Arial", 14))
#label3.pack(pady=10)

entry = tk.Entry(frame_genere_ville) #utilisateur peut entrer une valeur 
entry.pack()

#Boutons

bouton1= tk.Button(frame_genere_ville, text = "generate cities", command = generer_villes)
bouton1.pack(pady=5)

bouton2 = tk.Button(frame_genetic,text="Run the genetic algorithme", command=run_algo)
bouton2.pack(pady=5)

label_distance = tk.Label(frame_genetic,text="BEST DISTANCE : ")
label_distance.pack()

# Lancer l'application
fenetre.mainloop()



ANNEXE 4 : 
INTERFACE GRAPHIQUE 



