from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import AddList

# Create your views here.


def index(request):
    return render(request, "main/main.html")


def list_site(request, list_id):
    ls = ToDoList.objects.get(id=list_id)
    items = Item.objects.all()

    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                if request.POST.get(f"c{item.id}") == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                return render(request, "main/list.html", {"ls": ls, "items": items})

    return render(request, "main/list.html", {"ls": ls, "items": items})


def add(request):
    if request.method == "POST":
        form = AddList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect(f"/list/{t.id}")
    else:
        form = AddList()

    return render(request, "main/add.html", {"form": form})
