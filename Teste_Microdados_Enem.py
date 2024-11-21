import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from rfpimp import *
from sklearn.ensemble import RandomForestClassifier
import joblib

dataframe = pd.read_csv('MICRODADOS_ENEM_2023.csv', encoding='latin-1', sep=';')
dataframe = dataframe.sample(frac=0.1, random_state=42)

columns_to_remove = ['TP_ENSINO', 'CO_MUNICIPIO_ESC', 'NO_MUNICIPIO_ESC', 'CO_UF_ESC', 'SG_UF_ESC', 'TP_DEPENDENCIA_ADM_ESC', 'TP_LOCALIZACAO_ESC', 'TP_SIT_FUNC_ESC', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT', 'TX_GABARITO_CN', 'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT']
dataframe.drop(columns=columns_to_remove, inplace=True)
dataframe.dropna(inplace=True, how='any', axis='index')

columns = dataframe.select_dtypes(include=['object', 'bool']).columns
ordinal = OrdinalEncoder()
values_cat = ordinal.fit_transform(dataframe[columns])
dataframe[columns] = values_cat

X, y = dataframe.drop(columns='NU_NOTA_REDACAO'), dataframe['NU_NOTA_REDACAO']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

rf = RandomForestRegressor(n_estimators=10)
model = rf.fit(X_train, y_train)

ref_cols = list(X.columns)
target = "NU_NOTA_REDACAO"

joblib.dump(value=[model, ref_cols, target], filename="./models/model_nota_REDACAO.pkl")
