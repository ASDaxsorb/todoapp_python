from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("add/", views.add_todo, name="add"),
    path("save_new_todo", views.save_new_todo, name="save"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("edit/<int:pk>", views.EditView.as_view(), name="edit"),
    path("update/<int:todo_id>", views.update, name="update"),
    path("delete/<int:todo_id>", views.delete, name="delete"),
    path("toggle/<int:todo_id>", views.toggle_completed, name="toggle"),
]
