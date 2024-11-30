import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from rfpimp import *
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.metrics import mean_absolute_error

dataframe = pd.read_csv('MICRODADOS_ENEM_2023.csv', encoding='latin-1', sep=';')
dataframe = dataframe.sample(frac=0.1, random_state=42)

columns = [
    "TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA",
    "TP_NACIONALIDADE", "TP_ST_CONCLUSAO", "TP_ANO_CONCLUIU",
    "TP_ESCOLA", "TP_ENSINO", "IN_TREINEIRO", "Q001", "Q002", "Q003",
    "Q004", "Q005", "Q006", "Q007", "Q008", "Q009", "Q010", "Q011",
    "Q012", "Q013", "Q014", "Q015", "Q016", "Q017", "Q018", "Q019",
    "Q020", "Q021", "Q022", "Q023", "Q024", "Q025", 
    "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT"
]
dataframe = dataframe[columns]
dataframe.dropna(inplace=True, how='any', axis='index')

columns_to_convert = dataframe.select_dtypes(include=['object', 'bool']).columns
ordinal = OrdinalEncoder()
values_cat = ordinal.fit_transform(dataframe[columns_to_convert])
dataframe[columns_to_convert] = values_cat

columns_to_drop = ["NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_MT"]
dataframe['NU_NOTA_MEDIA'] = dataframe[columns_to_drop].mean(axis=1)
columns_to_drop.append("NU_NOTA_MEDIA")
X, y = dataframe.drop(columns=columns_to_drop), dataframe['NU_NOTA_MEDIA']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

rf = RandomForestRegressor(n_estimators=10)
model = rf.fit(X_train, y_train)

y_predict = rf.predict(X_test)

validation_e = mean_absolute_error(y_test, y_predict)
# print(f"{validation_e} average error;")

I = importances(rf, X_test, y_test)
# print(f"{I} importances;")

ref_cols = list(X.columns)
target = "NU_NOTA_MEDIA"

joblib.dump(value=[model, ref_cols, target], filename="./models/model_nota_MEDIA.pkl")
