from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from .forms import NewDepartmentForm
from applications.empleado.models import Empleado
from .models import Departamento


# Create your views here.

class DepartmentsView(TemplateView):
    template_name = 'departamento/home.html'
    success_url = reverse_lazy('app_department:success')


class DepartmentListView(ListView):
    template_name = 'departamento/list_all.html'
    # When it use get_queryset is not require the "model"
    # model = Departamento
    paginate_by = 2
    ordering = 'id'
    context_object_name = 'list'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        lista = Departamento.objects.filter(
            name__icontains = kword, 
            short_name__icontains = kword,
            # departamento__icontains = kword,
        )
        return lista


class DepartmentCreateView(FormView):
    template_name = 'departamento/add.html'
    form_class =  NewDepartmentForm
    success_url = reverse_lazy('app_department:department_list')

    def form_valid(self, form):
        print('*'*30)
        print('Form Valid')
        print('*'*30)

        depa = Departamento(
            name = form.cleaned_data['departamento'], 
            short_name = form.cleaned_data['nombre_corto'],
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        avatar = form.cleaned_data['avatar']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellidos,
            avatar = avatar,
            full_name = nombre + ' ' + apellidos,
            job = '1',
            departamento = depa
        )
        return super().form_valid(form)


class DepartmentSuccessSaveView(TemplateView):
    template_name = 'departamento/success.html'


class DepartmentUpdateView(UpdateView):
    template_name = 'departamento/update.html'
    model = Departamento
    fields = ['name', 'short_name']
    success_url = reverse_lazy('app_department:success')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


class DepartmentDeleteView(DeleteView):
    model = Departamento
    template_name = 'departamento/delete.html'
    success_url = reverse_lazy('app_department:success_delete')


class DepartmentSuccessDeleteView(TemplateView):
    template_name = "departamento/success_delete.html"

