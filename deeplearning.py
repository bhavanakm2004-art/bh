#CNNIMAGEPROCESSING
#1. import libraries
import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

#2. load dataset(MNIST is a built in data)
(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data()
print((x_train,y_train),(x_test,y_test))

#3. normalize data(scale pixel values to 0-1)
x_train=x_train.astype("float32") / 255.0
x_test=x_test.astype("float32") / 255.0
#4. reshape data(CNN expects 3D: height,width,channels)
x_train=x_train.reshape(-1,28,28,1)     #-1 means "figure this dimension out automatically"
x_test=x_test.reshape(-1,28,28,1)       #1 is the no of channels

#5. build a simple CNN model
model=models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),  #convolution
    layers.MaxPooling2D((2,2)),  #pooling layer
    layers.Flatten(),    #flatten into 1D
    layers.Dense(64,activation='relu'), #fully connected layer
    layers.Dense(10,activation='softmax') #output layer (10 classes)
])

#6. compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#7. train the model
history=model.fit(x_train,y_train,
                  epochs=5,
                  batch_size=64,    #faster training
                  validation_data=(x_test,y_test),
                  verbose=1)    #shows progress bar

#8. evaluate on test data
test_loss,test_acc=model.evaluate(x_test,y_test,verbose=0)
print("Test Accuracy:",round(test_acc*100,2),"%")

#9. predict example
prediction=model.predict(x_test[:1])    #get prediction probabilities
predicted_label=prediction.argmax()     #find the most likely class

plt.imshow(x_test[0].reshape(28,28),cmap="gray")
plt.title("Prediction: " +str(predicted_label))
plt.axis("off")
plt.show()#CNNIMAGEPROCESSING
#1. import libraries
import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

#2. load dataset(MNIST is a built in data)
(x_train,y_train),(x_test,y_test)=tf.keras.datasets.mnist.load_data()
print((x_train,y_train),(x_test,y_test))

#3. normalize data(scale pixel values to 0-1)
x_train=x_train.astype("float32") / 255.0
x_test=x_test.astype("float32") / 255.0
#4. reshape data(CNN expects 3D: height,width,channels)
x_train=x_train.reshape(-1,28,28,1)     #-1 means "figure this dimension out automatically"
x_test=x_test.reshape(-1,28,28,1)       #1 is the no of channels

#5. build a simple CNN model
model=models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),  #convolution
    layers.MaxPooling2D((2,2)),  #pooling layer
    layers.Flatten(),    #flatten into 1D
    layers.Dense(64,activation='relu'), #fully connected layer
    layers.Dense(10,activation='softmax') #output layer (10 classes)
])

#6. compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#7. train the model
history=model.fit(x_train,y_train,
                  epochs=5,
                  batch_size=64,    #faster training
                  validation_data=(x_test,y_test),
                  verbose=1)    #shows progress bar

#8. evaluate on test data
test_loss,test_acc=model.evaluate(x_test,y_test,verbose=0)
print("Test Accuracy:",round(test_acc*100,2),"%")

#9. predict example
prediction=model.predict(x_test[:1])    #get prediction probabilities
predicted_label=prediction.argmax()     #find the most likely class

plt.imshow(x_test[0].reshape(28,28),cmap="gray")
plt.title("Prediction: " +str(predicted_label))
plt.axis("off")
plt.show()