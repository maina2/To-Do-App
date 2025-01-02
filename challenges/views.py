from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.views.generic import CreateView,ListView,View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

class TaskCreateView(FormView):
    form_class= TaskForm
    template_name="challenges/Tasks.html"
    success_url="/success"

    def form_valid(self, form):
          form.save()
          return super().form_valid(form)



class SuccessTemplate(TemplateView):
    template_name = "challenges/success.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This is working"
        return context




