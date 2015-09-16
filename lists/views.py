from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    if Item.objects.count() == 0 :
        comment = 'yey, waktunya berlibur'
    if (Item.objects.count() > 0) and (Item.objects.count() < 5) :
        comment = 'sibuk tapi santai'
    if Item.objects.count() >= 5 :
        comment = 'oh tidak'

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items, 'comment': comment})
