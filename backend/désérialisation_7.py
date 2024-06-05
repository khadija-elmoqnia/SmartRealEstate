######################### Préparation des donnés explicatives 
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os
import pandas as pd

conversion_factor = 0.5906674542232723

def prepare_data(mortgage_15yr, consumer_price_index, gdp, personal_income, population, total_construction):
    data = {
    'Mortgage_15yr': mortgage_15yr ,
    'Consumer_Price_Index': consumer_price_index ,  # Indice (Jan 2000=100)
    'Gross Domestic Product': gdp * 1000000000,  # En milliards de dollars
    'Personal_Income': personal_income * 1000000000,  # En milliards de dollars
    'Population': population * 1000,  # En milliers
    'Total_Construction': total_construction * 1000000,  # En millions de dollars
}


    # Créer un DataFrame à partir de la ligne de données
    df = pd.DataFrame(data, index=[0])
    print(df.head())
    # Ajuster Consumer Price index 
    df['Consumer_Price_Index'] = df['Consumer_Price_Index'] * conversion_factor
    print(df.head())

     # Calculer les variables supplémentaires
    df['Economic_growth'] = df['Consumer_Price_Index'] * df['Gross Domestic Product']
    df['Construction_inflation'] = df['Consumer_Price_Index'] * df['Total_Construction']
    df['Wealth_density_index'] = df['Population'] * df['Personal_Income']
    print(df.head())

    # Supprimer les colonnes incorrectes
    columns_to_drop = ['Consumer_Price_Index', 'Personal_Income', 'Total_Construction','Population']
    df = df.drop(columns=columns_to_drop, axis=1)
    
    print("DATA AVANT NORMALISATION ",df.head())
      # Lire le fichier CSV
    data_with_features = pd.read_csv('c:\\Users\\H P\\Desktop\\SmartRealEstate\\backend\\data\\DATA_avecfeatures.csv', header=0)
    X = data_with_features.drop(columns=['DATE', 'Home_price_index'])
    # Créer un objet MinMaxScaler et l'adapter aux données existantes
    scaler = MinMaxScaler()
    scaler.fit(X)

    # Normaliser la ligne de données
    df_normalized = pd.DataFrame(scaler.transform(df), columns=df.columns)
    print("DATA APRES NORMALISATION ",df_normalized.head())
    return df_normalized




###################  Prediction 

import joblib

def predict_hpi(prepared_data):
    # Charger le modèle pré-entraîné
    model_path = "c:\\Users\\H P\\Desktop\\SmartRealEstate\\backend\\modele_gradient_boosting.pkl"
    model = joblib.load(model_path)
    
    # Faire des prédictions sur les données
    predictions = model.predict(prepared_data)
    
    return predictions


