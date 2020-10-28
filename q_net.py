import tensorflow as tf
from tensorflow import keras
    
def build_dqn_model(lr):
    model = keras.Sequential([
        keras.layers.Dense(128, input_shape = (2, ), activation='relu'),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(3, activation='linear')])
    model.compile(optimizer=keras.optimizers.Adam(learning_rate=lr), loss='mean_squared_error')
    #model.save('q_net_model')
    return model


