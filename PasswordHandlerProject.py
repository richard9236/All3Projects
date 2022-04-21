
import time
import random
from cryptography.fernet import Fernet
#import pyperclip as pc

# from cryptography.fernet import Fernet

remoteFileName = "Binder.txt"
file = open(remoteFileName, "a")
file = open(remoteFileName, "r")
def gettInput():
    x = input(": ")
    if "|" in x:
        print("Illegal character detected: |")
        return False
    if ";;" in x:
        print("Illegal character detected: ;;")
        return False
    return x 
def view(nameTB, valueTB):
    remoteLen = len(nameTB)
    if remoteLen != len(valueTB):
        print("ERROR:030D")
    for i in range(remoteLen):
        print(str(i +1)+"| "+ nameTB[i] +": " + valueTB[i])

combos = [
    "A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "!", "@", "$", ",", ";", "^", "<", ">", "&", "^", "|"
]
comboCombo = []
currentDataStore = False
key = False
currentPassword = False
currentDataStoreOFSC = file.read()

currentDataStoreTB = []
currentDataStoreTBValues = []

def generateCombo(password):
    passwordKey = gettPasswordKey(password)
    global combos
    global comboCombo
    bs = []
    for i in range(len(combos)):
        if i >= passwordKey:
            bs.append(combos[i])
    for i in range(len(combos)):
        if i < passwordKey:
            bs.append(combos[i])
    comboCombo = bs
    
def gettPasswordKey(password):
    remoteInt = 0
    for i in range(len(combos)):
        for ii in range(len(password)):
            if combos[i] == password[ii]:
                remoteInt = remoteInt + i
    
    remoteInt = int(remoteInt / len(password))
    remoteInt = clamp(remoteInt, 0, len(combos) -1)
    return remoteInt
def gettRandomShit(intAmount):
    global combos
    remoteString = ""
    for i in range(intAmount):
        remoteString = remoteString + combos[random.randint(0, len(combos) -1)]
    
    return remoteString

def wait(remoteFloat):
    #time.sleep(remoteFloat)
    s = 1

def encryptR(password, targetString):
    generateCombo(password)
    remoteString = ""
    for i in range(len(targetString)):
        x = 3
        for ii in range(len(combos)):
            if combos[ii] == targetString[i]:
                x = ii
                break
        
        remoteString = remoteString +comboCombo[x] + gettRandomShit(5)
    
    return remoteString
def decryptR(password, targetString):
    generateCombo(password)
    remoteBS = []
    
    remoteString = ""
    for i in range(0, len(targetString), 6):
        remoteBS.append(targetString[i])

    for i in range(len(remoteBS)):
        for ii in range(len(comboCombo)):
            if comboCombo[ii] == remoteBS[i]:
                remoteString = remoteString +combos[ii]
    print("Decrypting according to current 0 index...")
    return remoteString
def NewCommandLine():
    for i in range(50):
        print(" ")
def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)
def update():
    global currentDataStoreTB
    global currentDataStoreTBValues
    global file
    
    remoteString = "CORRECT|||"
    remoteLen = len(currentDataStoreTB)
    remoteInt = remoteLen -1
    file.close()
    file = open(remoteFileName, "w")
    
    for i in range(remoteLen):
        remoteString = remoteString +currentDataStoreTB[i] +"|" + currentDataStoreTBValues[i]
        if (i != remoteInt):
            remoteString = remoteString +"||"
    
    
    remoteString = encryptR(currentPassword, remoteString)
    file.write(remoteString)
    file.close()
def gettIntInput():
    remoteBool = True
    while (remoteBool == True):
        x = gettInput()
        if x.lower() == "back":
            print("?")
            return -1
    
        try:
            x = (int(x))
        except:
            print("["+x+ "] is not an integer.")
            print("Please enter it again, or [back] to quit")
        else:
            remoteBool = False
            break
    
    x = int(x) -1
    return x
remoteInt = 5 # number of tries
while remoteInt != 69:
    #write("favorite number", str(x))
    x = False
    if currentDataStoreOFSC== "":
        key = Fernet.generate_key()
        print("This is a blank file.")
        wait(1)
        print("Indicating this is your first time")
        wait(1)
        print("Enter a password, and do not forget it")
        x = gettInput()
        print("Enter it again")
        xx = gettInput()
        if (x == xx):
            remoteBool = 1
            for i in range(len(x)):
                if (x[i] == "|"):
                    remoteBool = 0
                    break
            if (remoteBool == 1):
                currentPassword = x
                generateCombo(x)
                currentDataStoreOFSC = "CORRECT|||Example_Phone_Number|305-583-1961||Example_Address|123 blue street"
                
                currentDataStoreOFSC = encryptR(currentPassword, currentDataStoreOFSC)
                
                NewCommandLine()
                print("Success")
            else:
                print("Invalid characters in password.")
                continue
        else:
            NewCommandLine()
            print("Passwords do not match.")
            continue
    else:
        print("Enter master password")
        x = gettInput()
    if (1+1 == 2):
        generateCombo(x)
        currentDataStore = decryptR(x, currentDataStoreOFSC)
            
        if "CORRECT|||" in currentDataStore:
            remoteInt = 69
            currentDataStore = currentDataStore.split("CORRECT|||")
            
            currentDataStore = currentDataStore[1]
            currentDataStore = currentDataStore.split("||") 
            
            for i in range(len(currentDataStore)):
                remoteTB = currentDataStore[i].split("|")
                currentDataStoreTB.append(remoteTB[0])
                currentDataStoreTBValues.append(remoteTB[1])
                
            break
        else:
            NewCommandLine()
            print("Incorrect Password")
    else:
        remoteInt = remoteInt-1
        if remoteInt <= 0:
            print("You entered the password incorrectly too many times.")
            wait(1)
            print(remoteFileName+" is facing deletion...")
            #x = open(remoteFileName, "d")
            break
        print("Incorrect, "+ str(remoteInt)+" tries left.")
lastStepWasSave = False

if remoteInt == 69:
    #nice
    NewCommandLine()
    while True:
        if (lastStepWasSave == False):
            view(currentDataStoreTB, currentDataStoreTBValues)
        
        print("Enter command")
        remoteInput = gettInput()
        remoteInput = remoteInput.lower()
        if (remoteInput) == "a":
            lastStepWasSave = False
            
            print("Enter the name of data")
            typeOfData = gettInput()
            print("Enter the value of "+ str(typeOfData))
            valueOfData = gettInput()
            currentDataStoreTB.append(typeOfData)
            currentDataStoreTBValues.append(valueOfData)
            
        elif remoteInput == "s":
            print("attempting to save data...")
            lastStepWasSave = True
            update()
            print("Success")
        elif remoteInput == "c":
            view(currentDataStoreTB, currentDataStoreTBValues)
            print("--Enter the index of a value you wish to copy to clipboard--")
            x = gettIntInput()
            if (x != "NULL"):
                x = clamp(x, 0, len(currentDataStoreTB) -1)
                print(currentDataStoreTB+ " selected...")
                print(currentDataStoreTBValues[x]+" has been copied to your clipboard.")

        elif remoteInput == "d":
            lastStepWasSave = False
            view(currentDataStoreTB, currentDataStoreTBValues)
            print("--Enter the index of a value you wish to delete--")
            x = gettIntInput()
            if (x != "NULL"):
                x = clamp(x, 0, len(currentDataStoreTB) -1)
                print("Did you mean to clear " +currentDataStoreTB[x]+"?")
                print("y = yes")
                xx = gettInput()
                
                if (xx == "y"):
                    currentDataStoreTB.pop(x)
                    currentDataStoreTBValues.pop(x)
        elif remoteInput == "q" or remoteInput == "quit" or remoteInput == "stop":
            if (lastStepWasSave == True):
                break
            else:
                print("Last step was not save command")
                wait(1.5)
                print("Please make sure to save before you exit")
            lastStepWasSave = True
        elif remoteInput == "help":
            print("--COMMAND_LIST--")
            print("a - add a new set of data")
            print("c - copy a password/value to your clipboard")
            print("d - delete a line of data")
            print("s - save the current data written")
            print("q - safely close, will warn if you have not saved yet")
        else:
            print("Unknown command: "+ remoteInput)
            print("Try: help")
            
        
        