# Excel to JSON Converter

Ce projet est une application web développée avec Flask qui permet de convertir un fichier Excel en un fichier JSON. Les utilisateurs peuvent télécharger un fichier Excel, sélectionner les colonnes qu'ils souhaitent convertir, et obtenir un fichier JSON en retour.

## Fonctionnalités

- Téléchargement d'un fichier Excel.
- Sélection des colonnes à convertir en JSON.
- Conversion et téléchargement d'un fichier JSON personnalisé.
- Gestion des dates (`Timestamp`) pour les rendre sérialisables en JSON.

## Prérequis

- Python 3.x
- Flask
- Pandas

## Installation

1. Clonez ce dépôt sur votre machine locale :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
2. Accédez au répertoire du projet :
    
    ```bash
    cd excel-to-json-converter
3. Installez les dépendances :

    Si vous avez déjà un fichier requirements.txt avec Flask et Pandas, exécutez la commande suivante :

    ```bash
    pip install -r requirements.txt

## Utilisation
1. Exécutez l'application :

    ```bash
    python app.py
2. Ouvrez un navigateur et accédez à l'adresse suivante :
    ```bash
    http://127.0.0.1:5000