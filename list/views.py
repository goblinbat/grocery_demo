from django.shortcuts import render, redirect
from . import models
# from django.http import HttpResponse

def my_list(request):
    if request.method == "POST":
        my_item = models.Item.objects.get(id=request.POST['id'])
        my_item.grabbed = request.POST['grabbed']
        my_item.save()

        return redirect('myList')

    list_items = models.Item.objects.filter(grabbed=False)
    grabbed_items = models.Item.objects.filter(grabbed=True)

    context = {
        'the_list': list_items,
        'grabbed_items': grabbed_items
    }
    return render(request, 'list/my_list.html', context=context)
    
def add(request):
    if request.method == "POST":  
        # Add an item to the database
        # This creates an item to put in the table/database
        my_item = models.Item(name=request.POST["name"], amount=request.POST["amount"], price=request.POST["price"])
        
        #This saves the item to the item table in the database
        my_item.save()

        return redirect('myList')
    return render(request, 'list/add.html')

def delete(request):
    if request.method == 'POST':
        my_item = models.Item.objects.get(id=request.POST["id"])
        my_item.delete()

        return redirect('myList')
     
