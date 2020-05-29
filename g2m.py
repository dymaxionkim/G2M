# -*- coding: utf-8 -*-
"""
G2M : Ganttproject csv file to Mermaid html Converter
V20200529
by Dymaxion.kim@gmail.com
"""

import csv

# Input file name (csv file)
InputFileName = "gantt.csv"

# Output file name (html file)
OutputFileName = "gantt.html"

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

# Combine NAME+STATUS
for index in range(1,x):
    Data[index][NAME] = Data[index][NAME] + ' (' + Data[index][STATUS] + '%)'

# Make Content to output
Content = []
Content.append("<html>")
Content.append("<script src='https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.5.1/mermaid.min.js'></script>")
#Content.append("<script src='mermaid.min.js'></script>")
Content.append("<script>mermaid.initialize({startOnLoad:true});</script>")
Content.append("<div class='mermaid'>")
Content.append("gantt")
Content.append(" title 프로젝트 일정계획")
Content.append(" dateFormat YYYY-MM-DD")
Content.append(" axisFormat %Y%m%d")
LC = len(Content)-1

for index in range(1,x):
    if not (Data[index][NAME])[0:2]=='  ':
        Content.append(' section ' + Data[index][NAME])
    elif (Data[index][NAME])[0:2]=='  ':
        ContentTemp = '  ' + Data[index][NAME] + ' : '
        if Data[index][START] == Data[index][FINISH]:
            ContentTemp = ContentTemp + 'milestone,' + Data[index][START] + ','
        if Data[index][STATUS] == '100':
            ContentTemp = ContentTemp + 'done,'
        elif not Data[index][STATUS] == '0':
            ContentTemp = ContentTemp + 'active,'
        ContentTemp = ContentTemp + Data[index][START]
        if not Data[index][START] == Data[index][FINISH]:
            ContentTemp = ContentTemp + ',' + Data[index][FINISH]
        Content.append(ContentTemp)

Content.append("</div>")
Content.append("</html>")

# Output html file
file2 = open(OutputFileName, mode='wt', encoding='utf-8')
for line2 in Content:
    file2.write(''.join(line2)+'\n')
file2.close()

