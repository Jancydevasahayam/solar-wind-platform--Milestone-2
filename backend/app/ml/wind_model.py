from sklearn.ensemble import RandomForestRegressor
import numpy as np



def train_wind_model():

    X = np.array([
        [3.5, 25],
        [5.0, 30],
        [7.0, 32],
        [8.5, 35],
        [4.0, 28]
    ])


    y = np.array([
        200,
        350,
        600,
        800,
        300
    ])


    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )


    model.fit(X,y)

    return model



wind_model = train_wind_model()



def predict_wind_energy(
        wind_speed,
        temperature
):

    prediction = wind_model.predict(
        [[wind_speed, temperature]]
    )

    return round(float(prediction[0]),2)