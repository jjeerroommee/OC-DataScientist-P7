import streamlit as st
import requests


def request_prediction(data):
    data_json = {'inputs': data}

    response = requests.request(
        method='POST',
        headers={"Content-Type": "application/json"},
        
        #url='http://localhost:5000/predict', # when using a local flask server
        url='https://oc-datascientist-p7-lgbm.azurewebsites.net/predict/', # when using an Azure clouded server
        json=data_json)
    
    if response.status_code != 200 :
        raise Exception(
            "Request failed with status {}, {}".format(response.status_code, response.text))

    return response.json()


def main():
    st.title("API de prédiction de solvabilité d'un client bancaire")
    st.header("Interface de test locale (streamlit)")
    
    st.markdown("Saisir les variables décrivant la situation d'un client :")
    
    data={}
    data['EXT_SOURCE_3'] = [st.number_input('ext_source_3 (décimal entre 0 et 1)',
                                   min_value=0., max_value=1.0, value=0.50, step=0.01)]

    data['EXT_SOURCE_2'] = [st.number_input('ext_source_2 (décimal entre 0 et 1)',
                              min_value=0., max_value=1.0, value=0.49, step=0.01)]

    data['PAYMENT_RATE'] = [st.number_input('payment_rate (décimal entre 0 et 1)',
                                   min_value=0.01, max_value=.13, value=0.05, step=0.01)]

    data['EXT_SOURCE_1'] = [st.number_input('ext_source_1 (décimal entre 0 et 1)',
                                   min_value=0., max_value=1.0, value=0.50, step=0.01)]

    data['NAME_FAMILY_STATUS_Married'] = [st.number_input('name_family_status_married (booléen)',
                                 min_value=0, max_value=1, value=1, step=1)]

    data['CODE_GENDER_F'] = [st.number_input('code_gender_f (booléen)',
                                    min_value=0, max_value=1, value=1, step=1)]

    data['AMT_ANNUITY'] = [st.number_input('amt_annuity (entier avec pas = 1000)',
                                  min_value=1000, max_value=130000, value=27000, step=1000)]

    data['APPROVED_CNT_PAYMENT_MEAN'] = [st.number_input('approved_cnt_payment_mean (entier avec pas = 1)',
                                                min_value=0, max_value=100, value=14, step=1)]

    predict_btn = st.button('Prédire')
    st.markdown("L'API retourne la classe (*accepté*/*refusé*) et la valeur prédite par le modèle :")
    st.markdown("\t- crédit accepté si probabilité de défaut du client ~ 0")
    st.markdown("\t- crédit refusé si probabilité de défaut du client ~ 1")
    st.markdown("---")

    if predict_btn :
        pred = request_prediction(data)
        st.write('Classe : ', pred['classe'])
        st.write('Probabilité de défaut : ', pred['proba_echec'])


if __name__ == '__main__':
    main()
