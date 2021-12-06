import threading
import concurrent.futures

#import ModelController
import Gui



def main():
    #modelThread = threading.Thread(target=ModelController.startModel, args=(), daemon=True)
    #modelThread.start()

    #guiThread = threading.Thread(target=Gui.startWebview, args=(), daemon=True)
    #guiThread.start()
    
    #modelThread.join()
    #guiThread.join()
    
    Gui.startWebView()




#create a main that will run the program
if __name__ == '__main__':
    main()