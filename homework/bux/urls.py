from django.urls import path
from .views import views_home,views_home2,views_aboute,views_services,views_contact,views_server

urlpatterns = [
    path('',views_home,name='views_home'),
    path('home/',views_home2,name='views_home2'),
    path('aboute/', views_aboute, name='views_aboute'),
    path('services/', views_services, name='views_services'),
    path('contact/', views_contact, name='views_contact'),
    path('new/',views_server,name='views_server')

]