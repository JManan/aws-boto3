from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.invoke_lambda_function_django, name="lambda-function"),
]
