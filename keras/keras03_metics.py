import numpy as np
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# from tensorflow.keras import model로 하면 
# keras의 model을 불러들이는 것
# 2에서 모델구성 model =models.Sequential() 이렇게 해야 에러 안남
# from tensorflow import keras로 하면 
# 2에서 모델구성 model =keras.models.Sequential() 이렇게 해야 에러 안남

#1.데이터
x_train=np.array([1,2,3,4,5])
y_train=np.array([1,2,3,4,5]) 
#x,y개수 같게-데이터많을수록 훈련 더 잘됨

x_test=np.array([6,7,8]) #x의 평가 데이터
y_test=np.array([6,7,8])
#훈련데이터에는 x_train, y_train
#평가데이터는 x_test,y_test 따라서 평가데이터라서 훈련x

#2.모델 구성
model =Sequential()
# model =models.Sequential()
# model =keras.models.Sequential()
# from을 어떻게 설정하냐에 따라 모델구성 달라짐
model.add(Dense(5, input_dim=1, activation='relu'))
#activation 활성화 함수
model.add(Dense(25))
#activation을 안쓴것은 default(기본값)이 있다는 것 
# 위activation과 연관없음 안쓰면 linear로 자동으로 됨
model.add(Dense(20))
model.add(Dense(10))
model.add(Dense(3))
model.add(Dense(1)) # 마지막은 바꾸면 안됨

#3. 컴파일, 훈련
#model.compile(loss='mse', optimizer='adam', metrics=['accuracy']) #acc = acuracy
#model.compile(loss='mse', optimizer='adam', metrics=['mse'])
model.compile(loss='mse', optimizer='adam', metrics=['mae'])  #mae : 평균절대오차 
model.fit(x_train, y_train, epochs=100, batch_size=1)

#4.평가 예측
loss=model.evaluate(x_test, y_test, batch_size=1) #두개 이상이면 list로 묶는다.
print('loss : ', loss)
#result = model.predict([9])  #실습값이 9가 나오는지 확인
result = model.predict([x_train]) 
#만약 x값을 트레인으로 한다면 5개의 값이 나온다. metrixs이므로
print("result : ", result) 
