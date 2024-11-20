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
        fields = ['id','nome']

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    prior = serializers.ChoiceField(choices=Produto.PrioridadeChoices)

    class Meta:
        model = Produto
        fields = ['id','nome','categoria','prior']

class QuantidadePadraoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()

    class Meta:
        model = QuantidadePadrao
        fields = ['id','produto','qtd_min','qtd_med','qtd_max']

class DespensaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True)
    quantidadepadrao_set = QuantidadePadraoSerializer(many=True)
    
    class Meta:
        model = Despensa
        fields = ['id','quantidadepadrao_set','descricao','categorias']

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = ['id','nome']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id','nome']

class ItemSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer()
    mercado = MercadoSerializer()
    comprador = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = ['id',
            'produto',
            'data_vencimento',
            'data_compra',
            'preco',
            'consumido',
            'mercado',
            'comprador',
            'despensa',
            ]

class DespensaItensSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = Despensa
        fields = ['id','item_set']

class ProdutoQuantidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoQuantidade
        fields = ['id','qtd','produto']

class ListaCompraSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    destino = DespensaSerializer() #queryset=Despensa.objects.only('descricao')
    produtoquantidade_set = ProdutoQuantidadeSerializer(many=True)

    class Meta:
        model = ListaCompra
        fields = ['id','produtoquantidade_set','usuario','destino']

