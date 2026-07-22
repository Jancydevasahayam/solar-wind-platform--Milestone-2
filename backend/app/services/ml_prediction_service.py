from app.ml.solar_model import predict_solar_energy
from app.ml.wind_model import predict_wind_energy



def get_solar_energy_prediction(
        irradiance,
        temperature
):
    """
    Predict solar energy output using ML model.
    """

    energy_output = predict_solar_energy(
        irradiance,
        temperature
    )

    return {
        "input_solar_irradiance": irradiance,
        "input_temperature": temperature,
        "predicted_energy_output_kwh": energy_output
    }



def get_wind_energy_prediction(
        wind_speed,
        temperature
):
    """
    Predict wind energy output using ML model.
    """

    energy_output = predict_wind_energy(
        wind_speed,
        temperature
    )

    return {
        "input_wind_speed": wind_speed,
        "input_temperature": temperature,
        "predicted_energy_output_kwh": energy_output
    }