from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'
    

class PruebaListView(ListView):
    template_name = 'home/list.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'


class ModeloListView(ListView):
    model = Prueba
    template_name = 'home/list_prueba.html'
    context_object_name = 'lista_prueba'


class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    # fields = ['titulo', 'subtitulo', 'cantidad']
    success_url = reverse_lazy('app_home:success')
    form_class = PruebaForm


class HomeSuccessSaveView(TemplateView):
    template_name = 'home/sucess.html'


class HomeSuccessDeleteView(TemplateView):
    template_name = 'home/success_delete.html'


class ResumenFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'


class HomeTemplate1View(TemplateView):
    template_name = 'home/home1.html'


class HomeTemplate2View(TemplateView):
    template_name = 'home/home2.html'


class HomeTemplate3View(TemplateView):
    template_name = 'home/home3.html'


