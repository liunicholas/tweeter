import datetime

from django.db import models
from django.utils import timezone
from . import badhash
from django.contrib.auth.models import user

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    followed_users = models.CharField(max_length=20,default=",")
    password = models.TextField(default="")
    secretChar = models.CharField(max_length=10,default="")

    # post_ids = models.CharField(max_length=20, default="")
    def getId(self):
        return self.id
    # def getPostIds(self):
    #     return self.post_ids
    def __str__(self):
        # return str(self.id) + " " + self.user_name + " posts: " + self.post_ids + " followed users: " + self.followed_users
        return str(self.id) + " " + self.user_name + " followed users: " + self.followed_users + " Pw: " + self.password
    def getFollowedUsers(self):
        return self.followed_users
    def hashPassword(self):
        # print("TESTING")
        print(self.password)
        hashedPassword, secretChar = badhash.encode(self.password)
        self.secretChar = secretChar
        self.password = hashedPassword
        self.save()
        # print(self.hashedPassword)

    # class Meta:
    #     hashedPassword = ""
    #     secretChar = ""

class Post(models.Model):
    user_name = models.CharField(max_length=20)
    user_id = models.IntegerField(default=-1)
    post_picture_url = models.TextField(max_length=200)
    post_caption = models.TextField(max_length=144)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return "User: " + self.user_name + " " + str(self.user_id) + " Caption: " + self.post_caption
    def getId(self):
        return self.id
    def getUserId(self):
        return self.user_id
    def getUserName(self):
        return self.user_name
    def getPic(self):
        return self.post_picture_url
    def getCap(self):
        return self.post_caption
    def getDate(self):
        return self.post_date
    def getlikes(self):
        return self.likes
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.post_date <= now
