import threading
import eel
#import concurrent.futures
from ModelController import ModelController


import Gui

mc = ModelController()

@eel.expose
def get_projects():
    return mc.get_projects()

@eel.expose
def get_project_data(project):
    return mc.get_project_data(project)

@eel.expose
def receive_feedback(img_name,feedback):
    return mc.get_feedback(img_name, feedback)

@eel.expose
def activate_project(project):
    var = mc.activate_project(project)
    return var

@eel.expose
def activate_model(model):
    print("Activating model: " + model)
    try:
        mc.activate_model(model)
        return True
    except Exception as e:
        print("Error activating model: " + str(e))
        return False

@eel.expose
def get_images(image_name):
    return mc.get_images(image_name)

@eel.expose
def create_model():
    return mc.create_model()

@eel.expose
def get_model_data(model):
    return mc.get_model_data(model)

@eel.expose
def get_models():
    return mc.get_models()

@eel.expose
def get_image(image):
    print("requested image: " + image)
    return mc.get_images(image)

@eel.expose
def update_image(image, data):
    try:
        return mc.get_feedback(image, data)
    except Exception as e:
        print(e)
        return False 

def predict(image):
    return mc.predict(image)

@eel.expose
def start_prediction():
    print("##############################################################")
    print("Starting prediction")
    thread = threading.Thread(target=mc.predict_model, args=(), daemon=True)
    thread.start()

@eel.expose
def stop_prediction():
    print("Stopping prediction")
    mc.running = False

@eel.expose
def get_updated_model():
    return mc.model.database.database


def main():
    # mc = ModelController()
    # modelThread = threading.Thread(target=mc.startModel, args=(), daemon=True)
    # modelThread.start()

    guiThread = threading.Thread(target=Gui.startWebView, args=(), daemon=True)
    guiThread.start()
    
    
    #modelThread.join()
    guiThread.join()




#a main that will run the program
if __name__ == '__main__':
    main()