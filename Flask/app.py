from flask import Flask
from flask import request, render_template
from flask_cors import CORS
import joblib
model=joblib.load('model.pkl')

app=Flask(__name__,static_url_path='')
CORS(app)

@app.route('/',methods=['GET'])
def sendhomepage():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def drugprediction():
    A=int(request.form['A'])
    S=request.form['S']
    B=request.form['B']
    C=request.form['C']
    N=float(request.form['N'])
    X =[[A,S,B,C,N]]
    prediction=model.predict(X)[0]
    return render_template('predict.html',predict=prediction)
if __name__=='__main__':
    app.run(debug=False)