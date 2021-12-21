import tensorflow as tf


class ImageModel:
    def __init__(self, shape, model=None):
        if model is None:
            weights = 'imagenet'
            # 2 classes on our classifier
            n_classes = 2
            # Dimensions from the image after being resized
            shape = shape

            trained_model = tf.keras.applications.xception.Xception(
                            include_top=False,
                            weights=weights,
                            input_shape=shape,
                            pooling='max'
                            )
                            
            self.model = tf.keras.Sequential()
            self.model.add(trained_model)
            self.model.add(tf.keras.layers.Flatten())
            self.model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))
            opt = tf.keras.optimizers.Adam(learning_rate=0.01)
            self.model.compile(loss='categorical_crossentropy', optimizer=opt)
        else:
            self.model = self.load_model(model)
        

    def predict(self, image):
        print("##############################")
        print("Predicting image: shape = {}".format(image.shape))
        
        image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
        predict = self.model.predict(image)
        print("Prediction: {}".format(predict))
        print("##############################")
        return [predict[0][0], predict[0][1]]
    
    def update_weights(self, image, target):
        self.model.fit(image, target, epochs=2, verbose=0)
    
    def update_image_bulk(self, image_list, prediction_list):
        self.model.fit(image_list, prediction_list, epochs=100, verbose=0)
    
    def save_model(self, path):
        self.model.save(path)
    
    def load_model(self, path):
        self.model = tf.keras.models.load_model(path)
