import tensorflow as tf
import pandas as pd
#데이터 준비
file_dir = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
data = pd.read_csv(file_dir)
data.head()
# independent변수, dependent변수
independent = data[['온도']]
dependent = data[['판매량']]
print(independent.shape, dependent.shape)
#모델 만들기
X = tf.keras.layers.Input(shape=[1]) #1은 independent변수 숫자
Y = tf.keras.layers.Dense(1)(X) #1은 dependent변수 숫자
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')
#모델을 학습(FIT)
model.fit(independent, dependent, epochs=6000, verbose=0)
#모델을 재학습(FIT)
model.fit(independent, dependent, epochs=10)
#Use model if model loss reached 0.0002
model.predict(independent)
#dependent
#15도라면 몇개의 레모네이를 만들어야 하는가
print(model.predict([[15]]))