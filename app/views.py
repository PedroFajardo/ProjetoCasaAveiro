from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from app.models import thing
from app import forms

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    tparams = {
        'title': 'Casa Aveiro',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    assert isinstance(request, HttpRequest)
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)

def listArca(request):
    if request.method == 'POST':
        for t in request.POST:
            if t != "csrfmiddlewaretoken":
                coisa = thing.objects.filter(name__icontains = t)[0]
                coisa.quantity = request.POST[t]
                coisa.save()

    things = thing.objects.filter(category__icontains = "Arca").order_by('name')
    
    return render(request, 'listArca.html', {'things' : things})

def listDispensa(request):
    if request.method == 'POST':
        for t in request.POST:
            if t != "csrfmiddlewaretoken":
                coisa = thing.objects.filter(name__icontains = t)[0]
                coisa.quantity = request.POST[t]
                coisa.save()

    things = thing.objects.filter(category__icontains = "Dispensa").order_by('name')
    return render(request, 'listDispensa.html', {'things' : things})

def listFrigorifico(request):
    if request.method == 'POST':
        for t in request.POST:
            if t != "csrfmiddlewaretoken":
                coisa = thing.objects.filter(name__icontains = t)[0]
                coisa.quantity = request.POST[t]
                coisa.save()

    things = thing.objects.filter(category__icontains = "Frigorifico").order_by('name')
    return render(request, 'listFrigorifico.html', {'things' : things})

def listFruta(request):
    if request.method == 'POST':
        for t in request.POST:
            if t != "csrfmiddlewaretoken":
                coisa = thing.objects.filter(name__icontains = t)[0]
                coisa.quantity = request.POST[t]
                coisa.save()

    things = thing.objects.filter(category__icontains = "Fruta").order_by('name')
    return render(request, 'listFruta.html', {'things' : things})

def listWC(request):
    if request.method == 'POST':
        for t in request.POST:
            if t != "csrfmiddlewaretoken":
                coisa = thing.objects.filter(name__icontains = t)[0]
                coisa.quantity = request.POST[t]
                coisa.save()

    things = thing.objects.filter(category__icontains = "WC").order_by('name')
    return render(request, 'listWC.html', {'things' : things})

def addThing(request):
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to ir
        form = forms.thingInsert(request.POST)
        if form.is_valid():  # is it valid?
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            category = form.cleaned_data['category']
            exists = thing.objects.filter(name__icontains=name)
            if not exists:
                t = thing(name=name, quantity=quantity, category=category)
                t.save()
                return render(request, 'addThing.html', {'form': form, 'inserted' : True})

    # if GET (or any other method), create blank form
    else:
        form = forms.thingInsert()
    return render(request, 'addThing.html', {'form': form})
