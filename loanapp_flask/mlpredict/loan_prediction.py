import pickle

with open('model.pkl', 'rb') as file:
    rfc = pickle.load(file)

def predict_loan_application(data):
    # Use the model to make predictions
    prediction = rfc.predict(data)
    return prediction
