from django.urls import path
from todos.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="list_todos"),
]
