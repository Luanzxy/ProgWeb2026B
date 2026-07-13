from django.shortcuts import render, redirect
from loja.models import Categoria

def list_categoria_view(request, id=None):
    categoria_nome = request.GET.get("categoria")
    categorias = Categoria.objects.all()
    
    if categoria_nome is not None:
        categorias = categorias.filter(Categoria__contains=categoria_nome)
        
    if id is not None:
        categorias = categorias.filter(Categoria__contains=categoria_nome)
        
    context = {'categorias': categorias}
    return render(request, template_name='categoria/categoria.html', context=context, status=200)

def create_categoria_view(request, id=None):
    if request.method == 'POST':
        categoria_nome = request.POST.get("Categoria") # Pega o valor do input name="Categoria"
        try:
            obj_categoria = Categoria()
            obj_categoria.Categoria = categoria_nome # Atribui ao campo do seu Model
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria_nome)
        except Exception as e:
            print("Erro inserindo categoria: %s" % e)
        return redirect("/categoria") # Redireciona para o prefixo da sua rota de listagem
        
    return render(request, template_name='categoria/categoria-create.html', status=200)

def edit_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    
    context = { 'categoria': categoria }
    return render(request, template_name='categoria/categoria-edit.html', context=context, status=200)

def edit_categoria_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        categoria_nome = request.POST.get("Categoria")
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            obj_categoria.Categoria = categoria_nome
            obj_categoria.save()
            print("Categoria %s editada com sucesso" % categoria_nome)
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")

def details_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    
    context = { 'categoria': categoria }
    return render(request, template_name='categoria/categoria-details.html', context=context, status=200)

def delete_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    
    context = { 'categoria': categoria }
    return render(request, template_name='categoria/categoria-delete.html', context=context, status=200)

def delete_categoria_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
    try:
        Categoria.objects.filter(id=id).delete()
        print("Categoria excluída com sucesso")
    except Exception as e:
        print("Erro excluindo categoria: %s" % e)
    return redirect("/categoria")