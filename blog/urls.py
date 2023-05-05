from django.urls import path
from django.views.generic import TemplateView
from blog.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre', TemplateView.as_view(template_name='about.html'), name='sobre'),
    path('contato', ContatoView.as_view(), name='contato'),
    path('post/<int:pk>', PostView.as_view(), name='post'),
    path('buscar', BuscarView.as_view(), name='buscar')
] 

