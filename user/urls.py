from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
]