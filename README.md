# Prédiction de risque patient - Exercice Machine Learning

Petit projet pédagogique pour comprendre l'intégration d'un modèle de Machine Learning, du dataset à une API fonctionnelle.

## Objectif

Prédire si un patient est "à risque" ou non, à partir de trois informations : âge, tension, cholestérol — et exposer ce modèle via une API utilisable par n'importe quelle application.

## Ce que ce projet m'a permis d'apprendre

- Charger et manipuler des données avec **pandas**
- Distinguer les *features* (variables explicatives) de la *cible* (variable à prédire)
- Entraîner et évaluer un modèle de classification avec **scikit-learn** (régression logistique, train/test split)
- Sauvegarder un modèle entraîné avec **joblib**, pour le réutiliser sans le ré-entraîner
- Exposer un modèle via une **API REST avec Flask**
- Tester une API avec `curl`
- Versionner un projet Python avec Git/GitHub

## Technologies utilisées

- Python 3.14
- pandas
- scikit-learn
- Flask
- joblib

## Structure du projet