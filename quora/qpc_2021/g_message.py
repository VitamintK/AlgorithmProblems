import numpy as np
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras import layers

# gnrtr = (x for x in ['2','1 2 -1 5 4', '1 3 2 6 5 -1'])
# def input():
#     return next(gnrtr)

# read in the data
n = int(input())
data = []
maxlen = 0
maxint = 0
for i in range(n):
    words = [int(x) for x in input().split()]
    data.append(words)
    maxlen = max(maxlen, len(words))
    maxint = max(maxint, max(words))

# process the data
for datum in data:
    for i in range(len(datum)):
        if datum[i] == -1:
            datum[i] = maxint+1
forward_x = []
backward_x = []
forward_y = []
backward_y = []
real_indices = []
for datum in data:
    for i in range(len(datum)):
        if datum[i] == maxint+1:
            real_indices.append(len(forward_x))
        forward_x.append(datum[:i])
        forward_y.append(datum[i])
        backward_x.append(datum[i+1:])
        backward_y.append(datum[i])
        
def one_hot(x):
    # hack: increase the size of the one-hot encoding by 1 so that a value of -1 just maps to the last value
    ans = np.zeros(maxint+2)
    ans[x] = 1
    return ans

for i in range(len(forward_x)):
#     forward_x[i] = [one_hot(x) for x in forward_x[i]]
#     backward_x[i] = [one_hot(x) for x in backward_x[i]]
    forward_y[i] = one_hot(forward_y[i])
    backward_y[i] = one_hot(backward_y[i])

# print(data[:100])

forward_x = keras.preprocessing.sequence.pad_sequences(forward_x, maxlen=maxlen)
backward_x = keras.preprocessing.sequence.pad_sequences(backward_x, maxlen=maxlen)
forward_y = np.array(forward_y)
backward_y = np.array(backward_y)

# build the model
# https://keras.io/examples/nlp/bidirectional_lstm_imdb/
inputs = keras.Input(shape=(None,), dtype="int32")
# Embed each integer in a 128-dimensional vector
x = layers.Embedding(maxint+2, 10)(inputs)
# Add 2 bidirectional LSTMs
x = layers.Bidirectional(layers.LSTM(64, return_sequences=True))(x)
x = layers.Bidirectional(layers.LSTM(64))(x)
# Add a classifier
outputs = layers.Dense(maxint+2, activation="softmax")(x)
model1 = keras.Model(inputs, outputs)

model1.compile("adam", "categorical_crossentropy", metrics=["accuracy"])
model1.fit(forward_x, forward_y, batch_size=40, epochs=20,verbose=0)


# build the model
# https://keras.io/examples/nlp/bidirectional_lstm_imdb/
inputs = keras.Input(shape=(None,), dtype="int32")
# Embed each integer in a 128-dimensional vector
x = layers.Embedding(maxint+2, 10)(inputs)
# Add 2 bidirectional LSTMs
x = layers.Bidirectional(layers.LSTM(64, return_sequences=True))(x)
x = layers.Bidirectional(layers.LSTM(64))(x)
# Add a classifier
outputs = layers.Dense(maxint+2, activation="softmax")(x)
model2 = keras.Model(inputs, outputs)

model2.compile("adam", "categorical_crossentropy", metrics=["accuracy"])
model2.fit(backward_x, backward_y, batch_size=40, epochs=20,verbose=0)

for index in real_indices:
    print(forward_x[index])
    print(forward_y[index])
    ans = model1.predict([forward_x[index]])[0]
    ans += model2.predict([backward_x[index]])[0]
    print(ans)
    print(np.argmax(ans[1:-1]))