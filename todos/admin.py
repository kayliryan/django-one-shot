from django.contrib import admin

from todos.models import TodoList


# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoList, TodoAdmin)
