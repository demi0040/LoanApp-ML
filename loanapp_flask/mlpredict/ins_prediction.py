import pickle

with open('medic_ins/model.pkl', 'rb') as file:
    plr = pickle.load(file)

def predict_loan_application(data):
    # Use the model to make predictions
    prediction = plr.predict(data)
    return prediction
