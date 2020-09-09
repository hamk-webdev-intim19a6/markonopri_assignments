import json

# Constant dictionary, if file not found
obj1 = {
    "s": "Kissa", "v": "Kass"
}
obj2 = {
    "s": "Koira", "v": "Koer"
}
obj3 = {
    "s": "Aasi", "v": "Eesel"
}
obj4 = {
    "s": "Hevonen", "v": "Hobune"
}
obj5 = {
    "s": "Sammakko", "v": "Konn"
}     
# New dictionary where the new words will come.
objX = {"s": "", "v": ""}

# List got all dictionarys
alldata = [obj1, obj2, obj3, obj4, obj5, objX]


try:
    with open("test.json") as f:
        print(f.read())
        print("There is no data. App will use constant data. ")
except:
    with open("test.json", "w") as f:
        json.dump(alldata, f)
        print("Constant dictionary saved JSON format.")

# Function what will test if user input is in dictionary

def try_it(string):
    if string == obj1['s']:
        print(obj1['v'])
    elif string == obj2['s']:
        print(obj2['v'])
    elif string == obj3['s']:
        print(obj3['v'])
    elif string == obj4['s']:
        print(obj4['v'])
    elif string == obj5['s']:
        print(obj5['v'])
    elif string == objX['s']:
        print(objX['v'])
    else:
        print("Word not found. Please input a definition.")
        
        ifNotFound(string)

# Function for creating words to dictionary. And updating JSON.
def ifNotFound(first):
    sec = input("Input translation: ")

    objZ = {"s":first, "v":sec}
    objX.update(objZ)


    with open("test.json", "w") as f:
        json.dump(alldata, f)


print("## A simple dictionary app ##")

pick = ''


# While loop for the program
while (pick != 'q'):
    print("a) Search word")
    print("q) EXIT")
    

    pick = input("Make your pick...\n")

    if pick == 'a':
        print("--Searching word--\n")
        word = input("Input word: ")
        
        try_it(word)
        
            
    elif pick == 'q':
        print("Goodbye!")

    else:
        print("input error ER4576")

