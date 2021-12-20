from ImageModel import ImageModel
import Database

#define a class named model with a constructor and a method named train
class Model:
    MODEL_NAME = 'model.h5'
    def __init__(self, config, folder):
        self.config = config
        self.modelImage1 = ImageModel(shape = [1712, 720, 3], model = None)
        self.modelImage2 = None
        self.modelText = None
        self.model_path = folder
        self.database = Database.Database(folder, config["model_name"])



    def train():
        pass
    
    def predict(self, image):
        model1 = self.modelImage1.predict(image)

        result = model1
        return bool((result[0]>result[1]))
    
    def update_image_feedback(self, image, feedback):
        print("Updating image feedback")
        print(feedback)
        print(image)
        #self.database.update_image_feedback(image, feedback)