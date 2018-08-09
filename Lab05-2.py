"""
1)	Create an application that uses a dictionary to hold the following data:
Id	Name	Email
1	Bob Smith	BSmith@Hotmail.com
2	Sue Jones	SueJ@Yahoo.com
3	Joe James	JoeJames@Gmail.com

2)	Add code that lets users appends a new row of data.
3)	Add a loop that lets the user keep adding rows.
4)	Ask the user if they want to save the data to a file when they exit the loop.
5)	Save the data to a file if they say 'yes'

"""

#2)	Add code that lets users appends a new row of data.
dicRow1 = {"ID":"1","Name": "Bob Smith", "Email":"BSmith@Hotmail.com"}
dicRow2 = {"ID":"2","Name":"Sue Jones", "Email": "SueJ@Yahoo.com"}
dicRow3 = {"ID":"3","Name" :"Joe James","Email":"JoeJames@Gmail.com"}
lstTable = [dicRow1, dicRow2, dicRow3]
#2)	Add code that lets users appends a new row of data.
#3)	Add a loop that lets the user keep adding rows.
while(True):
    intID = (int(input("Enter an ID:" )))
    strName = (input("Enter an name:" ))
    strEmail = (input("Enter an email:" ))
    #lstNewRow = [intID, strName, strEmail] - becomes new dictionary
    dicNewRow = {"ID":intID,"Name":strName,"Email":strEmail}
    lstTable.append(dicNewRow)
    if(input("Type exit to end: ").lower() == 'exit'): break
#4)	Ask the user if they want to save the data to a file when they exit the loop.
#5)	Save the data to a file if they say 'yes'


strSaveToFile = input("Would you like to save this data to a file:? (y/n)?")
if (strSaveToFile.lower() == "y"):
    objFile = open("Lab05-3Data.txt", "w")
    for row in (lstTable):
        strRow = str(row)
        objFile.write(strRow)
        objFile.write("\n")
    objFile.close
    print("The following data\n\r", lstTable, "\n\rSaved!")
else:
    print("Data not saved!")

