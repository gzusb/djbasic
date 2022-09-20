from curses.ascii import EM
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from applications import empleado
from .models import Empleado
from django.urls import reverse_lazy
from .forms import EmpleadoForm

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    # When it use get_queryset is not require the "model"
    # model = Empleado
    paginate_by = 5
    ordering = 'id'
    context_object_name = 'list'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains = kword, 
            last_name__icontains = kword,
            # departamento__icontains = kword,
        )
        return lista


class ListAllEmpleadosAdminView(ListView):
    template_name = 'empleado/list_admin.html'
    # When it use get_queryset is not require the "model"
    # model = Empleado
    paginate_by = 5
    ordering = 'id'
    context_object_name = 'list'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name__icontains = kword, 
            last_name__icontains = kword,
            # departamento__icontains = kword,
        )
        return lista


class ListByAreaEmpleado(ListView):
    template_name = 'empleado/list_by_area.html'
    context_object_name = 'lista'
    paginate_by = 2

    def get_queryset(self):
        area = self.kwargs['area'] # Get param dep_name from URL
        queryset = Empleado.objects.filter(
            departamento__name = area
        )
        return queryset


class ListEmpleadosByKword(ListView):
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print("************************")
        kword = self.request.GET.get('kword')
        lista = Empleado.objects.filter(
            first_name = kword
        )
        print(">> ", kword)
        print(">> ", lista)

        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/skills.html'
    context_objects_name = 'habilidades'

    def get_queryset(self):
        user_id = self.request.GET.get('user_id')
        user_id = int(user_id) if user_id.isdigit() else 1
        empleado = Empleado.objects.get(id=user_id)
        print(">>", empleado.habilidades.all())
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/detail_employee.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail Employee'

        print(context)
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleado/add.html'
    # Show specific elements use a list
    # fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar']
    # If the "form_class" is used, isn't necesary "fields", the fields are defined in the file forms.py
    form_class = EmpleadoForm
    # Show all elements use a tuple with the item " __all__ "
    # fields = ('__all__')
    # If don't require to use another page, set . (dot)
    # success_url = '.'
    # If require to use another page, set the path (used in urls.py)
    # success_url = '/success'
    # The best practice is to use reverse_lazy('app_name:url_name')
    success_url = reverse_lazy('app_empleado:list_admin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Employee'
        print(context)
        return context

    def form_valid(self, form):
        # If you want to avoid save using .save(), you can add as param in the function "commit=False"
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super().form_valid(form)

class EmpleadoSuccessSaveView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoUpdateView(UpdateView):
    template_name = 'empleado/update.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades']
    success_url = reverse_lazy('app_empleado:list_admin')

    def post(self, request, *args, **kwargs):
        print("************    POST    ****************")
        print(request.POST)
        print("****************************************")
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print("************ FORM VALID ****************")
        # print(form)
        print("****************************************")
        return super().form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'Empleado/delete.html'
    success_url = reverse_lazy('app_empleado:list_admin')
    context_object_name = 'employee'



class EmpleadoSuccessDeleteView(TemplateView):
    template_name = "empleado/success_delete.html"


class InicioView(TemplateView):
    template_name = 'inicio.html'