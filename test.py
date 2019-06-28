from agent.agent import Agent
import numpy as np
import random
from numpy import float64
from keras.models import Sequential
from keras.layers import Dense


### split_data - o functie care imparte data din fisierul data/GSPC in 4 seturi
###
### primul set consta in 80% din date din coloanele 1,2,3 si 4 care sunt folosite ca si predictori pentru a antrena modelele
### al doilea set consta din alceleasi date dar coloana 5 care este targetul nostru pentru model
### setul 3 si 4 sunt datele pe care le vom folosi pentru validare (scoring) respectiv valoarea reala

def split_data():
    train = []
    labels = []
    validation = []
    v_labels = []
    lines = open("data/^GSPC.csv", "r").read().splitlines()
    for line in lines[1:]:
        line_tokens = line.split(",")
        row = [float64(line_tokens[1]),
               float64(line_tokens[2]),
               float64(line_tokens[3]),
               float64(line_tokens[4])]
        target = [float64(line_tokens[5])]
        if random.random() < 0.8:  # random < 0.80 == 80% din data merge pentru training restul o sa o folosim la validare
            train.append(row)
            labels.append(target)
        else:
            validation.append(row)
            v_labels.append(target)
    return train, labels, validation, v_labels


# cele 4 seturi de date
training_data, training_labels, validation_data, validation_labels = split_data()

# se converteste array-ul la numpy array (modelele lucreaza cu numpy)
input_data = np.array(training_data, float64)
target_data = np.array(training_labels, float64)

# definim ce tip de model se va face
# aici se definesc parametrii modelului si in functie de aceste definitii va depinde acuratetea modelului
# pentru inceput alegem:
model = Sequential()
model.add(Dense(1, activation='linear'))
model.compile(loss="mse", optimizer='adam')
##########################

# antrenam modelul cu datele din setul de training si label-ul lor
model.fit(x=input_data, y=target_data, epochs=100, verbose=0)

# acum modelul este antrenat trebuie sa-l verificam cu setul de validare sa vedem cat ii de corect
# desi keras are functie de score care face acesta validare pentru valoarea academica o sa o scriem aici

values_predicted = np.array(validation_data, float64)
predicted_values = model.predict(values_predicted)
for i in range(predicted_values.__len__()):
    p_value = format(abs(predicted_values[i][0]), '.6f')
    print("Modelul prezice: " + str(p_value) + " cand valoarea era: " + str(validation_labels[i]))

# ^^^^^^^^ media erorilor (diferentelor intre valoarea prezisa si valoarea reala) este o masura a acuratetii modelului.
# Repetand operatiunea de la lina 48 in jos schimband valoarea parametrilor modelului (model) , adaugand alti estimatori se obtine un model cu o alta acuratete.
# Problema devine cum modifici linia 48->49 ai sa obtii un model mai bun - este o problema de "Hyper Parameters Optimization"