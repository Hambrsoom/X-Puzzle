from pprint import pprint

def getSearchPath(closedArr, algoType, puzzleNumber):
    print("Search Path")
    
    fileName = "output/" + str(puzzleNumber) + "_" + algoType + "_search" +".txt"

    file = open(fileName, "w")

    for node in reversed(closedArr):
        if algoType == "ucs":
            gn = node["gn"]
            hn = 0
            fn = 0
        elif algoType == "gbfs":
            gn = 0
            hn = node["hn"]
            fn = 0
        elif algoType == "astar":
            gn = node["gn"]
            hn = node["hn"]
            fn = node["fn"]
        currentState = node["currentState"]

        file.write(str(fn) + " " + str(gn) + " " + str(hn) + " " + listToString(currentState) + "\n")
    
    file.close()


def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele + " "
    
    # return string   
    return str1 