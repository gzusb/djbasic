from django.urls import path
from .  import views

app_name = 'app_department'
urlpatterns = [
    path('department/', views.DepartmentsView.as_view(), name='department'),
    path('department/list/', views.DepartmentListView.as_view(), name='department_list'),
    path('department/add/', views.DepartmentCreateView.as_view(), name='add'),
    path('department/success/', views.DepartmentSuccessSaveView.as_view(), name='success'),
    path('department/update/<pk>/', views.DepartmentUpdateView.as_view(), name='update'),
    path('department/delete/<pk>/', views.DepartmentDeleteView.as_view(), name='delete'),
]
