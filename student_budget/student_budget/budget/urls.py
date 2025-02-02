from django.urls import path
from . import views
from . views import user_login, user_registration, expense


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', user_login, name='login'),
    path('registration/', user_registration, name='registration'),
    path('about/', expense, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Ensure this is correctly linked to the dashboard vie
]
