from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np

APP = Flask(__name__)
API = Api(APP)

PERFORMANCE_MODEL = pickle.load(open('perfomance.pkl', 'rb'))


@APP.route('/')
def hello_world():
    return render_template('predict_page.html')

@APP.route('/predict',methods=['POST','GET'])
class Predict:
    def predict():
        parser = reqparse.RequestParser()
        parser.add_argument('assignment')
        parser.add_argument('cats')
        parser.add_argument('attendance')

        args = parser.parse_args()  # creates dictionary

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        out = {'Prediction': PERFORMANCE_MODEL.predict([X_new])[0]}
        return out, 200

API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port=5000)
