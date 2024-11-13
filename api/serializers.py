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

class QuantidadePadraoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = QuantidadePadrao
        fields = ['produto','qtd_min','qtd_med','qtd_max']

class DespensaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True)
    quantidadepadrao_set = QuantidadePadraoSerializer(many=True)
    
    class Meta:
        model = Despensa
        fields = ['quantidadepadrao_set','descricao','categorias']

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
            'produto',
            'data_vencimento',
            'data_compra',
            'preco',
            'consumido',
            'mercado',
            'comprador',
            'despensa',
            ]

class ProdutoQuantidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoQuantidade
        fields = ['qtd','produto']

class ListaCompraSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    destino = DespensaSerializer() #queryset=Despensa.objects.only('descricao')
    produtoquantidade_set = ProdutoQuantidadeSerializer(many=True)

    class Meta:
        model = ListaCompra
        fields = ['produtoquantidade_set','usuario','destino']

