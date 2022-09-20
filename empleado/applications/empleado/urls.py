from django.urls import path
from .  import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = 'app_empleado'
urlpatterns = [
    path('', views.InicioView.as_view(), name='home'),
    path('employee/list/', views.ListAllEmpleados.as_view(), name='list'),
    path('employee/list_admin/', views.ListAllEmpleadosAdminView.as_view(), name='list_admin'),
    path('employee/list_by_area/<area>/', views.ListByAreaEmpleado.as_view(), name='list_by_area'),
    path('employee/search_employee/', views.ListEmpleadosByKword.as_view(), name='search_employee'),
    path('employee/skills/', views.ListHabilidadesEmpleado.as_view(), name='skills'),
    path('employee/detail_employee/<pk>/', views.EmpleadoDetailView.as_view(), name='detail_employee'),
    path('employee/add/', views.EmpleadoCreateView.as_view(), name='add'),
    path('employee/success/', views.EmpleadoSuccessSaveView.as_view(), name='success'),
    path('employee/update/<pk>/', views.EmpleadoUpdateView.as_view(), name='update'),
    path('employee/delete/<pk>/', views.EmpleadoDeleteView.as_view(), name='delete'),
    path('employee/success_delete/', views.EmpleadoSuccessDeleteView.as_view(), name='success_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
