import Model
import Database
import DirectoryManager





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