from django.urls import path
from .  import views

app_name = 'app_home'
urlpatterns = [
    path('home/', views.IndexView.as_view(), name='home'),
    path('home/list/', views.PruebaListView.as_view(), name='list'),
    path('home/list_prueba/', views.ModeloListView.as_view()),
    path('home/add/', views.PruebaCreateView.as_view(), name='add'),
    path('home/success/', views.HomeSuccessSaveView.as_view(), name='success'),
    # path('home/update/<pk>/', views.HomeUpdateView.as_view(), name='update'),
    # path('home/delete/<pk>/', views.HomeDeleteView.as_view(), name='delete'),
    # path('home/success_delete/', views.HomeSuccessDeleteView.as_view(), name='success_delete'),
    path('home/resume_foundation/', views.ResumenFoundationView.as_view(), name='resume_foundation'),
    path('home/home1/', views.HomeTemplate1View.as_view(), name='home1'),
    path('home/home2/', views.HomeTemplate2View.as_view(), name='home2'),
    path('home/home3/', views.HomeTemplate3View.as_view(), name='home3'),
]
