# SUJET: Régression linéaire pour la prédiction du prix des voitures

## Objectif
Ce projet est une introduction aux concepts de base du machine learning. L'objectif est de créer un programme qui prédit le prix d'une voiture en utilisant une fonction linéaire entraînée avec un algorithme de descente de gradient. Bien que nous travaillerons sur un exemple précis pour ce projet, vous serez en mesure d'utiliser l'algorithme avec n'importe quel autre jeu de données une fois terminé.

## Instructions Générales
- **Langage** : Vous êtes libre d'utiliser le langage de programmation de votre choix.
- **Bibliothèques** : Vous pouvez utiliser n'importe quelle bibliothèque, à condition qu'elle ne fasse pas tout le travail pour vous. Par exemple, l'utilisation de `numpy.polyfit` en Python est considérée comme de la triche.
- **Visualisation** : Choisissez un langage qui permet une visualisation facile des données, ce qui sera très utile pour le débogage.

## Partie Obligatoire
Implémentez un algorithme de régression linéaire sur un seul élément : le kilométrage d'une voiture. Pour ce faire, vous devez implémenter deux programmes :

1. **Programme de Prédiction** :
   - Ce programme sera utilisé pour prédire le prix d'une voiture en fonction de son kilométrage. Lorsque vous lancez le programme, il vous demandera un kilométrage et devra vous donner un prix approximatif de la voiture.

2. **Programme d'Entraînement** :
   - Ce programme sera utilisé pour entraîner votre modèle. Il lira le jeu de données et effectuera une régression linéaire sur ces données.
  
## Bonus

1. **Visualisation des Données** :
   - Affichez les données sur un graphique.

2. **Affichage de la Ligne de Régression** :
   - Affichez la ligne résultant de votre régression linéaire sur le même graphique et voyez si elle fonctionne !

3. **Affichage de la Courbe de Coût** :
   - Affichez la courbe résultant de l'historique de votre coût.

4. **Programme de Vérification de la Précision** :
   - Un programme qui vérifie la précision de votre algorithme.
  

## Install
Pour installer les dépendances nécessaires, utilisez le fichier `requirements.txt` :

```bash
pip3 install -r requirements.txt
```



## Usage

Pour utiliser le programme de prédiction, suivez les étapes suivantes :

1. **Préparer le fichier de paramètres** :
   - Assurez-vous que le fichier `params.txt` contient les valeurs de `theta0` et `theta1` sur deux lignes séparées. Par exemple :
     ```
     1.0
     2.0
     ```

2. **Lancer le programme** :
   - Exécutez le programme en utilisant la commande suivante :
     ```bash
     python3 priceEstimation.py
     ```

3. **Entrer le kilométrage** :
   - Le programme vous demandera d'entrer un kilométrage. Entrez un nombre entier positif.

4. **Obtenir le prix estimé** :
   - Le programme calculera et affichera le prix estimé de la voiture en fonction du kilométrage entré.

Exemple d'interaction :

```bash
Please enter a mileage:
10000
This car worth 12000 euros
```
