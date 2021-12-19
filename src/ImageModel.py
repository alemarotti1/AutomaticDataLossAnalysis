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
        else:
            self.model = model
    
    def predict(self, image):
        return self.model.predict(image)
    
    def update_weights_based_on_loss(self, image, loss):
        self.model.fit(image, loss)
    
    def save_model(self, path):
        self.model.save(path)
    
    def load_model(self, path):
        self.model = tf.keras.models.load_model(path)
