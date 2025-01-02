from django.urls import path
from . import views

urlpatterns = [
    path("",views.TaskCreateView.as_view()),
    path("success/",views.SuccessTemplate.as_view())
]
