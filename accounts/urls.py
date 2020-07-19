from django.contrib.auth import views
from django.contrib.auth.views import LoginView
from django.urls import path
# from accounts import views

from django.urls import path

from accounts.views import EmailRegisterFormView

app_name = 'accounts'


urlpatterns = [
    path('register/', EmailRegisterFormView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]