from ModelController import ModelController
import csv
import random
import pathlib
import PIL
import numpy as np
from sklearn.model_selection import train_test_split

mc = ModelController()

mc.activate_project("zhangai")

print(mc.active_project)

mc.activate_model("model0")

def train(X, Y):
    #convert the lists to numpy arrays
    X = np.array(X)
    Y = np.array(Y)

    #split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    #get only the first 10 images and labels
    X_train = X_train[:10]
    Y_train = Y_train[:10]

    print("initiating training")
    print(X_train.shape)
    print(Y_train.shape)
    #train the model
    mc.update_model_bulk(X_train, Y_train)

    #evaluate the model
    mc.model.modelImage1.model.evaluate(X_test, Y_test)



#open the csv file at "../database/database_test.csv"
with open("../database/database_test.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    
    #randomize the order of the rows
    rows = list(reader)
    random.shuffle(rows)


    X = []
    Y = []

    images_added = 0
    runs = 0
    #for each row
    for row in rows:
        print("row: " + str(runs*100+images_added)+ " of " + str(len(rows)))
        if images_added >= 100:
            train(X, Y)
            X = []
            Y = []
            images_added = 0
            runs += 1
        #get the project
        project = row[0]
        #get the image
        image = row[1]
        #get the label
        label = row[2]

        #get the image path
        image_path = pathlib.Path("../projetos") / project / "dataloss"
        path = sorted((image_path).glob("*/"+image+"*.*"))

        image_after = PIL.Image.open(path[0])
        image_after_table = np.array(image_after)
        image_before = PIL.Image.open(path[1])
        image_before_table = np.array(image_before)

        
        #diff between the images
        diff = image_after_table - image_before_table
        
        #remove the alpha channel
        diff = diff[:,:,:3]

        #normalize the images
        new_image = diff/255

        X.append(new_image)
        if label == "False Positive":
            Y.append([0,1])
        else:
            Y.append([1,0])
        images_added += 1
        



