from django.urls import path
from . import views

urlpatterns = [
    path('test-auth', views.TestFunctionAuthView),
    path('test-auth2', views.TestClassAuthView.as_view()),
    path('login',views.LoginView.as_view()),
    path('register',views.RegisterView.as_view())
]