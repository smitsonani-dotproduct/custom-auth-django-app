from django.urls import path
from .views import LoginView, RegisterView, TestFunctionAuthView, TestClassAuthView

urlpatterns = [
    path("test-auth", TestFunctionAuthView),
    path("test-auth2", TestClassAuthView.as_view()),
    path("login", LoginView.as_view()),
    path("register", RegisterView.as_view()),
]
