#accuracy확인

import numpy as np
from sklearn.datasets import load_iris

dataset = load_iris() #x,y=load_iris(return_X_y=True)와 같다
x= dataset.data
y= dataset.target
#print(dataset.DESCR)
#print(dataset.feature_names)

#print(x.shape) #(150,4)
#print(y.shape) #y가 3종류(150,)---> 바뀔거다
#print(x[:5])
'''
print(y)
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2] --> 이렇게 0,1,2 섞어서 나온다. 0,1만 나오게 수정해야함
'''
'''
######sklearn로 전처리 하기 ----> 근데 이걸로 하면 안된다.
###이거는 0,1,2 라벨 숫자 부여하는 것
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
e = LabelEncoder()
e.fit(y)
y = e.transform(y)
y = np_utils.to_categorical(y)
print(y.shape)
print(y)
'''
from sklearn.preprocessing import OneHotEncoder 
#sklearn 데이터 다중분류 경우 이거 사용
encoder = OneHotEncoder()
y = encoder.fit_transform(y.reshape(-1,1)).toarray()

# 전처리 알아서/ minmax, train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y, 
                     shuffle=True, train_size=0.8, random_state=66)

from sklearn.preprocessing import MinMaxScaler
scaler =MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
'''
#### 원핫인코딩 oneHotEcoding####  ----> 이거 텐져플로우 데이터인 경우
from tensorflow.keras.utils import to_categorical
y= to_categorical(y)
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)
#print(y.shape) #(150,3)
#print(y)
'''
'''
#print(y)#벡터형식으로 바뀐다. 0,1,2 사라지고 벡터로 변경
[1. 0. 0.]
 [1. 0. 0.]
 [1. 0. 0.]
 [1. 0. 0.]
 [1. 0. 0.]
 [1. 0. 0.]
 [1. 0. 0.]
 [1. 0. 0.]
'''

#2. 모델
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
#model.add(Dense(1)) #-->hidden이 없는 layer가 있다. 
# activation 다음 층으로 연결할때 전달하는 방법
model.add(Dense(3, activation='softmax')) #y값 3개이다(0,1,2)
#분류하고자 하는 노드에 개수를 output나오게 해라
#linear은 선형, relu는 회귀, sigmoid는 이진분류

#3. 컴파일, 훈련
                   #mean_squared_error
model.compile(loss='categorical_crossentropy', 
              optimizer='adam', metrics=['acc', 'mae'])
####loss가 이진 분류일 때는binary_crossentropy(0,1만 추출)
model.fit(x_train,y_train, epochs=150, 
           validation_split=0.2, batch_size=10,verbose=0)

#4. 평가 ,예측
loss=model.evaluate(x_test,y_test, batch_size=10)
print(loss)  #loss, accurac 값 추출
#y_pred=model.predict(x[-5:-1])
#print(y_pred) # y_pred로 코딩한 값
#print(y[-5:-1]) 

'''
y_pred=model.predict(x[-5:-1])
print(y_pred) -원핫인코딩 한값
[2.3917291e-23 3.4554517e-09 1.0000000e+00]
 [2.9042364e-21 4.1744691e-08 1.0000000e+00]
 [5.4568571e-22 2.7116839e-08 1.0000000e+00]
 [1.2453324e-22 1.7178943e-08 1.0000000e+00]]
원래 y값
[[0. 0. 1.]
 [0. 0. 1.]
 [0. 0. 1.]
 [0. 0. 1.]]
'''

##argmax로 결과치 수정

y1_pred = model.predict(x_test[-5:-1])
print(y1_pred)
print(np.argmax(y1_pred, axis=1))# 가장 큰 클래스를 출력해주는 함수
#axis=0 0이 위치하는 데이터 인덱스가 0부터 시작하므로 [0,1,2]
#행마다 위치하는 값이 2니까 행이 

'''
결과
[0.2929254472255707, 0.9666666388511658, 0.15748263895511627]
[[1.4803344e-03 8.8146053e-02 9.1037357e-01]
 [9.9200785e-01 7.4190465e-03 5.7309697e-04]
 [7.6894391e-01 2.2478288e-01 6.2731630e-03]
 [1.1676942e-02 5.5393237e-01 4.3439060e-01]]
[2 0 0 1]
'''
