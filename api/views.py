#from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
#daqui, por ter importado as models, também joga as models pra cá
from api.serializers import *

class CreateUser(APIView):
    #queryset = Usuario.objects.all()
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']
        passwd = request.data['password']

        if Usuario.objects.filter(email=email).count() > 0:
            return Response(status=404, data={'response':'Já tem esse email cadastrado, bro'})

        user = Usuario.objects.create_user(email=email,password=passwd)
        user.save()

        return Response(status=201, data={'response':f'Usuario {email} Criado'})


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


class DetailConsumo(generics.ListAPIView):
    queryset = Consumo.objects.all()
    serializer_class = ConsumoSerializer
    class Meta:
        fields = '__all__'
        abstract = True


class DetailConsumoUsuario(DetailConsumo):
    def get_queryset(self):
        id = self.request.GET.get('usuario_id')
        queryset = Consumo.objects.filter(usuario__id=id) \
                                  .order_by('-data_hora')
        return queryset

class DetailConsumoDespensa(DetailConsumo):
    def get_queryset(self):
        id = self.request.GET.get('despensa_id')
        queryset = Consumo.objects.filter( item__despensa__id=id) \
                                  .order_by('-data_hora')
        return queryset

class GerarListaCompra(APIView):
    def get(self, request):
        listaCompra = {}
        req = request.data

        listaObj = ListaCompra.objects.get(pk=request.data['lista_id'])
        despensa = listaObj.destino

        c_estoque = req['considerar_estoque_despensa']
        c_qtd_pad = req['considerar_quantidade_padrao']
        c_qtd_pad = c_qtd_pad.lower() if c_qtd_pad else 'affs velho'

        for prodqtd in listaObj.produtoquantidade_set.all():
            listaCompra[str(prodqtd.produto)] = prodqtd.qtd

        #subtraindo da quantidade padrao
        qtd_pad = despensa.quantidadepadrao_set

        for prod in listaCompra.keys():
            try:
                qtd_pad_prod = qtd_pad.get(produto__nome=prod)
            except:
                continue
            the_qtd_pad_prod = the_qtd_pad_prod = qtd_pad_prod.qtd_max if qtd_pad_prod.qtd_max else 0
            match c_qtd_pad:
                case 'min':
                    the_qtd_pad_prod = qtd_pad_prod.qtd_min if qtd_pad_prod.qtd_min else qtd_pad_prod.qtd_med
                case 'med':
                    the_qtd_pad_prod = qtd_pad_prod.qtd_med if qtd_pad_prod.qtd_med else the_qtd_pad_prod
                case _: pass
            if listaCompra[prod] > the_qtd_pad_prod:
                listaCompra[prod] = the_qtd_pad_prod

        if c_estoque:
            for prod in listaCompra:
                qtd_itens = despensa.item_set.filter(produto__nome=prod).count()
                listaCompra[prod] -= qtd_itens

        for prod in listaCompra.copy().keys():
            if listaCompra[prod] <= 0:
                listaCompra.pop(prod)
        
        if not listaCompra:
            listaCompra={'response': 'lista vazia, bro. A despensa já tem os itens necessários nas quantidades solicitadas ou o estoque está cheio'}
            return Response(data=listaCompra, status=200)
            
        listaCompra={'response': listaCompra}
        return Response(data=listaCompra, status=200)


