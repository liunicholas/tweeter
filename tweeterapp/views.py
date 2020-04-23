#django 3
#python 3.8

#admin un: ethan
#admin pw: ethan

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Post, MyUser
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from random import *
from . import badhash

#stuff for stock report
from tweeterapp.yfinance import *
# from tweeterapp.graphics import *
from random import *
import numpy as np

defaultPicUrl = "data:image/png;base64,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"

def login(request):
    #goes to login page html
    return render(request, 'tweeterapp/login.html', {})

def authentication(request):
    #gets the informtion from the login.html
    username=request.POST['username']
    password=request.POST['password']
    username=username.lower().strip()
    password=password.strip()
    # user = MyUser.objects.filter(username=username)

    # admin must log in through the real admin login
    # if username == "poster":
    #     return HttpResponseRedirect('/tweeterapp/admin')
    #
    # if len(user) != 0:
    #     print(user[0])
    #     secretChar = user[0].secretChar
    #     hashedPw = user[0].password
    #     realPW = badhash.decode(hashedPw,secretChar)
    #     print(password)
    #     print(realPW)
    #     if realPW == password:
    #         # gets all the information of the user and its followed users for context
    #         context = createContext(username)
    #         #real website
    #         return render(request, 'tweeterapp/userPage.html', context)
    #
    #     else:
    #         # invalid user, goes back to login
    #         return HttpResponseRedirect('/tweeterapp/login')
    #
    # else:
    #     # invalid user, goes back to login
    #     return HttpResponseRedirect('/tweeterapp/login')


    user=authenticate(request, username=username, password=password)
    # admin must log in through the real admin login
    if username == "poster":
        return HttpResponseRedirect('/tweeterapp/admin')

    # if the username and password corresspond to a real user
    if user is not None:
        #gets all the information of the user and its followed users for context
        context = createContext(username)
        #real website
        return render(request, 'tweeterapp/userPage.html', context)
        #return HttpResponseRedirect('/tweeterapp/' + username + "/")

    else:
        #invalid user, goes back to login
        return HttpResponseRedirect('/tweeterapp/login')

def createContext(username):
    #get the user and then its posts and followed users
    username=username.strip().lower()
    thisThisUser = MyUser.objects.filter(username=username)[0]
    # print(thisThisUser)

    # postIds = thisThisUser.getPostIds()
    followedUsersRaw = thisThisUser.getFollowedUsers()

    #creates list of user's posts
    thisPosts = []
    # post = []
    # postIdsList = getIntsFromString(postIds)
    # for postIndex in postIdsList:
    #     thisPost = get_object_or_404(Post, pk=postIndex)
    #     # post.append(thisPost.getPic)
    #     # post.append(thisPost.getCap)
    #     # post.append(thisPost.getlikes)
    #     # post.append(thisPost.getDate)
    #     # posts.append(post)
    #     # post = []
    #     thisPosts.append(thisPost)
    for thisPost in Post.objects.all():
        if thisPost.getUserId() == thisThisUser.getId():
            if thisPost.getPic() != defaultPicUrl:
                thisPosts.append(thisPost)

    if len(thisPosts) == 0:
        newPost = Post(username=thisThisUser.username,user_id=thisThisUser.id,post_picture_url=defaultPicUrl,post_caption="Default")
        newPost.save()
        thisPosts.append(newPost)
    # print("middle")
    #creates list of user objects of folloowed users
    followedUsers = []
    # followedUser = []
    followedUsersList = getIntsFromString(followedUsersRaw)
    # print("here after middle")
    # print(followedUsersList)
    for objIndex in followedUsersList:
        # print("in this")
        thisUser = get_object_or_404(User, pk=objIndex)
        # print("after in this")
        # followedUser.append(thisUser.getUserName)
        # followedUser.append(thisUser.getPostIds)
        # followedUsers.append(followedUser)
        # followedUser = []
        followedUsers.append(thisUser)
    # print("a little more")
    #creates list of list of followed user's posts objects
    allFollowedUserPosts = []
    followedUserPosts = []
    # followedUserPost = []
    for userObject in followedUsers:
        # postList = getIntsFromString(object.getPostIds())
        # for index in postList:
        #     thisPost = get_object_or_404(Post, pk=index)
        #     # followedUserPost.append(thisPost.getPic)
        #     # followedUserPost.append(thisPost.getCap)
        #     # followedUserPost.append(thisPost.getlikes)
        #     # followedUserPost.append(thisPost.getDate)
        #     # followedUserPosts.append(followedUserPost)
        #     # followedUserPost = []
        #     followedUserPosts.append(thisPost)
        #
        # allFollowedUserPosts.append(followedUserPosts)
        # followedUserPosts = []
        for thisPost in Post.objects.all():
            if thisPost.getUserId() == userObject.getId():
                followedUserPosts.append(thisPost)
        if len(followedUserPosts) == 0:
            newPost = Post(username=userObject.username,user_id=userObject.id,post_picture_url=defaultPicUrl,post_caption="Default")
            newPost.save()
            followedUserPosts.append(newPost)

        allFollowedUserPosts.append(followedUserPosts)
        followedUserPosts = []

    # followedUsersListRange = range(len(followedUsers))

    #to create the default display with just one post from each user
    # topFollowedUserPosts = []
    # for i in range(0,len(allFollowedUserPosts)):
    #     topFollowedUserPosts.append(allFollowedUserPosts[i][0])

    context = {
        "user":thisThisUser,
        "posts":thisPosts,
        # "yourFirstPost":thisPosts[0],
        # "followedUsers":followedUsers,
        "allFollowedUserPosts":allFollowedUserPosts,
        # "oneFollowedUserPost":topFollowedUserPosts,
        # "numberOfFollowedUsers":followedUsersListRange,
        # "test":postIds,
    }
    # print("finished making context")
    return context

def addComment(request):

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def deleteComment(request):

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def addPost(request):
    username=request.POST['username']
    username=username.lower()
    # password=request.POST['password']
    # user=authenticate(request, username=username, password=password)
    # if user is not None:
    url=request.POST['url']
    caption=request.POST['caption']

    thisUser = MyUser.objects.filter(username=username)[0]
    userId = thisUser.getId()

    newPost = Post(username=username,user_id=userId,post_picture_url=url,post_caption=caption)
    newPost.save()

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def deletePost(request):
    username=request.POST['userName']
    username=username.lower()
    postId=request.POST['postId']

    thisPost = Post.objects.filter(id=postId)[0]
    thisPost.delete()

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def logout(request):
    #once it exits the authnetication url, the session is over
    return HttpResponseRedirect('/tweeterapp/login/')

def newUser(request):
    print(request.POST)
    username=request.POST['username']
    username=username.lower().strip()
    tryUser = MyUser.objects.filter(username=username)
    print(tryUser)
    password=request.POST['password']
    password2=request.POST['password2']
    if len(tryUser) == 0 and username != "" and password==password2:
        newUser = MyUser(username=username)
        newUser.set_password(password)
        newUser.save()
        # newUser.hashPassword()
    else:
        return HttpResponseRedirect('/tweeterapp/')

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def followUser(request):
    print(request.POST)
    username = request.POST['username']
    user = MyUser.objects.filter(username=username)[0]
    followerRequest = request.POST['followerRequest']
    followerRequest=followerRequest.lower().strip()
    tryFollow = MyMyUser.objects.filter(username=followerRequest)
    if len(tryFollow) != 0:
        if str(tryFollow[0].id) not in user.followed_users:
            userId = str(tryFollow[0].id)
            user.followed_users += ",%s," % userId
            user.save()
    print("here")
    #gets all the information of the user and its followed users for context
    print(username)
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def unfollowUser(request):
    print(request.POST)
    username = request.POST['username']
    confirm = request.POST['confirm']
    user = MyUser.objects.filter(username=username)[0]
    unfollowId = str(request.POST['userId'])
    intList = []
    tempStore = ""
    print(unfollowId)
    print("^id")
    print(confirm)
    if confirm == "CONFIRM":
        print("here")
        for char in user.followed_users:
            if char != " " and char != ",":
                tempStore += char
            else:
                if tempStore != "" and tempStore != "," and tempStore != '':
                    print(tempStore)
                    if tempStore not in intList and tempStore != unfollowId:
                        print(tempStore)
                        intList.append(int(tempStore))
                tempStore = ""

        followedUsers = ""
        for item in intList:
            followedUsers+=str(item) + ","

        user.followed_users = followedUsers
        user.save()

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def deleteAccount(request):
    username = request.POST['username']
    confirm = request.POST['confirm']
    if confirm == "CONFIRM":
        user = MyUser.objects.filter(username=username)[0]
        user.delete()

        return render(request, 'tweeterapp/login.html', {})

    else:
        #gets all the information of the user and its followed users for context
        context = createContext(username)
        #real website
        return render(request, 'tweeterapp/userPage.html', context)

def editPost(request):
    username = request.POST['username']
    postId = request.POST['postId']
    newURL = request.POST['url']
    newCaption = request.POST['caption']

    post = Post.objects.filter(id=postId)[0]

    if post.post_caption != newCaption or post.post_picture_url != newURL:
        if "(edited)" not in newCaption:
            newCaption += " (edited)"

    post.post_caption = newCaption
    post.post_picture_url = newURL
    post.save()

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def getIntsFromString(string):
    #converts string of ints separated by commas into a list of ints
    intList = []
    tempStore = ""
    for char in string:
        if char != " " and char != ",":
            tempStore += char
        else:
            if tempStore != "" and tempStore != "," and tempStore != '':
                if tempStore not in intList:
                    print(tempStore)
                    intList.append(int(tempStore))
            tempStore = ""

    return intList

# def startGraph():
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

# def drawGraphDeatils(win, stockName):
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

# def drawGraph(win, totalItems, maxVal, pixelPerDate, pixelPerDollar, dateList):
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

def makeStockReport(stockName):
    # win = startGraph()
    # stockName = getStockName(win)
    openList, closeList, dateList = getData(stockName)

    totalItemsInitial = len(dateList)

    openList, closeList, dateList = predictFutureProbability(openList, closeList, dateList)

    # drawGraphDeatils(win, stockName)

    totalItems = totalItemsInitial
    totalItems = len(dateList)
    minVal, maxVal = getMinMax(openList, closeList)
    # pixelPerDate = 1360.0/totalItems
    # pixelPerDollar = 695.0/maxVal
    # drawGraph(win, totalItems, maxVal, pixelPerDate, pixelPerDollar, dateList)

    # low = 100000
    # high = 0
    # DRAWN = False
    # text1 = Text(Point(180, 725), "")
    # text2 = Text(Point(180, 725), "")
    # text3 = Text(Point(180, 725), "")
    # text4 = Text(Point(180, 725), "")
    # text5 = Text(Point(180, 725), "")
    # for i in range(0,totalItems,10):
    #     xVal = i*pixelPerDate+50
    #     yVal = (openList[i])*pixelPerDollar+50
    #     # print(xVal, yVal)
    #     point = Point(xVal, yVal)
    #     point.setFill("green")
    #     point.setOutline("green")
    #     point.draw(win)
    #     xVal = i*pixelPerDate+50
    #     yVal = (closeList[i])*pixelPerDollar+50
    #     # print(xVal, yVal)
    #     point = Point(xVal, yVal)
    #     point.setFill("red")
    #     point.setOutline("red")
    #     point.draw(win)
    #
    #     if openList[i] < low:
    #         low = openList[i]
    #     if openList[i] > high:
    #         high = openList[i]
    #     if closeList[i] < low:
    #         low = closeList[i]
    #     if closeList[i] > high:
    #         high = closeList[i]
    #
    #     text1.undraw()
    #     text1 = Text(Point(180, 725), "%.2f" % openList[i])
    #     text1.setSize(20)
    #     text1.setFill("white")
    #     text1.setOutline("white")
    #     text1.draw(win)
    #
    #     text2.undraw()
    #     text2 = Text(Point(180, 700), "%.2f" % closeList[i])
    #     text2.setSize(20)
    #     text2.setFill("white")
    #     text2.setOutline("white")
    #     text2.draw(win)
    #
    #     text3.undraw()
    #     text3 = Text(Point(180, 675), "%.2f" % low)
    #     text3.setSize(20)
    #     text3.setFill("white")
    #     text3.setOutline("white")
    #     text3.draw(win)
    #
    #     text4.undraw()
    #     text4 = Text(Point(180, 650), "%.2f" % high)
    #     text4.setSize(20)
    #     text4.setFill("white")
    #     text4.setOutline("white")
    #     text4.draw(win)
    #
    #     text5.undraw()
    #     text5 = Text(Point(190, 625), str(dateList[i][1])+"/"+str(dateList[i][2])+"/"+str(dateList[i][0]))
    #     text5.setSize(20)
    #     text5.setFill("white")
    #     text5.setOutline("white")
    #     text5.draw(win)
    #
    #     if i>100:
    #         recentList = closeList[i-99:i+1]
    #         avg = sum(recentList) / len(recentList)
    #         xVal = i*pixelPerDate+50
    #         yVal = avg*pixelPerDollar+50
    #         point = Point(xVal, yVal)
    #         point.setFill("blue")
    #         point.setOutline("blue")
    #         point.draw(win)
    #
    #     if i>20:
    #         recentList = closeList[i-19:i+1]
    #         avg = sum(recentList) / len(recentList)
    #         xVal = i*pixelPerDate+50
    #         yVal = avg*pixelPerDollar+50
    #         point = Point(xVal, yVal)
    #         point.setFill("yellow")
    #         point.setOutline("yellow")
    #         point.draw(win)
    #
    #     if i>totalItemsInitial and DRAWN==False:
    #         p1 = Point(i*pixelPerDate+50, 50)
    #         p2 = Point(i*pixelPerDate+50, 770)
    #         line = Line(p1, p2)
    #         line.setFill("white")
    #         line.setOutline("white")
    #         line.draw(win)
    #         DRAWN=True;

    # while True:
    #     userClick = win.getMouse()
    #     x = userClick.getX()
    #     pixelLength = x-50
    #     dateInPixel = int(pixelLength/pixelPerDate)
    #
    #     maxVal = max(openList[:dateInPixel]+closeList[:dateInPixel])
    #     minVal = min(openList[:dateInPixel]+closeList[:dateInPixel])
    #
    #     text1.undraw()
    #     text1 = Text(Point(180, 725), "%.2f" % openList[dateInPixel])
    #     text1.setSize(20)
    #     text1.setFill("white")
    #     text1.setOutline("white")
    #     text1.draw(win)
    #
    #     text2.undraw()
    #     text2 = Text(Point(180, 700), "%.2f" % closeList[dateInPixel])
    #     text2.setSize(20)
    #     text2.setFill("white")
    #     text2.setOutline("white")
    #     text2.draw(win)
    #
    #     text3.undraw()
    #     text3 = Text(Point(180, 675), "%.2f" % minVal)
    #     text3.setSize(20)
    #     text3.setFill("white")
    #     text3.setOutline("white")
    #     text3.draw(win)
    #
    #     text4.undraw()
    #     text4 = Text(Point(180, 650), "%.2f" % maxVal)
    #     text4.setSize(20)
    #     text4.setFill("white")
    #     text4.setOutline("white")
    #     text4.draw(win)
    #
    #     text5.undraw()
    #     text5 = Text(Point(190, 625), str(dateList[dateInPixel][1])+"/"+str(dateList[dateInPixel][2])+"/"+str(dateList[dateInPixel][0]))
    #     text5.setSize(20)
    #     text5.setFill("white")
    #     text5.setOutline("white")
    #     text5.draw(win)

    return openList, closeList, dateList

def showStockHistory(request):
    name=request.POST['name']
    openList, closeList, dateList = makeStockReport(name)

    context = {}
    stockInfo = []
    for i in range(len(openList)):
        tempList=[]
        tempList.append(str(dateList[i][1])+"/"+str(dateList[i][2])+"/"+str(dateList[i][0]))
        tempList.append(openList[i])
        tempList.append(closeList[i])
        stockInfo.append(tempList)

    stock = Ticker(name)
    stockInfoKeys=stock.info
    context['stockInfo'] = stockInfo
    context['stockPic'] = stockInfoKeys['logo_url']
    context['stockName'] = stockInfoKeys['longName']
    return render(request, 'tweeterapp/stockHistory.html', context)

def showStock(request):
    name=request.POST['name']

    stock = Ticker(name)
    stockInfo=stock.info

    context = {}

    context['stockPic'] = stockInfo['logo_url']
    context['stockName'] = stockInfo['longName']
    context['dayLow'] = stockInfo['dayLow']
    context['dayHigh'] = stockInfo['dayHigh']
    context['currentPrice'] = stockInfo['regularMarketPrice']
    context['summary'] = stockInfo['longBusinessSummary']

    return render(request, 'tweeterapp/stockInfo.html', context)
