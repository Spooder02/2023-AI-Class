# using Library
import tensorflow as tf
import pandas as pd
# data
file_dir = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
iris = pd.read_csv(file_dir)
iris.head()
#원핫encoding
encoding = pd.get_dummies(iris)
encoding.head()
print(encoding.shape)
print(encoding.columns)
#독립변수, 종속변수
# 독립변수, 종속변수
independent = encoding[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
dependent = encoding[['품종_setosa', '품종_versicolor','품종_virginica']]
print(independent.shape, dependent.shape)
encoding.head()
encoding.tail()
#모델의 구조
# 모델의 구조 만듦
X = tf.keras.layers.Input(shape=[4]) #4란 숫자는 독립변수(속성, feature) 숫자
Y = tf.keras.layers.Dense(3, activation='softmax')(X) #3이란 숫자는 종속변수 숫자
model = tf.keras.models.Model(X,Y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')
#데이터로 모델을 학습(Fit)
model.fit(independent, dependent, epochs=1000)
#모델을 이용합니다.
#모델 사용
model.predict(independent[0:5])
print(dependent[0:5])
model.predict(independent[-5:])
print(dependent[-5:])
#학습한 가중치
model.get_weights()