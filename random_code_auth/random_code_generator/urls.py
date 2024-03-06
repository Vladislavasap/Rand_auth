from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('generate/', views.generate_random_code, name='generate_random_code'),
    path('register/', views.register_view, name='register'),
]
