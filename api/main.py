
from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI(
    title="Movie Box Office Prediction API",
    description="An API for predicting the amount of money a movie generates.",
    version="1.0.0",
    docs_url='/'
)

@app.post('/v1/prediction') #path with post method (url)
def make_model_prediction(request: PredictionRequest):
    return PredictionResponse(worldwide_gross=get_prediction(request))



# Aquí hay un resumen de la estructura:

# app: Es una instancia de FastAPI, que representa la aplicación FastAPI.
# app.post('/v1/prediction'): Define una ruta para el método POST con la URL relativa /v1/prediction.
# make_model_prediction(request: PredictionRequest): Es una función que maneja la solicitud POST en 
# la ruta /v1/prediction. Toma un objeto PredictionRequest en el cuerpo de la solicitud y devuelve
#  una respuesta con un objeto PredictionResponse.