from django.urls import path
from .views import *
app_name = "profil"

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name='register'),

]