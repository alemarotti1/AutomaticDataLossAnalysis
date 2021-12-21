from ImageModel import ImageModel
import Database

#define a class named model with a constructor and a method named train
class Model:
    MODEL_NAME = 'model.h5'
    def __init__(self, config, folder, state={""}):
        self.config = config
        self.modelImage1 = ImageModel(shape = [1712, 720, 3], model = None)
        self.modelImage2 = None
        self.modelText = None
        self.model_path = folder
        self.database = Database.Database(folder, config["model_name"])
        self.running = False
        self.no_of_verified = 0



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
        self.database.update_database(image, "Confirmed", feedback)

    def update_image_prediction(self, image, prediction):
        self.database.update_database(image, "Predicted" ,prediction)
    
    def predict_model(self):
        self.running = True
        #while self.running is true and there are images to be verified 
        while self.running and self.no_of_verified < len(self.database.database["file_list"]):
            print ("Verifying image")

            #get the image from the database
            image = self.database.database["file_list"][self.no_of_verified]

            #if the file status is different than 1
            if self.database.database["file_list"][self.no_of_verified]["state"] == "unknown":
                prediction = self.predict(image)
                self.database.update_database()

                

            self.no_of_verified += 1