from django.urls import path 
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('guest/',views.not_a_member,name='guest'),
    path('profile/',views.profile,name='profile'),
]
