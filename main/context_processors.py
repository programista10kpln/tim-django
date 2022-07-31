from .models import ToDoList


def todolist_cols(request) -> dict:
    ids = ToDoList.objects.values_list('id', flat=True)
    names = ToDoList.objects.values_list('name', flat=True)

    return {'attrs': zip(ids, names)}
