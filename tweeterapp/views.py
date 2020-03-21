#django 3
#python 3.8

#admin un: poster
#admin pw: ethan

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Post, User
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.utils import timezone
from random import *
from . import badhash

defaultPicUrl = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAPFBMVEXb29v////u7u7c3Nz39/f8/Pzi4uLl5eXX2Nf09PTs7Ozj4+P6+vrf39/19fXo6OjZ3tnV19bc2tfb19U+xcbzAAAGKklEQVR4nO2di46jIBRAWxAoCqU78///umLr1Haso9wHYjjZZJNJpuPphXt5KJ7E0Tn9Ox2dS+4LIKcalk81LJ9qWD7VsHyqYflUw/KphuVTDcunGpZPNSyfalg+1bCyfxhj6LXuTKTrtJdsf5Zn30IbYRunlDpH+v9dcxVBs2hSxnAQ8EY05084ETzhBQwQt1Jj3Ue9O8oG2ku40LUUaYT6Q++BNXzdEpHwuXH+pmlzX+5WfLsyfE8EeY/EJPzV++ZwFHG8EXxmn162tM8XR/ykc3ukdEykTfSLWOzLwTWU8cPM5g74SjihXtPt9IX3YcN1CZjfGEY0xxtyxdepPXCK66IgkuPt9I3zQXc6YAt9oAzeJX2hGgYUv0iLFkNUQzzBvvwPn4hgiWkIzzFTLNJVIRnG77pFFRyjCAavVmALYimijdoMuuCQbuBgVXwKwagITzVIhh6nDv5Cwy8Nx9CnzJXWoOCKOIaQycQyDYYhvKljVvp3wAkVI4ZUnfCOAY5sMAyvlIJnB2xjCHMLyjYaAVZFuCFtGz2D8yl8TIM73p4DNga/QEcNnlwQWPfBhvQhBE+kYIaauhcOwBY1YIYcIYQGEWQoWUJ4PoN2NECG1LVwBDR2AxlirI6uQUGCCDFEWh5dAWTHBmLIk2cikFwDMaSa+M4AuEzAr3KMZ0YAJRFgiL+A+BlAMwUYcmXSCGCamPqbkn7eNAUwh0r/bmjWSD9BfFvRLJzdEG0bYxN0a4hzwNcVt8OZaPqOyC8oWQVBNb8QQ4Q9jI1oZsPkZCpT6wVvsUDaTdwE1+x3hL9c8JZDvFsX1sM3OQQaJidhbsPr4Q2TBzXJubTGEBv+flhMLk02PH495B7T8Bt2zIb8k3zOtcRIx6sXey+zIfcTNZJ1xTuS4dmvUtZp0r8a3pKfPrVIN+QtiOkT4HRDnrsURtK3ZkrZt0hPpQBDzo6YPLMAGXKOavI8RMt1r0kk0xO0fBUxx65FhK9e5HrSW3IN3ED304Dgyqb8a6UjXDMo5pnTFJ5c02Q8U4JnKSPHHv4PHCM36AMJMDh2EbOGkKMn5qr2I/RzKMRH19Ogron5auEI8fg733DmCW3F2MXZQ5TtNH8bjRAOwPfQRiN0+TRzKXxCNVHcRSe8Q9MV99EJHzcCUCiinxkFA/9p4JxzplmwFZudpNEnEnciBVjkJgN0Tts7+4vgAJ7idW99MIKZUXeWRacElNENZqFHP4HWw/ONQ72jG/+MXQltqTtuoSMGMtVQuxlrLwEIo0UvEkQnQfu0AU7D/0xFOma7Y0PSQAlP89Z2U+Vosi8aJqDF2pzjBJkf8YnsslsRSDWeV05SJujfjODDwrH6feNkOFifHimNsE69RlMpdxWG8SUQ9HgdQtsOr8pu2xA6ptDt4SukvYZchnv4ZolhUzz+m4KOb3h8jt/jj294fI6faY5veHxqpimf4/fD4xsen+NnGsZVIPkK158lNpRem2FxxlrbvNL/JK7YhBBXoybp4EUd4Xug+Cqlj17CNuvXvJWzojXaF7D0pnuzq0vdCFausSJ0EjPDo70LSWrTbtuoWDKN75lFiifOu5B6OfynEvqGi7EcDm0PXge0yM2hbKunmmz99P6HPEXofuN6S+ilJvySX/0mXBSUDYn9Mq2ha7ykskGyESmPsG039Jo1eG+W1my94q2R7xY3AzlwFn27+Gd/VuaM3hRlN2zNra8WMmwYhZHTCI87tZWG96iWNTTrxgOr+qFsc3e+edyaQP5tKPX+wvekgb92PvkV21y4dtlxeeTtcW6IpSbttfOxOrTMZ10lo+6Os8H8HGHPffIjDPtpRPfJULZFtM8pH29NnVsE8tznWuIg5iZZl7lRTXnxe6DEXJt8N5SmVL+BX7VDvhsm3r+8H5xZNPR7Hr+s5f1u8ctdNP67FFMAl1Hi9Eyb35MY6tIb6BMXJpXhx7DYDDrLPavKST/kPQSRg8ezDf5huJP1CVTspJV2e58ipTE8QzVkGu6Tufnoe2NvWHyNXyK+6ovs3fb7oG+puS+BnGpYPtWwfKph+VTD8qmG5VMNy6calk81LJ9qWD7VsHyqYflUw/KphuVTDcvn+Ib/AT9IcIlzlHcdAAAAAElFTkSuQmCC"

def login(request):
    #goes to login page html
    return render(request, 'tweeterapp/login.html', {})

def authentication(request):
    #gets the informtion from the login.html
    username=request.POST['username']
    password=request.POST['password']
    user = User.objects.filter(user_name=username)
    if len(user) != 0:
        print(user[0])
        secretChar = user[0].secretChar
        hashedPw = user[0].password
        realPW = badhash.decode(hashedPw,secretChar)
        print(password)
        print(realPW)
        if realPW == password:
            # gets all the information of the user and its followed users for context
            context = createContext(username)
            #real website
            return render(request, 'tweeterapp/userPage.html', context)

        else:
            # invalid user, goes back to login
            return HttpResponseRedirect('/tweeterapp/login')

    else:
        # invalid user, goes back to login
        return HttpResponseRedirect('/tweeterapp/login')


    #user=authenticate(request, username=username, password=password)
    #admin must log in through the real admin login
    # if username == "poster":
    #     return HttpResponseRedirect('/tweeterapp/admin')

    #if the username and password corresspond to a real user
    # if user is not None:
    #     #gets all the information of the user and its followed users for context
    #     context = createContext(username)
    #     #real website
    #     return render(request, 'tweeterapp/userPage.html', context)
    #     #return HttpResponseRedirect('/tweeterapp/' + username + "/")
    #
    # else:
    #     #invalid user, goes back to login
    #     return HttpResponseRedirect('/tweeterapp/login')

def createContext(username):
    #get the user and then its posts and followed users
    thisThisUser = User.objects.filter(user_name=username)[0]

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
        newPost = Post(user_name=thisThisUser.user_name,user_id=thisThisUser.id,post_picture_url=defaultPicUrl,post_caption="Default")
        newPost.save()
        thisPosts.append(newPost)

    #creates list of user objects of folloowed users
    followedUsers = []
    # followedUser = []
    followedUsersList = getIntsFromString(followedUsersRaw)
    for objIndex in followedUsersList:
        thisUser = get_object_or_404(User, pk=objIndex)
        # followedUser.append(thisUser.getUserName)
        # followedUser.append(thisUser.getPostIds)
        # followedUsers.append(followedUser)
        # followedUser = []
        followedUsers.append(thisUser)

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
            newPost = Post(user_name=userObject.user_name,user_id=userObject.id,post_picture_url=defaultPicUrl,post_caption="Default")
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

    return context

def addPost(request):
    username=request.POST['username']
    username=username.lower()
    # password=request.POST['password']
    # user=authenticate(request, username=username, password=password)
    # if user is not None:
    url=request.POST['url']
    caption=request.POST['caption']

    thisUser = User.objects.filter(user_name=username)[0]
    userId = thisUser.getId()

    newPost = Post(user_name=username,user_id=userId,post_picture_url=url,post_caption=caption)
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
    tryUser = User.objects.filter(user_name=username)
    print(tryUser)
    password=request.POST['password']
    password2=request.POST['password2']
    if len(tryUser) == 0 and username != "" and password==password2:
        newUser = User(user_name=username,password=password)
        newUser.save()
        newUser.hashPassword()
    else:
        return HttpResponseRedirect('/tweeterapp/')

    #gets all the information of the user and its followed users for context
    context = createContext(username)
    #real website
    return render(request, 'tweeterapp/userPage.html', context)

def getIntsFromString(string):
    #converts string of ints separated by commas into a list of ints
    intList = []
    for char in string:
        if char != " " and char != ",":
            intList.append(int(char))

    return intList
