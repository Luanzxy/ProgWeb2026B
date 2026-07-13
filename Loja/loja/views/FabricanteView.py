from django.shortcuts import render, redirect
from loja.models import Fabricante
from loja.forms.FabricanteForm import FabricanteForm

def list_fabricante_view(request, id=None):
    fabricante_nome = request.GET.get("fabricante")
    fabricantes = Fabricante.objects.all()
    
    if fabricante_nome is not None:
        fabricantes = fabricantes.filter(Fabricante__contains=fabricante_nome)
        
    context = {'fabricantes': fabricantes}
    return render(request, template_name='fabricante/fabricante.html', context=context, status=200)

def create_fabricante_view(request, id=None):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/fabricante")
            except Exception as e:
                print("Erro inserindo fabricante: %s" % e)
    else:
        form = FabricanteForm()
        
    context = {'form': form}
    return render(request, template_name='fabricante/fabricante-create.html', context=context, status=200)

def edit_fabricante_view(request, id=None):
    fabricantes = Fabricante.objects.all()
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    
    form = FabricanteForm(instance=fabricante)
    context = { 'fabricante': fabricante, 'form': form }
    return render(request, template_name='fabricante/fabricante-edit.html', context=context, status=200)

def edit_fabricante_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        fabricante_obj = Fabricante.objects.filter(id=id).first()
        form = FabricanteForm(request.POST, instance=fabricante_obj)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print("Erro salvando edição de fabricante: %s" % e)
    return redirect("/fabricante")

def details_fabricante_view(request, id=None):
    fabricantes = Fabricante.objects.all()
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    
    context = { 'fabricante': fabricante }
    return render(request, template_name='fabricante/fabricante-details.html', context=context, status=200)

def delete_fabricante_view(request, id=None):
    fabricantes = Fabricante.objects.all()
    if id is not None:
        fabricantes = fabricantes.filter(id=id)
    fabricante = fabricantes.first()
    
    context = { 'fabricante': fabricante }
    return render(request, template_name='fabricante/fabricante-delete.html', context=context, status=200)

def delete_fabricante_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
    try:
        Fabricante.objects.filter(id=id).delete()
    except Exception as e:
        print("Erro excluindo fabricante: %s" % e)
    return redirect("/fabricante")