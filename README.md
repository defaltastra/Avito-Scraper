# Scraper Avito Maroc Véhicules

Ce script permet de récupérer automatiquement des informations sur les annonces de véhicules disponibles sur le site Avito Maroc.

## Fonctionnalités

- Extraction des informations suivantes pour chaque annonce :
  - Nom du véhicule
  - Prix
  - Modèle (estimé à partir du titre)
  - Ville (sans le quartier)
- Navigation sur plusieurs pages d'annonces
- Sauvegarde des données au format Excel

## Prérequis

Pour utiliser ce script, vous aurez besoin d'installer les bibliothèques Python suivantes :

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Utilisation

1. Exécutez simplement le script Python :

```bash
python avito_scraper.py
```

2. Vous pouvez modifier cette valeur en changeant la variable `pages_a_scraper` dans la fonction `main()`.

3. Les résultats seront enregistrés dans un fichier Excel nommé "vehicules_avito.xlsx" dans le même répertoire que le script.

## Personnalisation

- **Nombre de pages** : Modifiez la variable `pages_a_scraper` dans la fonction `main()` pour analyser plus ou moins de pages.
- **Nom du fichier de sortie** : Modifiez le paramètre `nom_fichier` dans l'appel à la fonction `sauvegarder_excel()`.

## Avertissement

Ce script est fourni à des fins éducatives uniquement. L'utilisation de scripts d'extraction de données peut être soumise aux conditions d'utilisation du site web cible. Assurez-vous de respecter les conditions d'utilisation d'Avito Maroc et n'utilisez pas ce script de manière abusive.

Le script inclut des délais aléatoires entre les requêtes pour ne pas surcharger les serveurs d'Avito.

## Limites connues

- Les sélecteurs CSS utilisés pour extraire les données peuvent changer si Avito modifie la structure de son site.
- Le modèle du véhicule est estimé à partir des deux premiers mots du titre, ce qui peut ne pas être précis dans tous les cas.
