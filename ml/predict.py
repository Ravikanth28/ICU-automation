import pickle
import datetime

with open("ml/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_demand():
    hour = datetime.datetime.now().hour
    prediction = model.predict([[hour]])
    return int(prediction[0])
