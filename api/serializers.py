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

from django.contrib.auth import get_user_model

Usuario = get_user_model()

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email','password']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nome']

class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Categoria.objects.all(),source='categoria')
    prior = serializers.ChoiceField(choices=Produto.PrioridadeChoices)

    class Meta:
        model = Produto
        fields = '__all__'#['id','nome','categoria','prior']

class QuantidadePadraoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Produto.objects.all(),source='produto')

    class Meta:
        model = QuantidadePadrao
        fields = '__all__'

class DespensaSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True, read_only=True)
    categorias_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True,queryset=Categoria.objects.all(),source='categorias')
    #tvz de pau aqui. ---> atualização: deu bom demais

    quantidadepadrao_set = QuantidadePadraoSerializer(many=True, read_only=True)
    quantidadepadrao_set_ids = serializers.PrimaryKeyRelatedField(many=True,write_only=True,queryset=QuantidadePadrao.objects.all(),source='quantidadepadrao_set')
    
    class Meta:
        model = Despensa
        fields = '__all__'#['id','quantidadepadrao_set','descricao','categorias']

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = ['id','nome']

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id','nome']

class ItemSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    mercado = MercadoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Produto.objects.all(),source='produto')
    mercado_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Mercado.objects.all(),source='mercado')
    comprador = serializers.StringRelatedField()
    class Meta:
        model = Item
        fields = '__all__'

class DespensaItensSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True, read_only=True)
    item_set_ids = serializers.PrimaryKeyRelatedField(many=True,write_only=True,queryset=Item.objects.all(),source='item_set')
    class Meta:
        model = Despensa
        fields = '__all__'#['id','item_set']

class ProdutoQuantidadeSerializer(serializers.ModelSerializer):
    produto = serializers.StringRelatedField()
    class Meta:
        model = ProdutoQuantidade
        fields = '__all__'

class ListaCompraSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()
    destino = DespensaSerializer() #queryset=Despensa.objects.only('descricao')
    produtoquantidade_set = ProdutoQuantidadeSerializer(many=True,read_only=True)
    produtoquantidade_set_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True,queryset=ProdutoQuantidade.objects.all(),source='produtoquantidade_set')

    class Meta:
        model = ListaCompra
        fields = '__all__'#['id','produtoquantidade_set','usuario','destino']

