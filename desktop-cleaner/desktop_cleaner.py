import os #Allows us to interact with the os
import shutil #Allows us to copy, move, delete files/ folders

def createSubfolderIfNeeded(folderPath, subfolderName):
    subfolderPath = os.path.join(folderPath, subfolderName)
    if not os.path.exists(subfolderPath):
        os.makedirs(subfolderPath)
    return subfolderPath

def cleanFolder(folderPath):
    
    for filename in os.listdir(folderPath):
        if os.path.isfile(os.path.join(folderPath, filename)): #Checks if the path exists and the file is valid
            fileParts=filename.split('.')

            #Checks if the list has more than 1 item and that the filename doesnt start with a '.'
            subfolderName=f"{fileParts[-1].upper()} Files" if len(fileParts)>1 and not filename.startswith(".") else "Other Files"

            subfolderPath=createSubfolderIfNeeded(folderPath, subfolderName)

            filePath=os.path.join(folderPath, filename)
            newLocation=os.path.join(subfolderPath, filename)

            originalName = filename
            name, extension = os.path.splitext(filename) #Returns a tuple (root, .ext)
            counter=1

            while os.path.exists(newLocation):
                filename=f"{name} ({counter}){extension}"
                newLocation=os.path.join(subfolderPath, filename)
                counter+=1

            if not os.path.exists(newLocation):
                shutil.move(filePath, newLocation) #(src, des) Moves the file from the source to the destination
                print(f"Moved: {originalName} --> {subfolderName}")
            else:
                print(f"{originalName} already exists in {subfolderName}")
                

if __name__=="__main__":
    print("Desktop Cleaner Script is running...")
    folderPath=r"C:\Users\kanch\Downloads" #Add your folder path
    if os.path.isdir(folderPath): #Returns true if the given path is a directory
        cleanFolder(folderPath)
        print("Cleaning is complete!")
    else:
        print("Invalid folder path. Please ensure that the folder path is correct")
