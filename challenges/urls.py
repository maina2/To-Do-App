from django.urls import path
from . import views

urlpatterns = [
    path("",views.TaskCreateView.as_view(),name="task_list"),
    path("task/<int:pk>/edit/", views.TaskUpdateView.as_view(), name="task_edit"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task_delete"),
]
