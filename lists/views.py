from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List
from django.core.exceptions import ValidationError

def home_page(request):
#    if request.method == 'POST':
#        Item.objects.create(text=request.POST['tem_text'])
#        return redirect('/lists/the-only-list-in-the-world/')

    comment = 'yey, waktunya berlibur'
    
    items = Item.objects.all()
    return render(request, 'home.html', {'comment': comment})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    comment = ''
    countlist = Item.objects.filter(list_id=list_.id).count()
    if countlist == 0 :
        comment = 'yey, waktunya berlibur'
    elif (countlist > 0) and (countlist < 5) :
        comment = 'sibuk tapi santai'
    else :
        comment = 'oh tidak'

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'comment':comment, 'error': error})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(list_)

#def add_item(request, list_id):
 #   list_ = List.objects.get(id=list_id)
  #  Item.objects.create(text=request.POST['item_text'], list=list_)
   # return redirect('/lists/%d/' % (list_.id,))

