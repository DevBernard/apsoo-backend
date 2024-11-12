#from django.shortcuts import render
from rest_framework import generics

from api.serializers import *

class ListCategorias(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ListProdutos(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ListDespensas(generics.ListAPIView):
    queryset = Despensa.objects.all()
    serializer_class = DespensaSerializer

class ListMercados(generics.ListAPIView):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer

class ListMarcas(generics.ListAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ListItens(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ListListaCompras(generics.ListAPIView):
    queryset = ListaCompra.objects.all()
    serializer_class = ListaCompraSerializer

class ListProdutoQuantidades(generics.ListAPIView):
    queryset = ProdutoQuantidade.objects.all()
    serializer_class = ProdutoQuantidadeSerializer

class ListQuantidadesPadrao(generics.ListAPIView):
    queryset = QuantidadePadrao.objects.all()
    serializer_class = QuantidadePadraoSerializer