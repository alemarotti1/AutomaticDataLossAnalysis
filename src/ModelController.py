import Model
import Database
import DirectoryManager
import os
import json





class ModelController:

    def __init__(self):
        config = []
        self.model = Model.Model(config=config)
    
    def startModel(self):
        #self.model.start()
        #print("oi")
        pass
    
    def get_projects(self):
        varDir = DirectoryManager.get_all_projects()
        return [y.name for y in varDir]


    def get_project_data(self, project):
        if(not os.path.isfile(DirectoryManager.get_project_directory()/project/"state.json")):
            file = open(DirectoryManager.get_project_directory()/project/"state.json", "w+")
            #trasform from json to list
            list = DirectoryManager.get_list_from_project(project)
            for x in list:
                #create dict
                dict = {"file": x, "evaluation": -1, "state": "unknown"}
                #write dict to file
                file.write(json.dumps(dict))

        else:
            file = open(DirectoryManager.get_project_directory()/project/"state.json", "w+")
            #trasform from json to list
            data = json.load(file)
        return 
