from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

class TaskCreateView(FormView):
    form_class= TaskForm
    template_name="challenges/Tasks.html"
    success_url="/"

    def form_valid(self, form):
          form.save()
          return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()  # Add tasks to the context
        return context



# class SuccessTemplate(TemplateView):
#     template_name = "challenges/success.html"

#     def get_context_data(self, **kwargs) -> dict[str]:
#         context = super().get_context_data(**kwargs)
#         context["message"] = "This is working"
#         return context


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "challenges/task_confirm_delete.html"  # A confirmation template before deletion
    context_object_name = "task"
    success_url = reverse_lazy('task_list') 


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "challenges/task_form.html"  # You can use the same form as in TaskCreateView
    context_object_name = "task"

    def get_success_url(self):
        return reverse_lazy('task_list')