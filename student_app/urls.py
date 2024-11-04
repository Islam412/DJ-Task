from django.urls import path
from .views import home_view, login_view, add_student,register_view


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('add/', add_student, name='add_student'),
]
