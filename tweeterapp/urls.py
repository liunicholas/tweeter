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

    # path('<username>/', views.displayPage, name='userpage'),
]
