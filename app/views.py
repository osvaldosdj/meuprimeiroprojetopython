from ast import Return
from django.http.response import HttpResponse
from django.forms import ModelForm
from django.shortcuts import render, redirect
from app.models import Item, Tipo
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

# Create your views here.
def item_list(request):
    itens = Item.objects.all()
    return render(
        request,
        'item_list.html',
        {
            'itens': itens
        }

    )

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, tipo):
        return "%s" % tipo.descricao

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'dataCadastro', 'estoqueMinimo', 'tipo']
        """fields = '__all__' """
    
    tipo = CustomMMCF(
        queryset=Tipo.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

@login_required
def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/item_create')
    return render (
        request,
        'item_create.html',
        {
             'form': form
        }
    )


class TipoForm(ModelForm):
    class Meta:
        model = Tipo
        fields = ['descricao']
        """ fields = '__all__' """
    
   
@login_required (login_url="/login")
def tipo_create(request):
    form = TipoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/tipo_create')
    return render (
        request,
        'tipo_create.html',
        {
             'form': form
        }
    )

def login(request):
    if request.method =="GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get ('username')
        senha = request.POST.get ('senha')

    user = authenticate(username=username, password=senha)
    
    if user:
        return HttpResponse('Usuário Autenticado')
    else:
        return HttpResponse('Usuario ou Senha incorretos')


@login_required(login_url="/login")
def cadUsuario(request):
    if request.method == "GET":
        return render (request, 'cadUsuario.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        passwd = request.POST.get('senha')
    
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Usuario Já cadastrado')
        user = User.objects.create_user(username=username, email=email, password=passwd)
        user.save()

        return HttpResponse ('Usuario cadastrado com sucesso')