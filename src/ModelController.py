import Model
import DirectoryManager
import json
import base64





class ModelController:

    def __init__(self):
        config = []
        self.model = None
        self.database = None
    
    def startModel(self):
        #self.model.start()
        #print("oi")
        pass
    
    def get_projects(self):
        varDir = DirectoryManager.get_all_projects()
        return [y.name for y in varDir]

    
    def activate_project(self, project):
        self.active_project = project
        return True
    
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
            self.model = Model.Model(config, model_folder)
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
