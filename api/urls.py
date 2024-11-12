from api import views
from django.urls import path

urlpatterns = [
    path('list-categorias', views.ListCategorias.as_view(), name= 'Listagem de Categorias'),
    path('list-produtos', views.ListProdutos.as_view(), name= 'Listagem de Produtos'),
    path('list-despensas', views.ListDespensas.as_view(), name= 'Listagem de Despensas'),
    path('list-mercados', views.ListMercados.as_view(), name= 'Listagem de Mercados'),
    path('list-marcas', views.ListMarcas.as_view(), name= 'Listagem de Marcas'),
    path('list-itens', views.ListItens.as_view(), name= 'Listagem de Itens'),
    path('list-lista-compras', views.ListListaCompras.as_view(), name= 'Listas de Compras'),
    path('list-produto-quantidades', views.ListProdutoQuantidades.as_view(), name= 'Listagem de Quantidades de Produtos das Listas de Compras'),
    path('list-quantidades-padrao', views.ListQuantidadesPadrao.as_view(), name= 'Quantidades Padroes de Itens das Despensas'),
]