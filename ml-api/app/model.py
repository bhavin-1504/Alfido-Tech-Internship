import pickle

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(value: int):
    return int(model.predict([[value]])[0])