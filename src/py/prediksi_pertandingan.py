import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_model(df):
    """Melatih model Machine Learning berdasarkan data CSV."""
    
    if not {'HomeTeam', 'AwayTeam', 'FTR'}.issubset(df.columns):
        raise ValueError("CSV harus memiliki kolom: HomeTeam, AwayTeam, FTR")

    label_encoder = LabelEncoder()
    all_teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique()
    label_encoder.fit(all_teams)

    df['HomeTeam'] = label_encoder.transform(df['HomeTeam'])
    df['AwayTeam'] = label_encoder.transform(df['AwayTeam'])

    hasil_mapping = {'H': 0, 'A': 1, 'D': 2} 
    df['FTR'] = df['FTR'].map(hasil_mapping)

    X_home = df[['HomeTeam', 'AwayTeam']]
    y_home = df['FTHG']

    X_away = df[['HomeTeam', 'AwayTeam']]
    y_away = df['FTAG']
   
    # Model untuk Home Goals
    X_train_home, X_test_home, y_train_home, y_test_home = train_test_split(X_home, y_home, test_size=0.2, random_state=42)
    model_home = RandomForestClassifier(n_estimators=100, random_state=42)
    model_home.fit(X_train_home, y_train_home)

    # Model untuk Away Goals
    X_train_away, X_test_away, y_train_away, y_test_away = train_test_split(X_away, y_away, test_size=0.2, random_state=42)
    model_away = RandomForestClassifier(n_estimators=100, random_state=42)
    model_away.fit(X_train_away, y_train_away)


    return model_away, model_home, label_encoder

def prediksi_pertandingan(model_away, model_home, label_encoder, home_team, away_team):
    """Melakukan prediksi hasil pertandingan + skor berdasarkan model ML."""
    try:
        home_encoded = label_encoder.transform([home_team])[0]
        away_encoded = label_encoder.transform([away_team])[0]

        new_match = pd.DataFrame({
            'HomeTeam': [home_encoded],
            'AwayTeam': [away_encoded],
        })

        predicted_home_goals = model_home.predict(new_match)
        predicted_away_goals = model_away.predict(new_match)

        print(f"Predicted Score: {home_team} {predicted_home_goals[0]:.2f} - {predicted_away_goals[0]:.2f} {away_team}")

    except ValueError as e:
        print(f"Error: {e}. Please ensure that the team names are correct.")

    if predicted_home_goals[0] > predicted_away_goals[0] :
        hasil = f"{home_team} Menang"
    elif predicted_home_goals[0] < predicted_away_goals[0] :
        hasil = f"{away_team} Menang"
    else :
        hasil = 'Seri'

    return f"{hasil} (Skor: {home_team} {predicted_home_goals[0]:.2f} - {predicted_away_goals[0]:.2f} {away_team})"
