from django.views.generic import ListView, DetailView, FormView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from email.message import EmailMessage
import smtplib, os

from .models import Post
from .forms import ContatoForms


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'cards'
    paginate_by = 5
    ordering = ['data']


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class ContatoView(FormView):
    template_name = 'contact.html'
    form_class = ContatoForms
    success_url = reverse_lazy('contato')

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email1 = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']
        mensagem = form.cleaned_data['mensagem']

        email = EmailMessage()
        email["From"] = str(os.getenv('emailde'))
        email["To"] = str(os.getenv('emailpara'))
        email["Subject"] = f"Nova mensagem do blog"
        email.set_content(f'{nome} com email: {email1} e telefone: {telefone} enviou a seguinte mensagem: \n \n {mensagem}')

        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(str(os.getenv('emailde')), str(os.getenv('senha')))
        smtp.sendmail(str(os.getenv('emailde')), str(os.getenv('emailpara')), email.as_string())
        smtp.quit()

        return super().form_valid(form)


class BuscarView(ListView):
    model = Post
    template_name = 'buscar.html'
    context_object_name = 'cards'
    paginate_by = 5
    ordering = ['data']

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_buscar = self.request.GET.get('buscar')
        if nome_buscar:
            queryset = queryset.filter(nome__icontains=nome_buscar)
        return queryset
