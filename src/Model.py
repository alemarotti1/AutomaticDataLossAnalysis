import ImageModel
import Database

#define a class named model with a constructor and a method named train
class Model:
    MODEL_NAME = 'model.h5'
    def __init__(self, config, folder):
        self.config = config
        self.modelImage1 = None
        self.modelImage2 = None
        self.modelText = None
        self.model_path = folder
        self.database = Database.Database(folder, config["model_name"])



    def train():
        pass
    
    def predict(self, image):
        
        return self.modelImage1.predict(image)
    
    def update_image_feedback(self, image, feedback):
        print("Updating image feedback")
        print(feedback)
        print(image)
        #self.database.update_image_feedback(image, feedback)