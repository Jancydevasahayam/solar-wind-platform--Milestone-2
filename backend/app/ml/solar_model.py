from sklearn.ensemble import RandomForestRegressor
import numpy as np


def train_solar_model():

    # Example training data
    X = np.array([
        [5.5, 30],
        [4.2, 32],
        [3.5, 28],
        [6.0, 35],
        [2.8, 25]
    ])

    # Energy output (kWh)
    y = np.array([
        550,
        420,
        300,
        620,
        250
    ])


    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model



solar_model = train_solar_model()



def predict_solar_energy(
        irradiance,
        temperature
):

    prediction = solar_model.predict(
        [[irradiance, temperature]]
    )

    return round(float(prediction[0]),2)