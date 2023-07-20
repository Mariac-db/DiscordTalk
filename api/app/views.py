from .models import PredictionRequest
from .utils_api import get_model, transform_to_dataframe

model = get_model()

def get_prediction(request: PredictionRequest) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return max(0, prediction)

# el max 0 es porque no se debe entregar una predicción cruda a un usuario final, y podrían haber errores
# en el caso que las predicciones sean negativas elegimos el valor máximo para nunca dar algún valor 
# negativo, es nice tener un manejo de esos casos, qué se hará cuándo la inferencia no sea correcta?


