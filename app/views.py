from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from .models import *
from .forms import *

class OneView(ListView):
    model = Phone
    template_name = 'home.html'
    context_object_name = 'ones'

class AboutView(DetailView):
    model = Phone
    template_name = 'about.html'
    context_object_name = 'one'
    
class AddView(FormView):
    template_name = 'create.html'
    form_class = AddPhone
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        brand = form.cleaned_data['brand']
        model_name = form.cleaned_data['model_name']
        country = form.cleaned_data['country']
        created_item = Phone(brand=brand, model_name=model_name, country=country)
        created_item.save()
        return super().form_valid(form)
    
class TerminateView(DeleteView):
    model = Phone
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        filter = Phone.objects.filter(brand = search)
        context = {'filter':filter}
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html')

def add_image(request):
    data = Images.objects.all()
    if request.method == 'POST':
        img = Images.objects.create(image = request.FILES['image'])
        img.save()
        return render (request, 'create_image.html', {'data':data})
    else:
        return render (request, 'create_image.html', {'data':data})