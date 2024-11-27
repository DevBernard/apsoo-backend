from api import views
from django.urls import path


from rest_framework_simplejwt import views as jwtViews

urlpatterns = [
    path('createuser', views.CreateUser.as_view(), name='Criação de Usuario'),

    path('token',jwtViews.TokenObtainPairView.as_view(), name='Token de Autenticacao'),
    path('token/refresh', jwtViews.TokenRefreshView.as_view(), name='Token Refrescamentos'),
    path('token/verify', jwtViews.TokenVerifyView.as_view(), name='Token Verificações'),

    path('list-categorias', views.ListCategorias.as_view(), name='Listagem de Categorias'),
    path('list-produtos', views.ListProdutos.as_view(), name='Listagem de Produtos'),
    path('list-despensas', views.ListDespensas.as_view(), name='Listagem de Despensas'),
    path('list-mercados', views.ListMercados.as_view(), name='Listagem de Mercados'),
    path('list-marcas', views.ListMarcas.as_view(), name='Listagem de Marcas'),
    path('list-itens', views.ListItens.as_view(), name='Listagem de Itens'),
    path('list-lista-compras', views.ListListaCompras.as_view(), name='Listas de Compras'),
    #path('list-produto-quantidades', views.ListProdutoQuantidades.as_view(), name='Listagem de Quantidades de Produtos das Listas de Compras'),
    path('list-quantidades-padrao', views.ListQuantidadesPadrao.as_view(), name='Quantidades Padroes de Itens das Despensas'),

    #aqui ficam os endpoints das apis de detalhamento
    path('categoria/<int:pk>', views.DetailCategoria.as_view(), name='Categoria'),
    path('produto/<int:pk>', views.DetailProduto.as_view(), name='Produto'),
    path('despensa/<int:pk>', views.DetailDespensa.as_view(), name='Despensa'),
    path('despensa-itens/<int:pk>',views.DetailDespensaItens.as_view(), name='Itens de uma Despensa'),
    path('mercado/<int:pk>', views.DetailMercado.as_view(), name='Mercado'),
    path('marca/<int:pk>', views.DetailMarca.as_view(), name='Marca'),
    path('item/<int:pk>', views.DetailItem.as_view(), name='Item'),
    path('lista-compra/<int:pk>', views.DetailListaCompra.as_view(), name='Lista de Compras'),
    #path('produto-quantidade', views.DetailProdutoQuantidade.as_view(), name='Quantidade de Produtos das Listas de Compras'),
    #path('quantidade-padrao', views.DetailQuantidadePadrao.as_view(), name='Quantidades Padroes de Itens das Despensa'),
    path('gerar-lista-compra', views.GerarListaCompra.as_view(), name = 'Lista de Compras Gerada'),
    path('historico-consumo-usuario', views.DetailConsumoUsuario.as_view(), name='dt con usr'),
    path('historico-consumo-despensa', views.DetailConsumoDespensa.as_view(), name='dt con dsp'),
]