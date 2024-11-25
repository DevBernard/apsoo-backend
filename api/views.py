#from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
#daqui, por ter importado as models, também joga as models pra cá
from api.serializers import *

@api_view(['POST'])
@permission_classes([AllowAny])
def createuser(request):
    email = request.data['email']
    passwd = request.data['password']

    if (Usuario.objects.filter(email=email).count() > 0):
        return Response(status=404, data='Já tem esse email cadastrado, bro')

    user = Usuario.objects.create_user(email=email,password=passwd)
    user.save()

    return Response(status=201, data=f'Usuario f{email} Criado')


class ListCategorias(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ListProdutos(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ListDespensas(generics.ListCreateAPIView):
    queryset = Despensa.objects.all()
    serializer_class = DespensaSerializer

class ListMercados(generics.ListCreateAPIView):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer

class ListMarcas(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class ListItens(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ListListaCompras(generics.ListCreateAPIView):
    queryset = ListaCompra.objects.all()
    serializer_class = ListaCompraSerializer

class ListProdutoQuantidades(generics.ListCreateAPIView):
    queryset = ProdutoQuantidade.objects.all()
    serializer_class = ProdutoQuantidadeSerializer

class ListQuantidadesPadrao(generics.ListCreateAPIView):
    queryset = QuantidadePadrao.objects.all()
    serializer_class = QuantidadePadraoSerializer



class DetailCategoria(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class DetailProduto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class DetailDespensa(generics.RetrieveUpdateDestroyAPIView):
    queryset = Despensa.objects.all()
    serializer_class = DespensaSerializer

class DetailMercado(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer

class DetailMarca(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class DetailItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class DetailListaCompra(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListaCompra.objects.all()
    serializer_class = ListaCompraSerializer

class DetailProdutoQuantidade(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProdutoQuantidade.objects.all()
    serializer_class = ProdutoQuantidadeSerializer

class DetailQuantidadePadrao(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuantidadePadrao.objects.all()
    serializer_class = QuantidadePadraoSerializer

class DetailDespensaItens(generics.RetrieveAPIView):
    queryset = Despensa.objects.all()
    serializer_class = DespensaItensSerializer