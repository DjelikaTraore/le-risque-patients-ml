from flask import Flask, request, jsonify 
import pandas as pd
import joblib

app = Flask(__name__)

# Chargement du modèle sauvegardé
modele = joblib.load('modele_risque.pkl')

@app.route('/predict', methods=['POST']) # Définition d'une route pour la prédiction du risque
def predict(): # def permet de définir une fonction pour la prédiction du risque
    donnees = request.get_json() #data = request.get_json() permet de récupérer les données JSON envoyées dans la requête POST
    age = donnees['age']
    tension = donnees['tension']
    cholesterols = donnees['cholesterol']

    # Création d'un DataFrame pour le patient
    patient_data = pd.DataFrame({'age': [age], 'tension': [tension], 'cholesterol': [cholesterols]})

    # Prédiction
    prediction = modele.predict(patient_data) # c'est la fonction predict() qui permet de faire une prédiction sur les données du patient
    probability = modele.predict_proba(patient_data) # c'est la fonction predict_proba() qui permet de récupérer les probabilités

    return jsonify({ # jsonify() permet de convertir le dictionnaire en JSON pour l'envoyer en réponse à la requête POST
      'risque': int(prediction[0]), # int(prediction[0]) permet de convertir la prédiction en entier pour l'envoyer en réponse à la requête POST
        'probabilite_risque': float (probability[0][1]) # probability[0][1] permet de récupérer la probabilité de risque pour le patient
    })

if __name__ == '__main__': # if __name__ == '__main__': permet de vérifier si le script est exécuté directement ou importé en tant que module
    app.run(debug=True, port=5000) # app.run(debug=True, port=5000) permet de lancer l'application Flask en mode debug sur le port 5000