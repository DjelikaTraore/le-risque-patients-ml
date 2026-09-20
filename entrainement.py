import pandas as pd #importation de la bibliothèque pandas pour la manipulation des données

## Chargement des données 
donnees = pd.read_csv('risque_patients.csv')

#affichage des 5 premières lignes du DataFrame
print(donnees.head())

#les features (variables explicatives) sont toutes les colonnes 
X = donnees[['age' , 'tension' , 'cholesterol']]

#la variable cible (variable à prédire) est la colonne 'risque'
y = donnees['risque']

print(X.head()) #affichage des 5 premières lignes du DataFrame X
print(y.head()) #affichage des 5 premières lignes du DataFrame y

#importation de la classe LogisticRegression de la bibliothèque scikit-learn
from sklearn.linear_model import LogisticRegression 

#creation du model
modele = LogisticRegression()

# entrainement de modele sur les donnees du csv
modele.fit(X, y)

print("modele entrainer !!")
#####
# test sur un patient
import pandas as pd
# Création d'un DataFrame pour un nouveau patient avec les mêmes colonnes que le DataFrame d'origine
# nouveau_patient = pd.DataFrame({'age': [55], 'tension': [140], 'cholesterol': [220]})
# print("Prédiction du risque pour le nouveau patient :", modele.predict(nouveau_patient))
# probabilite_risque = modele.predict_proba(nouveau_patient)
# print("Probabilité de risque pour le nouveau patient :", probabilite_risque)
###