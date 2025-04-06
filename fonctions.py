import random
import math



                ##############CREER_POPULATION################


                
def creer_population(villes, taille_population): #on veut une population initiale d'itinéraires
    population = []
    n = len(villes)  # Nombre total de villes

    for _ in range(taille_population):
        individu = random.sample(villes, n)  # Mélange aléatoire des villes #ransom.sample() assure qu'on ne repète pas de villes 
        population.append(individu)

    return population
        

                ######################FITNESS################################

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



                #####################SELECTION#####################

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


                #############CROSS_OVER####################

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

                ##############MUTATION####################

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

#############FORMATION##################
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
