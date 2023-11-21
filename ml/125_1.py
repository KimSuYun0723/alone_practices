import tenserflow as tf
import numpy as np

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10, 13.])

model  tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(1,))
    tf.keras.layers.Dense(1)
])

model.compile(optimizer = 'sgd', loss = 'mean_squared_error')
model.fit(xs, ys, epochs=5)

p = model.predict([10.0])

print('p: ', p)