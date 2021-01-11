from tensorflow.keras.datasets import cifar10
import numpy as np
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

#print(x_train.shape, y_train.shape) #(50000, 32, 32, 3) (50000, 1)
#print(x_test.shape, y_test.shape)   #(10000, 32, 32, 3) (10000, 1)

x_train= x_train.reshape(x_train.shape[0], -1,48)/255.
x_test= x_test.reshape(x_test.shape[0], -1,48)/255.
#이미지 특성맞춰 숫자 바꾸기 x의 최대가 255이므로 255로 나눈다.
#이렇게 하면 0~1 사이로 된다.
#x_test=x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2],1)
#x_train=x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2],1)
###이미 전처리 이걸로 해서 minmax안써도 됨


#다중분류 y원핫코딩
from keras.utils.np_utils import to_categorical
y_train = to_categorical(y_train) #(50000, 10)
y_test = to_categorical(y_test)  #(10000, 10)


#2. 모델 구성
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM

model =Sequential()
model.add(LSTM(units=12, activation='relu', input_shape=(8*8, 48)))
model.add(Dense(5))
model.add(Dense(10, activation='relu'))
model.add(Dense(5))
model.add(Dense(5, activation='relu'))
model.add(Dense(10, activation='softmax')) #y값 3개이다(0,1,2)
model.summary()

#3. 컴파일, 훈련
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['acc'])
####loss가 이진 분류일 때는binary_crossentropy(0,1만 추출)
model.fit(x_train,y_train, epochs=20, 
           validation_split=0.2, batch_size=16,verbose=1)

#4. 평가 훈련
loss=model.evaluate(x_test,y_test, batch_size=16)
print(loss)

y_pred = model.predict(x_test[:10])
print('y_pred: ', y_pred.argmax(axis=1))
print('y_test: ', y_test[:10].argmax(axis=1))

'''
[1.6705783605575562, 0.3659999966621399]
y_pred:  [3 8 8 8 4 6 1 5 5 8]
y_test:  [3 8 8 0 6 6 1 6 3 1]
'''
