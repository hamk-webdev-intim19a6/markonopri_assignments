import re
from datetime import datetime
#Make a Python program, which can validate if the input string is a valid Finnish id number. You must calculate that the checksum is correct.
#Also output the birthdate of the person in format day.month.year and tell the gender (male/female) See https://fi.wikipedia.org/wiki/Henkil%C3%B6tunnus 

# hetu muoto: pp kk vv y nnn t

# kirjaimia G, I, O, Q, Z ei käytetä.

totalInput = []
nnn = []
ppkkvv = []
y = []
t = []


userInput = input("Please type 11 character long string: \n")


totalInput.append(userInput)
ppkkvv.append(userInput[0:6])
y.append(userInput[6])
nnn.append(userInput[7:10])
t.append(userInput[10])


jakojaannos = userInput[0:6] + userInput[7:10]


print("\nLists updated...\n")

def isCorrect(x):
    regexp = "^\d{6}[+-A]\d{3}[a-zA-Z0-9]$"
    match = re.search(regexp, x)
    
    if match:
        print("your input match")
    else:
        print("Your input don't match!")
        exit()

# y = vuosisadantunnus ( + = 1800luku     - = 1900-luku    A = 2000-luku)

def letscheckYnumber(z):
    if z == '+':
        print("1800-luvulla syntynyt")
    elif z == '-':
        print("1900-luvulla syntynyt")
    elif z == 'a':
        print("2000-luvulla syntynyt")
    else:
        print("Invalid character")


# ppkkvv = syntymäaika


def personBirthday(day):
    date_data = datetime.strptime(day, '%d%m%y' )
    print("Person birthday: ", date_data.strftime('%d/%m/%y'))

# t tarkistusmerkki t = ppkkvvnnn % 31, joka on 0-30 väliltä. Tarkista taulukosta tulos. 
# kirjaimia G, I, O, Q, Z ei käytetä.

def tarkistusMerkki(bigOne):
    result = int(bigOne) % 31
    Ycharacter = ''
    if result == 0:
        Ycharacter = '0'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 1:
        Ycharacter = '1'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 2:
        Ycharacter = '2'
        print("Tarkistusmerkki on: ", Ycharacter)    
    elif result == 3:
        Ycharacter = '3'
        print("Tarkistusmerkki on: ", Ycharacter)    
    elif result == 4:
        Ycharacter = '4'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 5:
        Ycharacter = '5'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 6:
        Ycharacter = '6'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 7:
        Ycharacter = '7'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 8:
        Ycharacter = '8'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 9:
        Ycharacter = '9'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 10:
        Ycharacter = 'A'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 11:
        Ycharacter = 'B'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 12:
        Ycharacter = 'C'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 13:
        Ycharacter = 'D'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 14:
        Ycharacter = 'E'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 15:
        Ycharacter = 'F'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 16:
        Ycharacter = 'H'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 17:
        Ycharacter = 'J'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 18:
        Ycharacter = 'K'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 19:
        Ycharacter = 'L'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 20:
        Ycharacter = 'M'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 21:
        Ycharacter = 'N'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 22:
        Ycharacter = 'P'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 23:
        Ycharacter = 'R'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 24:
        Ycharacter = 'S'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 25:
        Ycharacter = 'T'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 26:
        Ycharacter = 'U'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 27:
        Ycharacter = 'V'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 28:
        Ycharacter = 'W'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 29:
        Ycharacter = 'X'
        print("Tarkistusmerkki on: ", Ycharacter)
    elif result == 30:
        Ycharacter = 'Y'
        print("Tarkistusmerkki on: ", Ycharacter)
    else:
        print("t character invalid")


# nnn on yksilönumero. Naisilla parillinen ja miehillä pariton. [002-899] {900-999 käytetään tilapäiskäytössä}
def privateNumber(u):
    privatenamber = int(u)
    statusM = "mies"
    statusN = "nainen"
    if privatenamber % 2 == 0:
        print("yksilönumeron perusteella henkilö on: ", statusN)
    else:
        print("yksilönumeron perusteella henkilö on: ", statusM)
    


isCorrect(userInput)
letscheckYnumber(y[0])
personBirthday(ppkkvv[0])
tarkistusMerkki(jakojaannos)
privateNumber(nnn[0])




