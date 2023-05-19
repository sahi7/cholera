import joblib
import numpy as np

model_DT = joblib.load('models/CHOLERA_DT.pkl')
model_GB = joblib.load('models/CHOLERA_GB.pkl')
model_KNN = joblib.load('models/CHOLERA_KNN.pkl')
model_LR = joblib.load('models/CHOLERA_LR.pkl')
model_RFC = joblib.load('models/CHOLERA_RFC.pkl')
model_SVM = joblib.load('models/CHOLERA_SVM.pkl')

input_arr = np.array([35, 0, 1, 1, 97, 100, 60, 92]).reshape(1, -1)

def predict(input, model):
    return model.predict(input)

def predict_proba(input, model):
    return model.predict_proba(input)

res_DT = predict(input_arr, model_DT)
print(res_DT)

res_DT_proba = predict_proba(input_arr, model_DT)
print(res_DT_proba)



res_GB = predict(input_arr, model_GB)
print(res_GB)

res_GB_proba = predict_proba(input_arr, model_GB)
print(res_GB_proba)



res_KNN = predict(input_arr, model_KNN)
print(res_KNN)

res_KNN_proba = predict_proba(input_arr, model_KNN)
print(res_KNN_proba)



res_LR = predict(input_arr, model_LR)
print(res_LR)

res_LR_proba = predict_proba(input_arr, model_LR)
print(res_LR_proba)



res_RFC = predict(input_arr, model_RFC)
print(res_RFC)

res_RFC_proba = predict_proba(input_arr, model_RFC)
print(res_RFC_proba)



res_SVM = predict(input_arr, model_SVM)
print(res_SVM)

res_SVM_proba = predict_proba(input_arr, model_SVM)
print(res_SVM_proba)


ensemble_result = [res_DT_proba[0], res_GB_proba[0], res_KNN_proba[0], res_LR_proba[0], res_RFC_proba[0]]
print(ensemble_result)

output = np.mean(ensemble_result, axis = 0)
print(output)
print('Final Prediction - Class {}'.format(output.argmax()))