from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mapaQGIS/', views.mapaQGIS, name='mapaQGIS'),
    path('informacionFormulario/', views.informacionFormulario, name='informacionFormulario'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('mapaGoogle/', views.mapaGoogle, name='mapaGoogle'),
    path('about-1/', views.about1, name='about-1'),
    path('mapDevol/', views.mapDevol, name='mapDevol'),
    
]