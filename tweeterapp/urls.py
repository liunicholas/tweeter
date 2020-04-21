#django 3
#python 3.8
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    # path('<int:user_id>/', views.displayPage, name='userpage'),
    # path('<username>/', views.displayPage, name='userpage'),
    path('login/', views.login, name='login'),
    path('authentication/', views.authentication, name='authentication'),
    path('logout/', views.logout, name='logout'),
    path('post/', views.addPost, name='post'),
    path('deletePost/', views.deletePost, name='deletePost'),
    path('newUser/', views.newUser, name='newUser'),
    path('followUser/', views.followUser, name='followUser'),
    path('unfollowUser/', views.unfollowUser, name='unfollowUser'),
    path('deleteAccount/', views.deleteAccount, name='deleteAccount'),
    path('editPost/', views.editPost, name='editPost'),
    path('addComment/', views.addComment, name='addComment'),
    path('deleteComment/', views.deleteComment, name='deleteComment'),

    # path('<username>/', views.displayPage, name='userpage'),
]
