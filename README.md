# Prédiction de risque patient - Exercice Machine Learning

Petit projet pédagogique pour comprendre l'intégration d'un modèle de Machine Learning, du dataset à la prédiction interactive.

## Objectif

Prédire si un patient est "à risque" ou non, à partir de trois informations : âge, tension, cholestérol.

## Ce que ce projet m'a permis d'apprendre

- Charger et manipuler des données avec **pandas**
- Distinguer les *features* (variables explicatives) de la *cible* (variable à prédire)
- Entraîner un modèle de classification avec **scikit-learn** (régression logistique)
- Faire des prédictions et interpréter des probabilités
- Rendre un programme interactif avec `input()`

## Technologies utilisées

- Python 3.14
- pandas
- scikit-learn

## Comment lancer le projet

```bash
python entrainement.py
```

Le programme demande l'âge, la tension et le cholestérol du patient, puis affiche la prédiction (à risque ou non) avec le pourcentage de confiance.

## Données

Le fichier `risque_patients.csv` contient un jeu de données fictif de 10 patients, créé à des fins pédagogiques uniquement — aucune donnée réelle.

## Prochaines étapes

- [ ] Exposer le modèle via une API Flask
- [ ] Tester avec `curl`