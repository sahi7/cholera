import joblib
import numpy as np
from flask import Flask,request, url_for, redirect, render_template, jsonify

app = Flask(__name__)
app.static_folder = 'static'


model_DT = joblib.load('models/CHOLERA_DT.pkl')
#model_GB = joblib.load('models/CHOLERA_GB.pkl')
model_KNN = joblib.load('models/CHOLERA_KNN.pkl')
model_LR = joblib.load('models/CHOLERA_LR.pkl')
model_RFC = joblib.load('models/CHOLERA_RFC.pkl')
model_SVM = joblib.load('models/CHOLERA_SVM.pkl')

@app.route('/')
def welcome():
    return render_template("home.html")


@app.route('/diagnosis', methods=['POST','GET'])
def diagnosis():
    title = 'Diagnosis'
    desc = 'Identification of Vibrio cholerae'
    if request.method == 'POST':
        if request.is_json:
            response_data = request.get_json()
        else:
            response_data = request.form.to_dict()
            

        # Perform necessary processing with the data
        ques1 = request.form.get('ques1')
        ques2 = request.form.get('ques2')
        ques3 = request.form.get('ques3')
        ques4 = request.form.get('ques4')
        quantity1 = int(request.form.get('quantity1'))
        quantity2 = int(request.form.get('quantity2'))

        if ques1 == "yes" and ques2 == "yes" and quantity1 > 3 and quantity2 > 3:
            result = 'Positive'
        elif quantity1 < 3 and quantity2 < 3:
            result = 'Negative'
        elif ques1 == "yes" and ques4 == "yes":
            result = 'Positive'
        elif ques2 == "yes" and ques3 == "yes":
            result = 'Positive'
        else:
            result = 'Negative'
        
        desc = 'Patient screening complete'
        response_data['title'] = title
        response_data['desc'] = desc
        response_data['result'] = result
        print('respose', response_data)
        # Render the results template or return JSON response
        if request.is_json:
            return jsonify(response_data)
        else:
            return render_template("results.html", data=response_data)

    # Render the diagnosis template for GET requests
    return render_template("diagnosis.html", title=title, desc=desc)
    


@app.route('/prevention')
def prevention():
    title = 'Prevention'
    desc = 'Always boil all drinking water or treat it with chlorine'
    return render_template("prevention.html", title=title, desc=desc)



@app.route('/treatment')
def treatment():
    title = 'Treatment'
    desc = 'Rehydration therapy | Antibiotics | Zinc treatment'
    return render_template("treatment.html", title=title, desc=desc)



@app.route('/results',methods=['POST','GET'])
def results():
    title = 'Diagnosis'
    desc = 'Patient screening complete'

    return render_template("home.html", data=response_data)



@app.route('/predict',methods=['POST','GET'])
def predict():

    try:
        int_features=[int(x) for x in request.form.values()]
    except:
        return render_template('error.html')
    final=[np.array(int_features)]

    print(int_features)
    print(final)

    res_DT = model_DT.predict_proba(final)
    print('Predict Proba DT - {}'.format(res_DT))

    #res_GB = model_GB.predict_proba(final)
    #print('Predict Proba GB - {}'.format(res_GB))

    res_KNN = model_KNN.predict_proba(final)
    print('Predict Proba KNN - {}'.format(res_KNN))
    
    res_LR = model_LR.predict_proba(final)
    print('Predict Proba LR - {}'.format(res_LR))

    res_RFC = model_RFC.predict_proba(final)
    print('Predict Proba RFC - {}'.format(res_RFC))

    ensemble_result = [res_KNN[0], res_LR[0], res_RFC[0]]

    output = np.mean(ensemble_result, axis = 0)
    print(output)

    print('Final Prediction - Class {}'.format(output.argmax()))

    if output.argmax() == 1:
        return render_template('disease.html', pred='Danger.\nProbability of Cholera occuring is {}'.format(output[output.argmax()]))
    else:
        return render_template('disease.html', pred='Safe.\n Probability of Cholera not occuring is {}'.format(output[output.argmax()]))

if __name__=='__main__':
    app.run(debug = True, threaded = True)