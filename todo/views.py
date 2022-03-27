from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Todo


class IndexView(generic.ListView):
    template_name = "todo/index.html"
    context_object_name = "todos"
    model = Todo


class DetailView(generic.DetailView):
    template_name = "todo/detail.html"
    context_object_name = "current_todo"
    model = Todo


class EditView(generic.DetailView):
    template_name = "todo/edit.html"
    context_object_name = "current_todo"
    model = Todo


def add_todo(request):
    return render(request, "todo/add.html")


def save_new_todo(request):
    title = request.POST["title"].strip()
    content = request.POST["content"].strip()
    if title != "":
        Todo.objects.create(title=title, content=content)
        return redirect(reverse("todo:index"))
    else:
        return render(
            request, "todo/add.html", {"error": "The todo must contain a title"}
        )


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    new_title = request.POST["title"].strip()

    if new_title != "":
        todo.title = new_title
        todo.content = request.POST["content"].strip()
        todo.save()
        return redirect(reverse("todo:detail", args=(todo_id,)))
    else:
        return render(
            request,
            "todo/edit.html",
            {"current_todo": todo, "error": "The title is empty!"},
        )


def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect(reverse("todo:index"))


def toggle_completed(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect(reverse("todo:index"))
