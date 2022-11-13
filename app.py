import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

print(pickle.__version__)
appRohit = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))


@appRohit.route('/')
def home():
    return render_template("index.html")

@appRohit.route('/predict', methods = ['POST'])
def predict():
    '''
    Fore rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text = 'Emplyee Salary should be $ {}'.format(output))

if __name__ == "__main__":
    appRohit.run(debug=True) 
