from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import CreatesNewList


def view_items_in_list_to_do(response, id_to_do_list):
    """perform operations with ToDoList by given id"""
    ls = ToDoList.objects.get(id=id_to_do_list)
    if response.method == 'POST':
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("select_"+str(item.id)) == "clicked":
                    item.complete = True
                    item.text = response.POST.get("text_"+str(item.id))
                    print(response.POST.get("text_"+str(item.id)))
                else:
                    item.complete = False
                    item.text = response.POST.get("text_"+str(item.id))
                item.save()

        elif response.POST.get("newItem"):
            text = response.POST.get("new_item_text_field")
            print(text)
            if len(text) > 2:
                ls.item_set.create(text=text, complete=False)

        elif response.POST.get("DelItem"):
             to_do_list = response.user.todolist.all()
             td_list = to_do_list.get(id=id_to_do_list)
             print('Here!')
             for item in td_list.item_set.all():
                 if response.POST.get("DelItem") == "del_" + str(item.id):
                    item.delete()


    return render(response, "main/list_to_do_items.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html")


def create_to_do_list(response):
    if response.method == 'POST':
        form = CreatesNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect("/view_to_do_lists/to_do_list_%i" % t.id)
    else:
        form = CreatesNewList()
    return render(response, "main/create_to_do_list.html", {"form": form})


def view_to_do_lists(response):
    if response.method == 'POST':
        if response.POST.get("delete"):
            for td in response.user.todolist.all():
                if response.POST.get("td_list"+str(td.id)) == "clicked":
                    td.delete()
    return render(response,
                  "main/view_to_do_lists.html",
                  {"todolist": response.user.todolist.all(), 'response': response})


def view_figures(response):
    return render(response, "main/view_figures.html")
