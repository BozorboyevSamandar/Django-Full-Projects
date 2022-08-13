from django.urls import path
from .views import loginPage, logoutUser, registerUser

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser,name='register'),
]
