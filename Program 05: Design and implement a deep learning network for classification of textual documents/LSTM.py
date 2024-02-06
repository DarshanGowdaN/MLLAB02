import tensorflow as tf
from tensorflow.keras.models import Sequential
from keras.datasets import imdb
from tensorflow.keras.layers import Dense, LSTM, Dropout, Embedding
from tensorflow.keras.preprocessing import sequence

# tf.random.set_seed(7)
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = 6000)
x_train = sequence.pad_sequences(x_train,maxlen = 5)
x_test = sequence.pad_sequences(x_test,maxlen = 5)
print(x_train.shape)

model = Sequential()
model.add(Embedding(top_words,embedding_vector_length,input_length=32))
model.add(Dropout(0.2))
model.add(LSTM(200))
model.add(Dense(1,activation='sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=3,batch_size=64)

scores = model.evaluate(x_test,y_test,verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))
