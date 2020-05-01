# -*- coding: utf-8 -*-
"""
G2M : Ganttproject csv file to Mermaid html Converter
V20181215
by Dymaxion.kim@gmail.com
"""

#import easygui
import os
import csv
from tkinter import filedialog
from tkinter import *

# Select a csv file to read.
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
InputFileName = root.filename

# Make the output file name.
SplitFileName = os.path.splitext(InputFileName)
OutputFileName = SplitFileName[0] + '.html'

# Read data from the csv file.
file1 = open(InputFileName, 'r', encoding='utf-8')
reader = csv.reader(file1)
Data=[]
for line in reader:
    Data.append(line)
file1.close()

# Size of Data
y=len(line)-1
x=len(Data)-1

# Find headers using actualy.
for index in range(0,y):
    if Data[0][index]=="ID":
        ID=index
    elif Data[0][index]=="이름":
        NAME=index
    elif Data[0][index]=="시작일":
        START=index
    elif Data[0][index]=="종료일":
        FINISH=index
    elif Data[0][index]=="완료":
        STATUS=index

# Make Content to output
Content = []
Content.append("<html>")
Content.append("<script src='https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.0.0-rc.2/mermaid.min.js'></script>")
Content.append("<script>mermaid.initialize({startOnLoad:true});</script>")
Content.append("<div class='mermaid'>")
Content.append("gantt")
Content.append(" title 프로젝트 일정계획")
Content.append(" dateFormat  YYYY-MM-DD")
Content.append(" axisFormat %Y%m%d")
LC = len(Content)-1
#ContentTemp = []

for index in range(1,x):
    if not (Data[index][NAME])[0:2]=='  ':
        Content.append(' section ' + Data[index][NAME])
    elif (Data[index][NAME])[0:2]=='  ':
        ContentTemp = '  ' + Data[index][NAME] + ' : '
        if Data[index][START] == Data[index][FINISH]:
            ContentTemp = ContentTemp + 'crit,'
        if Data[index][STATUS] == '100':
            ContentTemp = ContentTemp + 'done,'
        elif not Data[index][STATUS] == '0':
            ContentTemp = ContentTemp + 'active,'
        #ContentTemp = ContentTemp + Data[index][ID] + ',' + Data[index][START]
        ContentTemp = ContentTemp + Data[index][START]
        if not Data[index][START] == Data[index][FINISH]:
            ContentTemp = ContentTemp + ',' + Data[index][FINISH]
        Content.append(ContentTemp)

Content.append("</div>")
Content.append("</html>")


# Output
file2 = open(OutputFileName, mode='wt', encoding='utf-8')
for line2 in Content:
    file2.write(''.join(line2)+'\n')
file2.close()

# Open the output file.
os.startfile(OutputFileName) # Web Browser
os.system('notepad '+OutputFileName) # Windows notepad
