import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.externals import joblib
from normalization_coefficiants import *


X_cols = ['Cement (%W)', 'Water (%W)', 'Fine Agg (%W)', 'PCMs (%W)',
          'Fly ash (%W)', 'Silica Fume (%W)', 'Cenposphere (%W)', 'BFS (%W)',
          'Coarse Agg (%W)', 'AC (%W)', 'Superplasticiser (%W)',
          'Fiber Amount (%W)', 'PVA', 'PE', 'STEEL', 'CaCO3',
          'Polypropylene', 'Carbon', 'Glass', 'Basalt', 'UHMWPE',
          'F. Diameter (Micro-Meter)', 'Fiber Length (mm)',
          'Fiber Tensile Strength (Mpa)', 'Fiber Elastic Modulus (Gpa)',
          'Rubber', 'Lightw Agg',
          'MC (Viscosity Agent)', 'AEA', 'Oilling Agent/coating', 'HFV-Casting',
          'Graphene Oxide', 'Defoamer', 'Temperature', 'Water Curing',
          'Air Curing']

NX_cols = ['Fiber Amount (%W)', 'PVA', 'PE', 'STEEL', 'CaCO3',
           'Polypropylene', 'Carbon', 'Glass', 'Basalt', 'UHMWPE',
           'F. Diameter (Micro-Meter)', 'Fiber Length (mm)',
           'Fiber Tensile Strength (Mpa)', 'Fiber Elastic Modulus (Gpa)',
           'cs', 'ux2', 'ux1', 'us1', 'fs2', 'fx1', 'fs1', 'fx2', 'us2']

y_cols = ['cs', 'ux2', 'ux1', 'us1', 'fs2', 'fx1',
          'fs1', 'fx2', 'us2']  # Modified for Information Gain
full_feed = y_cols

models = []

for i, model_name in enumerate(y_cols):
    feed = y_cols[0:i][:]

    model = {"name": model_name,
             "X": X_cols,
             "y": [model_name],
             "feed": feed}
    models.append(model)

rf = {}
fN = {}


for model in models:
    name = model['name']

    rf[name] = joblib.load(f"Models/FRST/rf-{name}.pkl")
    fN[name] = tf.keras.models.load_model(f'Models/FDNN Ensemble/N-{name}.h5')


def encode(df):
    encoded = []

    for name, value in zip(df.columns, df.values.T):
        value = float(value[0])
        if name in y_cols:
            V = y_decodes[name]
        elif name in X_cols:
            V = X_decodes[name]

        val = (value - V["min"]) / (V["max"] - V["min"])  # normalization
        #val = (value - V["mean"]) / V["std"]
        encoded.append(val)
    V_en = pd.DataFrame(np.array(encoded), index=df.columns)
    return V_en.T


def decode(df):
    decoded = []

    for name, value in zip(df.columns, df.values.T):
        value = float(value[0])
        if name in y_cols:
            V = y_decodes[name]
        elif name in X_cols:
            V = X_decodes[name]

        # val = (value * V["std"]) + V["mean"]  # standardiztion
        val = value * (V["max"] - V["min"]) + V["min"]  # normalization
        decoded.append(val)
    V_de = pd.DataFrame(np.array(decoded), index=df.columns)
    return V_de.T


def nan_predict(predictions):
    array = []
    for i in range(len(predictions)):
        array.append(np.nan)
    df = pd.DataFrame(np.array(array))
    return df


def get_predictions(predictions, column_names):
    array = []
    for i in range(len(predictions)):
        array.append(predictions[i])
    df = pd.DataFrame(np.array(array), columns=column_names)
    return df


def ensemble_predict(x):
    list_of_xs = []
    for value in x.values():
        list_of_xs.append(value)

    xs = np.array(list_of_xs).astype(np.float).reshape(1, -1)
    xs = pd.DataFrame(xs, columns=X_cols)
    xs = encode(xs)

    y_pred = {}
    for output in y_cols:
        y_pred[output] = output

    predictions = []

    x_i = xs.copy()

    for model in models:
        name = model['name']
        feed = full_feed

        X_data = x_i.copy()

        for feed_name in feed:
            rf_predictions = rf[feed_name].predict(X_data)
            rf_predictions = pd.DataFrame(rf_predictions, columns=[feed_name])
            X_data = pd.concat([X_data, rf_predictions], axis=1)

        X_data = X_data[y_cols]
        fN_preds = fN[name].predict(X_data)

        predictions.append(get_predictions(
            fN_preds, [y_pred[name]]).values[0][0])

    predictions = np.array(predictions).reshape(1, 9)
    predictions = pd.DataFrame(predictions)
    predictions.columns = y_cols
    predictions = decode(predictions).values
    predictions = predictions.flatten().tolist()

    return predictions


# Mix Design Inputs
x = {}
exit_app = False

while exit_app != True:
    print("\n\nPlease Enter the Following Parameters: \n")

    for name in X_cols:
        x[name] = float(input(f"{name} = "))

    print("\nPlease Wait for predictions...\n")
    mechanical_properties = ['Compressive strength (cs)',
                            'peak tensile stress (ux2)',
                            'first crack tensile stress (ux1)',
                            'first crack tensile strain (us1)',
                            'peak flexural strain (fs2)',
                            'first crack flexural Strength (fx1)',
                            'first crack flexural strain (fs1)',
                            ' peak flexural strength (fx2)',
                            'peak tensile strain (us2)']
    results = ensemble_predict(x)

    for mp_name, p in zip(mechanical_properties, results):
        print(f"{mp_name} = {p}")

    exit_response = input("Press 'R' to make another prediction or another key to exit")
    if exit_response.lower() == 'r':
        exit_app = True