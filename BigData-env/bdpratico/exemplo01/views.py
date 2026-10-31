from django.shortcuts import render
from django.http import HttpResponse
from .models import pessoa
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return HttpResponse('EXEMPLO 01.')

def pagina0(request):
    return render(request, 'pagina0.html')

def pagina1(request):
    return render(request, 'pagina1.html')

def pagina2(request):
    dicionario = {}
    registros = pessoa.objects.all()
    dicionario['pessoas'] = registros
    return render(request, 'pagina2.html', dicionario)

def pagina3(request):
    dicionario = {}
    registros = pessoa.objects.all()
    dicionario['pessoas'] = registros
    return render(request, 'pagina3.html', dicionario)

def pagina4(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        funcao = request.POST.get('funcao')
        nascimento = request.POST.get('nascimento')
        ativo = request.POST.get('ativo')
        print("Nome:", nome)
        print("eMail:", email)
        print("Celular:", celular)
        print("Funcao:", funcao)
        print("Nascimento:", nascimento)
        print("ativo:", ativo)
    return render(request, 'exemplo01/pagina4.html')

class pessoa_create(CreateView):
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']

    def get_success_url(self):
        return reverse_lazy('pagina3_alias')

class pessoa_list(ListView):
    model = pessoa
    queryset = pessoa.objects.filter(ativo=True)

class pessoa_update(UpdateView):
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']

    def get_success_url(self):
        return reverse_lazy('pessoa_list_alias')

class pessoa_delete(DeleteView):
    model = pessoa
    fields = ['nome', 'email', 'celular', 'funcao', 'nascimento', 'ativo']
    template_name_suffix = '_delete'

    def get_success_url(self):
        return reverse_lazy('pessoa_list_alias')
