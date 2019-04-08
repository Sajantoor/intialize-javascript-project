import os
import sys
projectFolder = ""
projectName = ""
path = os.getcwd()
print ("The current working directory is %s" % path)

def getFolderName():
    print("What do you want your project to be called? \n")
    value = input()
    main(value)

def makeFolder(value):
    os.mkdir(value)
    os.chdir(os.getcwd() + "\\" + value)
    fileName = "index." + value
    f = open(fileName, "w")
    os.chdir(projectFolder)

def main(value):
    try:
        os.mkdir(value)
        global projectName
        projectName = value
    except:
        print("Error, check if this folder already exists in this directory.")
        projectName = ""
        getFolderName()
        return

    os.chdir(os.getcwd() + "\\" + projectName)
    global projectFolder
    projectFolder = os.getcwd()
    makeFolder("html")
    makeFolder("js")
    makeFolder("css")

getFolderName()
