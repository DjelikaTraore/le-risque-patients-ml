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

import joblib #importation de la bibliothèque joblib pour la sérialisation des objets Python
# sauvegarde du modele entrainer dans un fichier .pkl
joblib.dump(modele, 'modele_risque.pkl') #sauvegarde du modèle entraîné dans un fichier .pkl
print("Le modèle a été sauvegardé dans le fichier modele_risque.pkl.")

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


# Evaluation du taux d'entraînement du modèle 
from sklearn.model_selection import train_test_split
# Séparation des données en ensembles d'entraînement et de test
# x_train  va contenir 80% des données pour l'entraînement et x_test contiendra 20% des données pour le test
# y_train va contenir les étiquettes correspondantes pour l'ensemble d'entraînement et y_test contiendra les étiquettes pour l'ensemble de test
# random_state=42 est utilisé pour garantir que la séparation des données est reproductible

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modele.fit(X_train, y_train) # Entraînement du modèle sur l'ensemble d'entraînement
print("Le modèle a été réentraîné sur l'ensemble d'entraînement.")
score = modele.score(X_test, y_test) # Évaluation du modèle sur l'ensemble de test
print("Taux de réussite du modèle :", score)



# Test interactif pour un patient
age = int(input("Entrez l'âge du patient : "))
while age < 0 or age > 120:
    print("Veuillez entrer un âge valide (entre 0 et 120).")
    age = int(input("Entrez l'âge du patient : "))
    
tension = int(input("Entrez la tension du patient : "))
while tension < 80 or tension > 220:
    print("Veuillez entrer une tension valide (entre 80 et 220).")
    tension = int(input("Entrez la tension du patient : "))

cholesterol = int(input("Entrez le cholestérol du patient : "))
while cholesterol < 100 or cholesterol > 400:
    print("Veuillez entrer un cholestérol valide (entre 100 et 400).")
    cholesterol = int(input("Entrez le cholestérol du patient : "))
    
# Création d'un DataFrame pour le patient avec les mêmes colonnes que le DataFrame  
nouveau_patient = pd.DataFrame({'age': [age], 'tension': [tension], 'cholesterol': [cholesterol]})
# Prédiction du risque pour le patient
prediction = modele.predict(nouveau_patient)
# Affichage de la prédiction
if prediction[0] == 1:
    print("Le patient est à risque.")
else:
    print("Le patient n'est pas à risque.")
