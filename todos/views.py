# from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from todos.models import TodoList, TodoItem
from django.urls import reverse_lazy

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


class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todos/create.html"
    fields = [
        "name",
    ]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])
        # redirects to the detail page for that todo list

    # When do you use this????
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todos/update.html"
    fields = [
        "name",
    ]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.id])
        # redirects back to the detail page for that todo list


class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todos/delete.html"
    success_url = reverse_lazy("list_todos")

    # def get_success_url(self):
    #     return reverse_lazy("list_todos")
    # This does the exact same thing as above. just simplified to the line of
    # code above since we're not redirecting to a certain list with an int


class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todo_items/create.html"
    fields = [
        "task",
        "due_date",
        "is_completed",
        "list",
    ]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.list.id])


class TodoItemUpdateView(UpdateView):
    model = TodoItem
    template_name = "todo_items/update.html"
    fields = [
        "task",
        "due_date",
        "is_completed",
        "list",
    ]

    def get_success_url(self):
        return reverse_lazy("show_todolist", args=[self.object.list.id])
