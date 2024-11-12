from rest_framework import serializers

from despensa.models import (
    Categoria,
    Produto,
    Despensa,
    Mercado,
    Marca,
    Item,
    ListaCompra,
    ProdutoQuantidade,
    QuantidadePadrao
)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nome']

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    prior = serializers.ChoiceField(choices=Produto.PrioridadeChoices)

    class Meta:
        model = Produto
        fields = ['nome','categoria','prior']

class DespensaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True)
    
    class Meta:
        model = Despensa
        fields = ['descricao','categorias']

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = ['nome']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['nome']

class ItemSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    mercado = MercadoSerializer()
    comprador = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = [
            'data_vencimento',
            'data_compra',
            'preco',
            'consumido',
            'mercado',
            'comprador',
            'despensa',
            ]

class ListaCompraSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    destino = DespensaSerializer() #queryset=Despensa.objects.only('descricao')

    class Meta:
        model = ListaCompra
        fields = ['usuario','destino']

class ProdutoQuantidadeSerializer(serializers.ModelSerializer):
    lista_compra = ListaCompraSerializer()
    
    class Meta:
        model = ProdutoQuantidade
        fields = ['lista_compra','qtd','produto']

class QuantidadePadraoSerializer(serializers.ModelSerializer):
    despensa = DespensaSerializer()
    produto = ProdutoSerializer()

    class Meta:
        model = QuantidadePadrao
        fields = ['despensa','produto','qtd_min','qtd_med','qtd_max']