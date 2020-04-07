#Sean McGeachie
maleNames = ['Baptista','Petruchio','Gremio','Hortensio','Lucentio','Vincentio',
             'Tranio','Biondello','Grumio','Curtis','Nathaniel','Phillip',
             'Joseph','Nicholas','Peter', 'Tailor', 'Haberdasher','Officer']

femaleNames = ['KATHERINE','BIANCA', 'widow']

filePath = r"C:\Users\Sean\OneDrive\Documents\Uni\CS108\Plays\FolgerDigitalTexts_TXT_Complete\Shr.txt"
#read play into String array
global playArray
playArray = []
#this will need to be the directory where you keep .txt of play
with open(filePath) as myFile:
    for line in myFile:
        playArray.append(line)


#function will return the number of male lines
def findMaleLines():
    maleLines = 0
    maleLen = len(maleNames)
    for line in playArray:              #loop through every line in play
        for i in range(maleLen):        #loop through maleNames array
            if maleNames[i].upper() in line:
                maleLines += 1
    return maleLines

#function will return number of female lines 
def findFemaleLines():
    femaleLines = 0
    femaleLen = len(femaleNames)
    for line in playArray:              #loop through every line in play
        for i in range(femaleLen):      #loop through femaleNames array
            if femaleNames[i].upper() in line:
                femaleLines += 1
    return femaleLines

maleLines = findMaleLines()
femaleLines = findFemaleLines()

print("female lines: " + str(femaleLines))
print("male lines: " + str(maleLines))


#plot graph

import matplotlib.pyplot as plt

def plotBarGraph(x, y):
    plt.bar(x,y)
    plt.title("Number of Male vs Female Lines")

plotBarGraph(["Male Lines (" + str(maleLines) + ")" ,"Female Lines (" + str(femaleLines) + ")"],[maleLines,femaleLines])
plt.savefig(filePath + 'male_vs_female_lines.pdf')


#x = [1,2]
#y = [femaleLines, maleLines]

#plt.bar(x,y)

#plt.show()





        
