import urllib.request
import os.path

print("### This is a simple URL data program ###\n")

# User inputs: URL, PATH and Filename
userInputURL = input("Input URL here: \n")
pathInput = input("Input path: \n")
fileName = input("Input file name: \n")

# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen(userInputURL)

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and write it to path
data = webUrl.read()
with open(fileName, "w") as f:
    file_path = os.path.join(pathInput, fileName)
    if not os.path.isdir(pathInput):
        os.mkdir(pathInput)
    file = open(file_path, "w")
    f.write(str(data))