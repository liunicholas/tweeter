from yfinance import *
from graphics import *
from random import *
import numpy as np

def startGraph():
    gw = GraphWin("Stock Graph", 1440, 775)
    gw.setCoords(0, 0, 1440, 775)
    gw.setBackground("black")

    p1 = Point(50, 50)
    p2 = Point(1410, 50)
    line = Line(p1, p2)
    line.setFill("white")
    line.setOutline("white")
    line.draw(gw)

    p1 = Point(50, 50)
    p2 = Point(50, 745)
    line = Line(p1, p2)
    line.setFill("white")
    line.setOutline("white")
    line.draw(gw)

    return gw

def getStockName(win):
    text = Text(Point(700, 750), "Stock Name")
    text.setSize(30)
    text.setFill("white")
    text.setOutline("white")
    text.draw(win)
    textbox = Entry(Point(700, 700), 10)
    textbox.setFill("white")
    textbox.draw(win)

    while True:
        character = win.getKey()
        if character == "Return":
            stockName = textbox.getText()
            text.undraw()
            textbox.undraw()
            break

    return stockName

def drawGraphDeatils(win, stockName):
    text = Text(Point(110, 750), stockName.upper())
    text.setSize(30)
    text.setFill("white")
    text.setOutline("white")
    text.draw(win)

    text = Text(Point(110, 725), "Open:")
    text.setSize(20)
    text.setFill("white")
    text.setOutline("white")
    text.draw(win)

    text = Text(Point(110, 700), "Close:")
    text.setSize(20)
    text.setFill("white")
    text.setOutline("white")
    text.draw(win)

    text = Text(Point(110, 675), "Low:")
    text.setSize(20)
    text.setFill("white")
    text.setOutline("white")
    text.draw(win)

    text = Text(Point(110, 650), "High:")
    text.setSize(20)
    text.setFill("white")
    text.setOutline("white")
    text.draw(win)
    text = Text(Point(110, 625), "Date:")
    text.setSize(20)
    text.setFill("white")
    text.setOutline("white")
    text.draw(win)

def getData(stockName):
    stock = Ticker(stockName)
    hist = stock.history(period="max")

    openList = []
    closeList = []
    dateList = []
    for i in range(hist.shape[0]):
        line = hist.iloc[i]
        openList.append(line["Open"])
        closeList.append(line["Close"])
        dateList.append([hist.index[i].year,hist.index[i].month,hist.index[i].day])

    return openList, closeList, dateList

def getMinMax(openList, closeList):
    max1 = max(openList)
    max2 = max(closeList)
    maxVal = max([max1,max2])

    min1 = min(openList)
    min2 = min(closeList)
    minVal = min([min1,min2])

    return minVal, maxVal

def drawGraph(win, totalItems, maxVal, pixelPerDate, pixelPerDollar, dateList):
    TotalItems = ""
    for char in str(totalItems):
        if char != ".":
            TotalItems += char;
        else:
            break
    TotalItems = int(TotalItems)

    MaxVal = ""
    for char in str(maxVal):
        if char != ".":
            MaxVal += char;
        else:
            break
    MaxVal = int(MaxVal)

    for i in range(0,TotalItems,int(TotalItems/10)):
        text = Text(Point(i*pixelPerDate+50, 30), str(dateList[i][1])+"/"+str(dateList[i][2])+"/"+str(dateList[i][0]))
        text.setSize(15)
        text.setFill("white")
        text.setOutline("white")
        text.draw(win)

    for i in range(0,MaxVal,int(MaxVal/10)):
        text = Text(Point(25, i*pixelPerDollar+50), int(i))
        text.setSize(15)
        text.setFill("white")
        text.setOutline("white")
        text.draw(win)

def SortListInList(list):
    newList = []
    for i in range(len(list)):
        low = 0
        high = len(newList) - 1
        while low <= high:
            middle = int((high + low) / 2)
            if list[i][0] == newList[middle][0]:
                low = middle
                break
            elif list[i][0] > newList[middle][0]:
                low = middle + 1
            elif list[i][0] < newList[middle][0]:
                high = middle - 1

        newList.insert(low, list[i])

    return newList

def findClosestIndex(List, val):
    # List = np.asarray(List)
    # index = (np.abs(List - val)).argmin()
    # return index
    temp = []
    for item in List:
        temp.append(abs(val-item))

    return temp.index(min(temp))

def predictFutureProbability(openList, closeList, dateList):
    futureCloseList = list(closeList)
    futureOpenList = list(openList)
    futureDateList = list(dateList)
    differences = []
    for i in range(len(closeList)-50):
        differences.append([closeList[i+1]-closeList[i],closeList[i+49]-closeList[i+48]])

    differencesSorted = SortListInList(differences)
    #items per category
    ipc = int(len(differencesSorted)/100)
    predictionList = []
    for i in range(0,len(differencesSorted),ipc):
        signalTotal = 0
        # predictedTotal = 0
        optionsList = []
        for j in range(ipc):
            signalTotal += differencesSorted[j][0]
            # predictedTotal += differencesSorted[j][1]
            optionsList.append(differencesSorted[j][1])
        signalAvg = signalTotal/ipc
        # predictedAvg = predictedTotal/ipc
        predictionList.append([signalAvg,optionsList])

    valueList = []
    for i in range(len(predictionList)):
        valueList.append(predictionList[i][0])

    # print(valueList)

    for i in range(1000):
        currentDate = futureDateList[len(futureDateList)-1]
        currentOpen = futureOpenList[len(futureOpenList)-1]
        currentClose = futureCloseList[len(futureCloseList)-1]

        changeOpen = futureOpenList[len(futureOpenList)-1] - futureOpenList[len(futureOpenList)-2]
        changeClose = futureCloseList[len(futureCloseList)-1] - futureCloseList[len(futureCloseList)-2]

        count = 0
        for i in range(100):
            index = findClosestIndex(valueList,changeOpen)
            count += choice(predictionList[index][1])
        futureOpenList.append(count/100+currentOpen)

        count = 0
        for i in range(100):
            index = findClosestIndex(valueList,changeClose)
            count += choice(predictionList[index][1])
        futureCloseList.append(count/100+currentClose)

        year = currentDate[0]
        month = currentDate[1]
        day = currentDate[2]
        if day>30:
            month+=1
            day = 1
        if month>12:
            year+=1
            month = 1
        else:
            day+=1
        futureDateList.append([year,month,day])

    return futureOpenList, futureCloseList, futureDateList

def main():
    win = startGraph()
    stockName = getStockName(win)
    openList, closeList, dateList = getData(stockName)

    totalItemsInitial = len(dateList)

    openList, closeList, dateList = predictFutureProbability(openList, closeList, dateList)

    drawGraphDeatils(win, stockName)

    totalItems = totalItemsInitial
    totalItems = len(dateList)
    minVal, maxVal = getMinMax(openList, closeList)
    pixelPerDate = 1360.0/totalItems
    pixelPerDollar = 695.0/maxVal
    drawGraph(win, totalItems, maxVal, pixelPerDate, pixelPerDollar, dateList)

    low = 100000
    high = 0
    DRAWN = False
    text1 = Text(Point(180, 725), "")
    text2 = Text(Point(180, 725), "")
    text3 = Text(Point(180, 725), "")
    text4 = Text(Point(180, 725), "")
    text5 = Text(Point(180, 725), "")
    for i in range(0,totalItems,10):
        xVal = i*pixelPerDate+50
        yVal = (openList[i])*pixelPerDollar+50
        # print(xVal, yVal)
        point = Point(xVal, yVal)
        point.setFill("green")
        point.setOutline("green")
        point.draw(win)
        xVal = i*pixelPerDate+50
        yVal = (closeList[i])*pixelPerDollar+50
        # print(xVal, yVal)
        point = Point(xVal, yVal)
        point.setFill("red")
        point.setOutline("red")
        point.draw(win)

        if openList[i] < low:
            low = openList[i]
        if openList[i] > high:
            high = openList[i]
        if closeList[i] < low:
            low = closeList[i]
        if closeList[i] > high:
            high = closeList[i]

        text1.undraw()
        text1 = Text(Point(180, 725), "%.2f" % openList[i])
        text1.setSize(20)
        text1.setFill("white")
        text1.setOutline("white")
        text1.draw(win)

        text2.undraw()
        text2 = Text(Point(180, 700), "%.2f" % closeList[i])
        text2.setSize(20)
        text2.setFill("white")
        text2.setOutline("white")
        text2.draw(win)

        text3.undraw()
        text3 = Text(Point(180, 675), "%.2f" % low)
        text3.setSize(20)
        text3.setFill("white")
        text3.setOutline("white")
        text3.draw(win)

        text4.undraw()
        text4 = Text(Point(180, 650), "%.2f" % high)
        text4.setSize(20)
        text4.setFill("white")
        text4.setOutline("white")
        text4.draw(win)

        text5.undraw()
        text5 = Text(Point(190, 625), str(dateList[i][1])+"/"+str(dateList[i][2])+"/"+str(dateList[i][0]))
        text5.setSize(20)
        text5.setFill("white")
        text5.setOutline("white")
        text5.draw(win)

        if i>100:
            recentList = closeList[i-99:i+1]
            avg = sum(recentList) / len(recentList)
            xVal = i*pixelPerDate+50
            yVal = avg*pixelPerDollar+50
            point = Point(xVal, yVal)
            point.setFill("blue")
            point.setOutline("blue")
            point.draw(win)

        if i>20:
            recentList = closeList[i-19:i+1]
            avg = sum(recentList) / len(recentList)
            xVal = i*pixelPerDate+50
            yVal = avg*pixelPerDollar+50
            point = Point(xVal, yVal)
            point.setFill("yellow")
            point.setOutline("yellow")
            point.draw(win)

        if i>totalItemsInitial and DRAWN==False:
            p1 = Point(i*pixelPerDate+50, 50)
            p2 = Point(i*pixelPerDate+50, 770)
            line = Line(p1, p2)
            line.setFill("white")
            line.setOutline("white")
            line.draw(win)
            DRAWN=True;

    while True:
        userClick = win.getMouse()
        x = userClick.getX()
        pixelLength = x-50
        dateInPixel = int(pixelLength/pixelPerDate)

        maxVal = max(openList[:dateInPixel]+closeList[:dateInPixel])
        minVal = min(openList[:dateInPixel]+closeList[:dateInPixel])

        text1.undraw()
        text1 = Text(Point(180, 725), "%.2f" % openList[dateInPixel])
        text1.setSize(20)
        text1.setFill("white")
        text1.setOutline("white")
        text1.draw(win)

        text2.undraw()
        text2 = Text(Point(180, 700), "%.2f" % closeList[dateInPixel])
        text2.setSize(20)
        text2.setFill("white")
        text2.setOutline("white")
        text2.draw(win)

        text3.undraw()
        text3 = Text(Point(180, 675), "%.2f" % minVal)
        text3.setSize(20)
        text3.setFill("white")
        text3.setOutline("white")
        text3.draw(win)

        text4.undraw()
        text4 = Text(Point(180, 650), "%.2f" % maxVal)
        text4.setSize(20)
        text4.setFill("white")
        text4.setOutline("white")
        text4.draw(win)

        text5.undraw()
        text5 = Text(Point(190, 625), str(dateList[dateInPixel][1])+"/"+str(dateList[dateInPixel][2])+"/"+str(dateList[dateInPixel][0]))
        text5.setSize(20)
        text5.setFill("white")
        text5.setOutline("white")
        text5.draw(win)

main()
