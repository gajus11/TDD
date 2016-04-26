from django.shortcuts import redirect, render
from lists.models import Item, List
from django.core.exceptions import ValidationError

from lists.forms import ItemForm
from lists.models import Item, List

def home_page(request):
    context = {
        'form' : ItemForm(),
    }
    return render(request, 'home.html', context)


def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        context = {
            'error' : error,
        }
        return render(request, 'home.html', context)
    return redirect(list_)


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item.objects.create(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    context = {
        'list' : list_,
        'error' : error,
    }
    return render(request, 'list.html', context)
