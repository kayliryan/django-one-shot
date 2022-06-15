# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from todos.models import TodoList

# Create your views here.


class TodoListView(ListView):
    model = TodoList
    template_name = "todos/list.html"


class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todos/detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     todo_items = []
    #     for item in self.items.all():
    #         todo_items.append(item)
    #     context["todo_items"] = todo_items
    #     return context
    #
    # a_todo_list = TodoList.objects.get()
    # context['todo_list'] = self.todolist_list
    # todo_items = []
    # for item in TodoList.items.all():
    #     # self.request.user.todolist_list.all():
    #     # items.all? todolist_list.all?
    #     todo_items.append(item.items)
    # context["items_in_todo_list"] = todo_items
    # return context

    # # Create a new empty list and assign it to a variable
    # foods = []
    # # For each item in the user's shopping items
    # for item in self.request.user.shopping_items.all():
    #     # Add the shopping item's food to the list
    #     foods.append(item.food_item)
    # # Put that list into the context
    # context["food_in_shopping_list"] = foods
    # return context
