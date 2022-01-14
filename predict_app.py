from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('perfomance.pkl','rb'))


@app.route('/')
def home():
    return render_template("predict_page.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=np.fromiter(int_features,dtype=float)
    out= {model.predict([final])[0]}
    return render_template('predict_page.html',pred='Your Expected Grade is {}'.format(out))


if __name__ == '__main__':
    app.run(debug=True)