from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=250, blank=False)
    subtitulo = models.CharField(max_length=250, blank=False)
    texto = models.TextField( blank=False)
    texto2 = models.TextField(blank=True, default='')
    texto3 = models.TextField(blank=True, default='')
    texto4 = models.TextField(blank=True, default='')
    texto5 = models.TextField(blank=True, default='')
    texto6 = models.TextField(blank=True, default='')
    texto7 = models.TextField(blank=True, default='')
    texto8 = models.TextField(blank=True, default='')
    texto9 = models.TextField(blank=True, default='')
    texto10 = models.TextField(blank=True, default='')
    titulo2= models.CharField(max_length=250, blank=True, default='')
    titulo3= models.CharField(max_length=250, blank=True, default='')
    titulo4= models.CharField(max_length=250, blank=True, default='')
    titulo5= models.CharField(max_length=250, blank=True, default='')
    titulo6= models.CharField(max_length=250, blank=True, default='')
    titulo7= models.CharField(max_length=250, blank=True, default='')
    titulo8= models.CharField(max_length=250, blank=True, default='')
    titulo9= models.CharField(max_length=250, blank=True, default='')
    data = models.DateField(auto_now=True)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True, max_length=200)

