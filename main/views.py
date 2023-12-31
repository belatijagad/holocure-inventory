from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from main.forms import IdolsForm
from django.urls import reverse
from main.models import Idols
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.
def show_main(request):
    return render(request, 'main.html')

@login_required(login_url='/login')
def display_items(request):
    idols = Idols.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'idols': idols,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'display_items.html', context)

def add_items(request):
    form = IdolsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        idol = form.save(commit=False)
        idol.user = request.user
        idol.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, 'add_items.html', context)

def show_xml(request):
    data = Idols.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Idols.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Idols.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Idols.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return redirect('main:login')

def increment_superchat(request, id):
    idol = Idols.objects.get(pk=id)
    idol.superchats += 1
    idol.save()
    return redirect('main:display_items')

def decrement_superchat(request, id):
    idol = Idols.objects.get(pk=id)
    if idol.superchats > 0:
        idol.superchats -= 1
        idol.save()
    return redirect('main:display_items')

@csrf_exempt
def add_idols_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        generation = request.POST.get('generation')
        debut_date = request.POST.get('debut_date')
        tagline = request.POST.get('tagline')
        user = request.user

        new_idol = Idols(name=name, branch=branch, generation=generation, debut_date=debut_date, tagline=tagline, user=user)
        new_idol.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_idols_json(request):
    product_item = Idols.objects.all()
    return HttpResponse(serializers.serialize('json', product_item))

def delete_idol(request, id):
    obj = get_object_or_404(Idols, pk=id)
    obj.delete()
    return JsonResponse({"status": "success"})