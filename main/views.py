from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import IdolsForm
from django.urls import reverse
from main.models import Idols
from django.core import serializers

# Create your views here.
def show_main(request):
    return render(request, 'main.html')

def display_items(request):
    idols = Idols.objects.all()
    context = {
        'idols': idols,
    }
    return render(request, 'display_items.html', context)

def add_items(request):
    form = IdolsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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

