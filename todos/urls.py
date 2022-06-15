from django.urls import path
from todos.views import (
    TodoListView,
    TodoListDetailView,
    TodoListCreateView,
    TodoListUpdateView,
    TodoListDeleteView,
    TodoItemCreateView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="list_todos"),
    path("<int:pk>/", TodoListDetailView.as_view(), name="show_todolist"),
    path("create/", TodoListCreateView.as_view(), name="create_todolist"),
    path(
        "<int:pk>/edit/", TodoListUpdateView.as_view(), name="update_todolist"
    ),
    path(
        "<int:pk>/delete/", TodoListDeleteView.as_view(), name="delete_todolist"
    ),
    path("items/create/", TodoItemCreateView.as_view(), name="create_todoitem"),
]
