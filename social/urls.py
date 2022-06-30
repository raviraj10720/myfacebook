from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('logout',views.signout,name='logout'),
    path('register',views.register,name='register')
]
