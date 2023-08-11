from django.urls import path
from .  import views

urlpatterns=[
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('create-room/',views.createRoom,name="create-room"),
    path('upadteroom/<str:pk>/',views.updateRoom,name="updateroom"),
    path('deleteroom/<str:pk>/',views.deleteRoom,name="deleteroom"),
    path('delete-message/<str:pk>/',views.deleteMessage,name="delete-message"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutuser,name="logout"),
    path('register/',views.registeruser,name="register"),
    path('userprofile/<str:pk>/',views.userProfile,name="userprofile"), 


]