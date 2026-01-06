# Projet IA - Traveling Salesman Problem (TSP)/ NP-hard problem - Dans le cadre d'une Licence 3 - Mars-Avril 2025 

Projet réalisé dans le cadre du module ***Intelligence Artificielle**:

L'objectif est de concevoir un agent capable de trouver le  **plus court trajet** ( soluion optimale) permettant de visiter un ensemble de **N villes**, en passant **une seule fois** par chacune d’elles puis retourner à la ville de départ (**problème du voyageur de commerce (TSP)**).Problème **NP-hard**, ce n'est pas toujours simple ni évident de trouver la solution optimale avec un nombre de villes élevé. 

Nous résolvons ce problème avec un **algorithme génétique**, inspiré de l’évolution naturelle (sélection, croisement, mutation), et nous proposons une **interface graphique (Tkinter)** pour visualiser les villes et le meilleur trajet trouvé.

---

## Fonctionnalités

- Génération aléatoire de **N villes** sur une carte (canvas)
- Résolution du TSP par **algorithme génétique**
  - Population initiale aléatoire
  - Fitness basée sur la distance totale
  - Sélection par tournoi
  - Croisement **Order Crossover (OX)**
  - Mutation (échange de deux villes avec une probabilité)
  - Remplacement / formation de génération en gardant la taille constante
- Interface graphique :
  - Affichage des villes générées
  - Affichage du meilleur trajet + distance totale

---

## Technologies

- **Python 3**
- **Tkinter** (interface graphique)
- `random`, `math`

---

## Structure du projet 
├── main.py # Interface graphique + exécution
├── fonctions.py # creer_population, fitness, selection, crossover, mutation, formation
├── genetique_algo.py # fonction genetique()
└── README.md
## Installation & Lancement

### 1) Prérequis
Avoir Python 3 installé.
### 2) Lancer l'interface
Dans le dossier du projet python main.py

## Utilisation
Entrer un nombre de villes N dans le champ de saisie.

Cliquer sur "generate cities" → les villes sont affichées.

Cliquer sur "Run the genetic algorithme"

Le meilleur trajet est dessiné

La meilleure distance est affichée dans l’interface (BEST DIST)

## Explication de l'algorithme génétique 

L’algorithme suit les étapes classiques :

### 1) Population initiale

Création de plusieurs itinéraires aléatoires (permutations des villes) :

chaque itinéraire = un individu

l’ensemble = une population

Fonction : creer_population(villes, taille_population)

### 2) Fitness (qualité d’un itinéraire)

Un itinéraire est bon si sa distance totale est faible.
On maximise donc :

fitness= 1/distance_totale
	​


Fonctions : distance(ville1, ville2) et fitness(itineraire)

### 3) Sélection (tournoi)

On tire k individus au hasard, puis on garde le meilleur (fitness max).
On répète pour obtenir 2 parents.

Fonction : selection(population, k)

### 4) Croisement (Order Crossover - OX)

On copie un segment du parent 1 dans l’enfant,
puis on complète avec les villes du parent 2 dans l’ordre.

Fonction : crossover(parent1, parent2)

### 5) Mutation

Avec une probabilité donnée, on échange deux villes dans l’enfant pour maintenir la diversité.

Fonction : mutation(enfant)

### 6) Formation de la nouvelle population

On ajoute l’enfant, on trie par fitness, puis on retire le pire pour garder une taille constante.

Fonction : formation(population, enfant)

### 7) Boucle génétique

On répète tant que la fitness s’améliore.

Fonction : genetique(villes, taille_pop)

## Résultats attendus

Un chemin initial (villes connectées dans l’ordre de génération)

Puis un chemin optimisé par l’algorithme génétique, affiché dans le canvas résultat

Une distance finale “BEST DIST : XX.XX”

## Auteurs 
- Aissata GUINDO
- Insaf BENALI
## Licence
Projet universitaire




