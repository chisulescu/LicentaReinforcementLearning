from agent.agent import Agent
import numpy as np
import keras
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.optimizers import Adam

def getStockDataVec():
    print("1111111")
    vec = []
    # lines = open("data\" + key + ".csv", "rb").read().splitlines()
    lines = open("data\^GSPC.csv", "r").read().splitlines()

    for line in lines[1:]:
        vec.append(float(line.split(",")[4]))

    print("333333")
    return vec


input_data = getStockDataVec()


model = Sequential()
model.add(Dense(units=64, input_dim=input_data.__len__(), activation="relu"))
model.add(Dense(units=32, activatio="relu"))
model.add(Dense(units=8, activation="relu"))
model.add(Dense(10, activation="linear"))
model.compile(loss="mse", optimizer=Adam(lr=0.001))

train_data = np.array([input_data])

model.fit(x=train_data)

model.predict()
