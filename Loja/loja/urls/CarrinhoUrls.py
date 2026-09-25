from django.urls import path
from loja.views.CarrinhoView import create_carrinhoitem_view, list_carrinho_view, confirmar_carrinho_view, remover_item_view, aumentar_carrinhoitem_view, diminuir_carrinhoitem_view
urlpatterns = [
    path("", list_carrinho_view, name='list_carrinho'),
    path("<int:produto_id>", create_carrinhoitem_view, name='create_carrinhoitem'),
    path("confirmar", confirmar_carrinho_view, name='confirmar_carrinho'),
    path('remover/<int:item_id>/', remover_item_view, name='remover_carrinhoitem'),
    path('aumentar/<int:item_id>', aumentar_carrinhoitem_view, name='aumentar_carrinhoitem'),
    path('diminuir/<int:item_id>', diminuir_carrinhoitem_view, name='diminuir_carrinhoitem'),
]