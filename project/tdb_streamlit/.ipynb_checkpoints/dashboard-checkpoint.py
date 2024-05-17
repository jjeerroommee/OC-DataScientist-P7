import pandas as pd
import streamlit as st
import requests


def request_prediction(data):
    data_json = {'inputs': data}

    response = requests.request(
        method='POST',
        headers={"Content-Type": "application/json"},
        url='http://localhost:5000/predict',
        json=data_json)

    if response.status_code != 200 :
        raise Exception(
            "Request failed with status {}, {}".format(response.status_code, response.text))

    return response.json()


def main():
    st.title("Test de l'API de prédiction de solvabilité d'un client bancaire")

    ext_source_3 = st.number_input('ext_source_3 (décimal entre 0 et 1)',
                                   min_value=0., max_value=1.0, value=0.50, step=0.01)

    ext_source_2 = st.number_input('ext_source_2 (décimal entre 0 et 1)',
                              min_value=0., max_value=1.0, value=0.49, step=0.01)

    payment_rate = st.number_input('payment_rate (décimal entre 0 et 1)',
                                   min_value=0.01, max_value=.13, value=0.05, step=0.01)

    ext_source_1 = st.number_input('ext_source_1 (décimal entre 0 et 1)',
                                   min_value=0., max_value=1.0, value=0.50, step=0.01)

    name_family_status_married = st.number_input('name_family_status_married (booléen)',
                                 min_value=0, max_value=1, value=1, step=1)

    code_gender_f = st.number_input('code_gender_f (booléen)',
                                    min_value=0, max_value=1, value=1, step=1)

    amt_annuity = st.number_input('amt_annuity (entier avec pas = 1000)',
                                  min_value=1000, max_value=130000, value=27000, step=1000)

    approved_cnd_payment_mean = st.number_input('approved_cnd_payment_mean (entier avec pas = 5)',
                                                min_value=0, max_value=100, value=14, step=5)

    predict_btn = st.button('Prédire')
    if predict_btn:
        data = [[ext_source_3, ext_source_2, payment_rate, ext_source_1,
                 name_family_status_married, code_gender_f, amt_annuity, approved_cnd_payment_mean]]
        
        pred = request_prediction(data)
        st.write(
            'Variable 1 = {:.2f}'.format(data[0]))


if __name__ == '__main__':
    main()
