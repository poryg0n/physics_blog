from django.urls import path
from .views import (
        UserRegisterView, 
        UserEditView, 
        CreateProfilePageView,
        ShowProfilePageView,
        EditProfilePageView,
        PasswordsChangeView,
        )
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('create-profile-page/', CreateProfilePageView.as_view(), name='create-profile-page'),
    path('<int:pk>/edit-profile-page/', EditProfilePageView.as_view(), name='edit-profile-page'),
#   path('edit-user/', UserEditView.as_view(), name='edit-user'),
#   path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password-change'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name='password-change'),
    path('password-success/', views.password_success, name='password-success'),
]

