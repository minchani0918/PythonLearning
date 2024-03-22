import pandas as pd
import tensorflow as tf

파일경로 = "https://raw.githubusercontent.com/minchani0918/PythonLearning/main/boston%20(1).csv"
보스턴 = pd.read_csv(파일경로)
print(보스턴.columns)
보스턴.head()

독립 = 보스턴[['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','b','lstat']]
종속 = 보스턴[['medv']]
print(독립.shape,종속.shape)

X = tf.keras.layers.Input(shape=[13])
Y = tf.keras.layers.Dense(1)(X)

model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

model.fit(독립,종속,epochs=1000,verbose=0)
model.fit(독립,종속,epochs=10)

print(model.predict(독립[5:10]))
print(종속[5:10])
print(model.get_weights())