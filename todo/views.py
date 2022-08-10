from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Todo

from rest_framework import generics
from .serializers import TodoSerializer
from rest_framework.response import Response


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# class TodoAll(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     lookup_field = 'id'


# class TodoCreate(generics.):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class TodoUpdate(generics.UpdateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     lookup_field = 'id'

#     def perform_update(self, serializer):
#         serializer.save(owner=self.request.user)


# class TodoDelete(generics.DestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     lookup_field = 'id'

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')


def add(request):
    title = request.POST['title']
    Todo.objects.create(title=title)

    return redirect('todos:index')


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True

    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')
