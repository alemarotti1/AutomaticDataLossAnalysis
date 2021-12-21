import Model
import DirectoryManager
import json
import base64
import PIL
import numpy as np





class ModelController:

    def __init__(self):
        config = []
        self.model = None
        self.database = None
        self.running = False
        self.active_project = None
    
    def startModel(self):
        #self.model.start()
        #print("oi")
        pass
    
    def get_projects(self):
        varDir = DirectoryManager.get_all_projects()
        return [y.name for y in varDir]

    
    def activate_project(self, project):
        """ set the active project to the given project

        Arguments:
            project {str} -- name of the project to activate

        Returns:
            bool -- True if the project was activated, False otherwise

        """
        try:
            if (DirectoryManager.get_project_directory()/project).is_dir():
                self.active_project = project
                return True
        except Exception as e:
            print(e)
            return False
        return False
    
    def activate_model(self, model_name):
        """ activate a model for the active project

        Arguments:
            model_name {str} -- name of the model to activate

        Returns:
            bool -- True if the model was activated, False otherwise
        """
        try:
            model_folder = DirectoryManager.get_project_directory()/self.active_project/"modelos"/model_name
            config = json.load(open(model_folder/"state.json"))
            print("creating model "+ model_name+ " with folder: " + str(model_folder))
            config = {"model_name": model_name, "number_of_rights": config["number_of_rights"], "number_of_wrongs": config["number_of_wrongs"], "number_of_unknowns": config["number_of_unknowns"]}
            self.model = Model.Model(config, model_folder)
            print("model created ")
        except Exception as e:
            print(e)
            return False
        return True

    
    def get_feedback(self, img_name, feedback):
        try:
            self.model.update_image_feedback(img_name, feedback)
            return True
        except Exception as e:
            print(e)
            return False
    
    def get_images(self, image_name):
        return_val = {"before": "", "after": "", "view": ""}
        path = sorted((DirectoryManager.get_project_directory()/self.active_project/"dataloss").glob("*/"+image_name+"*.*"))
        print(image_name+"*.*")
        print(path)
        return_val["after"] = base64.b64encode(open(path[0], "rb").read()).decode("utf-8")
        return_val["before"] = base64.b64encode(open(path[1], "rb").read()).decode("utf-8")
        return_val["view"] = open(path[2], "r").read()

        return return_val
    
    def get_models(self):
        """ get the list of models for the active project

        Returns:
            list -- list of models
        """
        if(self.active_project is None):
            return []
        #get all folders from (DirectoryManager.get_project_directory()/self.active_project/"modelos")
        model_folder_list = [x.name for x in (DirectoryManager.get_project_directory()/self.active_project/"modelos").iterdir() if x.is_dir()]
        model_list = []

        for model in model_folder_list:
            #get the number of rights, wrongs and unknowns
            model_folder = DirectoryManager.get_project_directory()/self.active_project/"modelos"/model
            state = json.load(open(model_folder/"state.json"))
            state["name"] = model
            model_list.append(state)
        return model_list


    def create_model(self):
        """ create a new model for the active project 

        Returns:
            bool -- True if the model was created, False otherwise
        """
        try:
            model_num = len(self.get_models())
            model_name = "model"+str(model_num)

            #create model folder
            model_folder = DirectoryManager.get_project_directory()/self.active_project/"modelos"/model_name
        
            model_folder.mkdir()
            
            config = {"model_name": model_name, "number_of_rights": 0, "number_of_wrongs": 0, "number_of_unknowns": 0}
            self.model = Model.Model(config, model_folder)

        except Exception as e:
            print(e)
            return False
        return True

    def predict(self, image):
        """ predict the type of the image

        Arguments:
            image {str} -- image to predict
        
        Returns:
            str -- the prediction
        """

        return_val = {"before": "", "after": "", "view": ""}
        

        new_image = self.convert_image_path(image)


        result = self.model.predict(new_image)
        print("result: "+str(result))
        print(type(result))
        
        
        return result
    
    
    def predict_model(self):
        """ predict the type of the images in the active model

        Returns:
            true if the prediction was successful, false otherwise
        """

        self.running = True

        image_list = self.model.database.database
        for image in image_list["file_list"]:
            if not self.running:
                break
            if image["state"] != "Verified":
                image_array = self.convert_image_path(image["file"])
                result = self.model.predict(image_array)
                self.model.update_image_prediction(image["file"], result)
        
        self.running = False
    
    
    def convert_image_path(self, image_name):
        """ convert the image path to the image files

        Arguments:
            image_name {str} -- image name to convert

        Returns:
            numpy array -- image converted to numpy array
        """
        path = sorted((DirectoryManager.get_project_directory()/self.active_project/"dataloss").glob("*/"+image_name+"*.*"))
        print(image_name+"*.*")
        print(path)

        image_after = PIL.Image.open(path[0])
        image_after = image_after.resize((int(image_after.width//2), int(image_after.height//2)), PIL.Image.ANTIALIAS)
        image_after_table = np.array(image_after)
        image_before = PIL.Image.open(path[1])
        image_before = image_before.resize((int(image_before.width//2), int(image_before.height//2)), PIL.Image.ANTIALIAS)
        image_before_table = np.array(image_before)

        
        #diff between the images
        diff = image_after_table - image_before_table
        
        #remove the alpha channel
        diff = diff[:,:,:3]

        #normalize the images
        new_image = diff/255
        return new_image
    
    def update_model_bulk(self, image_list, result_list):
        """ update the model with a bulk of images

        Arguments:
            image_list {list} -- list of image names
            result_list {list} -- list of results
        """
        self.model.update_image_bulk(image_list, result_list)