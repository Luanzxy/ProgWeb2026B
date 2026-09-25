from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from loja.models.Favorito import Favorito
from loja.models.Produto import Produto


@login_required
def favoritar_produto_view(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    favorito, created = Favorito.objects.get_or_create(user=request.user, produto=produto)
    
    # Se já existia, remove ao clicar novamente (toggle)
    if not created:
        favorito.delete()
        
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def listar_favoritos_view(request):
    favoritos = Favorito.objects.filter(user=request.user)
    context = {
        'favoritos': favoritos
    }
    return render(request, 'favorito/favoritos-listar.html', context)