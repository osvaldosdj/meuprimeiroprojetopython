from django.forms import ModelForm
from django.shortcuts import render, redirect
from app.models import Item, Tipo
from django import forms

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