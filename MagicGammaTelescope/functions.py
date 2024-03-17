import tensorflow as tf
import matplotlib.pyplot as plt

def train_model(x_train,y_train,num_nodes,lr,epoch,batch_size,dropout_prob):
    
    nn_model = tf.keras.Sequential([
        tf.keras.layers.Dense(num_nodes, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dropout(dropout_prob),
        tf.keras.layers.Dense(num_nodes, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    nn_model.compile(
        optimizer=tf.keras.optimizers.Adam(lr),
        loss = 'binary_crossentropy',
        metrics = ['accuracy'])

    history = nn_model.fit(
        x_train,y_train,epochs=epoch ,batch_size=batch_size, validation_split=0.2 , verbose = 0 
    )

    return nn_model,history


def plot_loss(history):

    plt.plot(history.history['loss'],label='loss')
    plt.plot(history.history['val_loss'],label='val_loss')
    plt.xlabel('Epoch')
    plt.ylabel('Binary Crossentropy')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_accuracy(history):

    plt.plot(history.history['accuracy'],label='accuracy')
    plt.plot(history.history['val_accuracy'],label='val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.grid(True)
    plt.show()